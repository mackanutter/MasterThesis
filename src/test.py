import matplotlib.pyplot as plt
import numpy as np

def main():
    def initialize_grid(size):
        """Initialize a square grid with a single cell in the center."""
        grid = np.zeros((size, size), dtype=int)
        center = size // 2
        for x,y in np.ndindex(grid.shape):
            if (x-center)**2 + (y-center)**2 < 100:
                grid[x,y] = 1
        return grid

    def grow(grid, prob=1.0):
        """
        Grow the cell colony based on adjacency rules.
        Each empty cell adjacent to an occupied cell has a chance to become occupied.
        """
        size = grid.shape[0]
        new_grid = grid.copy()
        for x in range(size):
            for y in range(size):
                if grid[x, y] == 1:
                    # Try to grow in the four cardinal directions
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < size and 0 <= ny < size and grid[nx, ny] == 0:
                            if np.random.random() < prob:
                                new_grid[nx, ny] = 1
        return new_grid

    def simulate_growth(steps, size, prob=1.0):
        """Simulate the growth process over multiple steps."""
        grid = initialize_grid(size)
        for _ in range(steps):
            grid = grow(grid, prob)
        return grid

    def visualize_grid(grid):
        """Visualize the grid ."""
        plt.imshow(grid, cmap="binary")
        plt.tight_layout()
        plt.savefig("../figures/growth.png")
        plt.show()

    # Parameters
    grid_size = 500  # Size of the grid
    steps = 100       # Number of growth steps
    probability = 0.5  # Probability of growth

    # Simulate and visualize
    growth_process = simulate_growth(steps, grid_size, probability)
    visualize_grid(growth_process)

if __name__ == "__main__":
    main()

