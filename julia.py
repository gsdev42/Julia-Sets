import numpy as np
import matplotlib.pyplot as plt

def generate_julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    img = np.zeros(Z.shape, dtype=float)

    for i in range(max_iter):
        Z = Z**2 + c
        mask = np.abs(Z) < 1000
        img += mask

    return img

def plot_julia_set(julia_set):
    plt.imshow(julia_set, cmap='hot', extent=(-2, 2, -2, 2))
    plt.colorbar()
    plt.title('Julia Set')
    plt.show()

# Set parameters
width, height = 800, 800
xmin, xmax = -2, 2
ymin, ymax = -2, 2
c = complex(-0.8, 0.156)  # You can experiment with different values of 'c'
max_iter = 100

# Generate and plot the Julia set
julia_set = generate_julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter)
plot_julia_set(julia_set)
