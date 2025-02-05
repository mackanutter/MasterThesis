import numpy as np
import matplotlib.pyplot as plt

def main():

    def calc_dist_to_interface(grid,point):
        # Center is probably roughly same spot always
        # Find closes index where grid == 0
        # Calculate manhattan distance to that point
        # Return distance
        size = grid.shape[0]
        x0, y0 = point
        
        
    def initialize_grid(size):
        """Initialize a square grid with a single cell in the center."""
        grid = np.zeros((size, size), dtype=int)
        center = size // 2
        for x,y in np.ndindex(grid.shape):
            if (x-center)**2 + (y-center)**2 < 100:
                grid[x,y] = 1
        return grid
    
    def random_one(grid):
        # Find the indices where the matrix equals 1
        indices = np.argwhere(grid == 1)
        if indices.size == 0:
            raise ValueError("No elements with value 1 found in the matrix.")
        # Choose a random row from the indices
        random_index = indices[np.random.choice(len(indices))]
        return np.array(random_index)

    def grow(grid,prob):
        """Use Gillespie algorithm"""
        size = grid.shape[0]

        new_grid = grid.copy()

        # Time to next event? maybe implement latter as a function
        # Focus on the lattice and event parameters

        # Choose a random cell
        red_cell = random_one(grid)
        print(red_cell)
        
        # calculate manhattan distance to interface

    grid_size = 1000  # Size of the grid
    steps = 500       # Number of growth steps
    probability = 0.5 # Probability of growth

    grid = initialize_grid(grid_size)
    print(grid)
    for _ in range(steps):
        grid = grow(grid,probability)

    plt.imshow(grid, cmap="binary")
    plt.tight_layout()
    plt.savefig("../figures/growth.png")
    plt.show()

if __name__ == "__main__":
    main()


"""
Notes and ideas
How to calculate distance to interface?

"""