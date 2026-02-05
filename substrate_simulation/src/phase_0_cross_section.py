import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys

# --- Simulation Parameters ---

# Grid
GRID_SIZE = 300  # Number of points in each dimension
DX = 1.0         # Grid spacing

# World Physics
WIND_SPEED = 60.0

# Porous Medium Model
DECAY_LENGTH = 30.0 # Characteristic depth for wind velocity to decay

# --- New Unified Physics Model ---
# The speed function F is a balance of new material gain vs. net material loss.
# F(V) = Gain(V) - Loss(V)
# Equilibrium is where F(V) = 0.

# Gain via Atmospheric Accretion (particles trapped in the screen)
# Proportional to local wind speed V.
K_ACCRETION = 0.1

# Loss via Net Erosion (Shattering minus Recapture/Repair)
# Gross Shattering is proportional to local wind speed V.
K_SHATTER = 0.8
# Recapture probability is higher at lower local speeds. P = exp(-k*V)
RECAPTURE_VELOCITY_SCALE = 0.08 # k

# Simulation Loop
N_STEPS = 5000
DT = 0.1
PLOT_EVERY = 20
REINIT_EVERY = 10 # Reinitialize more often for stability

class LevelSetTower:
    """
    Represents the tower cross-section using a level-set method
    and a porous medium "screen with drag" model for wind.
    """
    def __init__(self, size, dx, radius):
        self.size = size
        self.dx = dx
        
        # Create grid
        grid_range = np.arange(-size // 2, size // 2) * dx
        self.x, self.y = np.meshgrid(grid_range, grid_range, indexing='ij')
        
        # Initialize phi as a signed distance function for a circle
        center_x, center_y = -GRID_SIZE // 4 * dx, 0
        self.phi = np.sqrt((self.x - center_x)**2 + (self.y - center_y)**2) - radius

    def _calculate_velocity_field(self):
        """
        Calculates the drag-reduced wind field V(x,y) across the grid.
        Wind flows left-to-right (along axis 1).
        """
        v_grid = np.zeros_like(self.phi)
        v_grid[:, 0] = WIND_SPEED

        # Wind decays exponentially with depth into the medium
        decay_factor = np.exp(-self.dx / DECAY_LENGTH)

        for j in range(1, self.size): # Iterate columns left-to-right
            v_prev = v_grid[:, j-1]
            # Check if current cell is inside the tower
            is_inside = self.phi[:, j] < 0
            # Apply decay if inside, otherwise velocity persists
            v_grid[:, j] = np.where(is_inside, v_prev * decay_factor, v_prev)
            
        return v_grid

    def _calculate_interface_speed_F(self):
        """
        Calculates the normal speed F based on the unified physics model.
        F(V) = Gain(V) - Loss(V)
        """
        v_local = self._calculate_velocity_field()

        # Rate of Gain (Atmospheric Accretion)
        rate_of_gain = K_ACCRETION * v_local

        # Rate of Loss (Net Erosion)
        gross_shattering = K_SHATTER * v_local
        p_recapture = np.exp(-RECAPTURE_VELOCITY_SCALE * v_local)
        rate_of_loss = gross_shattering * (1.0 - p_recapture)
        
        # F is the net speed: positive for growth, negative for erosion
        F = rate_of_gain - rate_of_loss

        return F

    def step(self):
        """
        Evolves the level-set function phi by one time step.
        """
        F = self._calculate_interface_speed_F()
        
        grad_phi_y, grad_phi_x = np.gradient(self.phi, self.dx)
        norm_grad_phi = np.sqrt(grad_phi_x**2 + grad_phi_y**2)
        norm_grad_phi[norm_grad_phi < 1e-8] = 1e-8

        # Evolve phi: phi_t + F * |grad(phi)| = 0  =>  phi_t = -F * |grad(phi)|
        phi_t = -F * norm_grad_phi
        self.phi += DT * phi_t

    def reinitialize(self, steps=10):
        phi_0 = self.phi.copy()
        dtau = self.dx / 2.0
        for _ in range(steps):
            s = np.sign(phi_0)
            
            gx_fwd = (np.roll(self.phi, -1, axis=1) - self.phi) / self.dx
            gx_bwd = (self.phi - np.roll(self.phi, 1, axis=1)) / self.dx
            gy_fwd = (np.roll(self.phi, -1, axis=0) - self.phi) / self.dx
            gy_bwd = (self.phi - np.roll(self.phi, 1, axis=0)) / self.dx

            grad_phi_plus_x = np.maximum(gx_bwd, 0)**2 + np.minimum(gx_fwd, 0)**2
            grad_phi_minus_x = np.minimum(gx_bwd, 0)**2 + np.maximum(gx_fwd, 0)**2
            grad_phi_plus_y = np.maximum(gy_bwd, 0)**2 + np.minimum(gy_fwd, 0)**2
            grad_phi_minus_y = np.minimum(gy_bwd, 0)**2 + np.maximum(gy_fwd, 0)**2
            
            grad_phi_norm_sq = np.where(s > 0, grad_phi_plus_x + grad_phi_plus_y,
                                        np.where(s < 0, grad_phi_minus_x + grad_phi_minus_y, 0))
            grad_phi_norm = np.sqrt(grad_phi_norm_sq)
            
            self.phi -= dtau * s * (grad_phi_norm - 1)

def main():
    print("Starting Substrate Tower Cross-Section Simulation (Phase 0)...")
    print("Using Unified Porous Medium Model.")

    tower = LevelSetTower(GRID_SIZE, DX, radius=GRID_SIZE // 6 * DX)

    fig, ax = plt.subplots(figsize=(12, 10))
    contour_artist = None
    imshow_artist = None

    def init():
        ax.set_xlim(tower.x.min(), tower.x.max())
        ax.set_ylim(tower.y.min(), tower.y.max())
        ax.set_aspect('equal')
        ax.set_title("Tower Cross-Section (Unified Porous Medium Model)")
        ax.set_xlabel("Wind Direction (m)")
        ax.set_ylabel("Crosswind (m)")
        ax.grid(True)
        return []

    def update(frame):
        nonlocal contour_artist, imshow_artist
        sys.stdout.write(f"Step {frame * PLOT_EVERY}/{N_STEPS}\r")
        sys.stdout.flush()
        
        for _ in range(PLOT_EVERY):
            tower.step()
        
        if frame % REINIT_EVERY == 0:
            tower.reinitialize()
        
        if contour_artist:
            for c in contour_artist.collections:
                c.remove()
        if imshow_artist:
            imshow_artist.remove()
        
        v_grid = tower._calculate_velocity_field()
        imshow_artist = ax.imshow(v_grid.T, extent=(tower.x.min(), tower.x.max(), tower.y.min(), tower.y.max()),
                                  origin='lower', cmap='viridis', alpha=0.5, vmin=0, vmax=WIND_SPEED)
        contour_artist = ax.contour(tower.x, tower.y, tower.phi, [0], colors='red', linewidths=2)
        
        # The list of collections is what needs to be returned for the animation.
        return list(contour_artist.collections) + [imshow_artist]

    ani = FuncAnimation(fig, update, frames=N_STEPS // PLOT_EVERY,
                        init_func=init, blit=False, repeat=False)
    
    # Add a colorbar for the wind field
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=0, vmax=WIND_SPEED))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, label='Local Wind Speed (m/s)', shrink=0.8)

    plt.show()
    print(f"\nSimulation finished.")


if __name__ == "__main__":
    main()