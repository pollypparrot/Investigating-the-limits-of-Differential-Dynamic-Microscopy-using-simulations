import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N_particle = 10  # number of particles
mean = 0
comp = 100  # number of computations
dt = 0.01  # time step size

k_B = 1.38e-23  # boltzmann constant
viscosity = 1e-3
a = 0.5e-6  # radius of sphere
temperature = 300
diffusivity = (k_B * temperature) / (6 * np.pi * viscosity * a)
s = 3  # splodge size
constant_factor = 1 / (2 * s ** 2)

# calculate standard deviation at given time
def stand_dev(time):
    return np.sqrt(2 * diffusivity * time)

# initialize arrays to store position information
dx_array = 1e6 * np.random.normal(loc=mean, scale=stand_dev(dt), size=(comp * N_particle, 1))
dy_array = 1e6 * np.random.normal(loc=mean, scale=stand_dev(dt), size=(comp * N_particle, 1))
# set it so no change for first position
dx_array[0] = 0
dy_array[0] = 0

grid = 512  # n x n micrometer grid size

# plots initial position
Z = np.zeros((grid, grid))  # grid data

# initialize array of initial positions
x_p_array = np.random.randint(1, grid - 1, size=N_particle).astype(float)
y_p_array = np.random.randint(1, grid - 1, size=N_particle).astype(float)

# precompute constants
constant_factor = 1 / (2 * s ** 2)

# plots moving particle
for computations in range(comp):
    Z.fill(0)
    
    # update particle positions with wrapping
    x_p_array = (x_p_array + dx_array[computations:computations + N_particle, 0]) % grid
    y_p_array = (y_p_array + dy_array[computations:computations + N_particle, 0]) % grid
    
    x_p_array = np.clip(np.round(x_p_array), 1, grid - 2)
    y_p_array = np.clip(np.round(y_p_array), 1, grid - 2)

    Z[x_p_array.astype(int), y_p_array.astype(int)] = 1

    # colors nearby pixels
    value = np.sum(
        np.exp(-((np.arange(grid)[:, None, None] - x_p_array) ** 2 + (np.arange(grid)[None, :, None] - y_p_array) ** 2) * constant_factor),
        axis=2,
    )
    # value doesn't exceed 1
    value = np.clip(value, 0, 1)
    
    plt.imshow(value, cm.get_cmap("gray"), interpolation='none')
    plt.axis('off')
    plt.show()