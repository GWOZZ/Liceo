import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from matplotlib import cm
from scipy.interpolate import griddata
from matplotlib.ticker import MultipleLocator

x = [0, 4.5, 9.0, 0, 4.5, 9.0, 0, 4.5, 9.0, 0, 4.5, 9.0, 0, 4.5, 9.0, -0.5, -0.5, -0.5, 9.5, 9.5, 9.5]

y =  [2.0, 2.0, 2.0, 4.0, 4.0, 4.5, 6.5, 7.0, 7.0, 9.5, 9.5, 9.5, 12.0, 12.0, 12.0, 1.5, 12.5, 4, 1.5, 12.5, 4]

z = [2.50, 2.50, 2.50, 4.0, 4.0, 4.0, 6.0, 6.0, 6.0, 8.0, 8.0, 8.0, 10.0, 10.0, 10.0, 2.499, 10.001, 4, 2.499, 10.001, 4]

x1 = [x[:15]]

y1 =  [y[:15]]

z1 = [z[:15]]

plt.rcParams.update({
    "text.usetex": True})

# Define the grid for the color plot
grid_resolution = 500
xi = np.linspace(min(x), max(x), grid_resolution)
yi = np.linspace(min(y), max(y), grid_resolution)
xi, yi = np.meshgrid(xi, yi)

# Interpolate the values on the grid using 'linear' method
zi = griddata((x, y), z, (xi, yi), method='linear')

# Create the plot with more levels for smooth color transition
num_levels = 100
contour = plt.contourf(xi, yi, zi, num_levels, cmap=cm.viridis, zorder=0)  # Set zorder=0

# Add scatter plot of the original data points with circles
scatter = plt.scatter(x1, y1, c=z1, cmap=cm.viridis, edgecolors=(0, 0, 0, 0.5), linewidths=1, facecolors=1, zorder=1)

plt.minorticks_on()
plt.xticks(ticks=[0.0 , 2.0, 4.0, 6.0, 8.0, 10.0, 12.0])
plt.yticks(ticks=[2.0, 4.0, 6.0, 8.0, 10.0, 12.0])
plt.xlabel(r"$x \pm \delta x \;\mathrm{(cm)}$")
plt.ylabel(r"$y \pm \delta x \;\mathrm{(cm)}$")
plt.colorbar(label=r'$\Delta V \pm \delta \Delta V \;\mathrm{(V)}$', extend='both', ticks=[2.5, 4.0, 6.0, 8.0, 10.0, 12.0])
plt.xlim([-0.5, 9.5])
plt.ylim([1.5, 12.5])

models = []
for i in range (5):
    models.append(np.poly1d(np.polyfit(x[:3], y[3*i:3*i+3], 1)))
    plt.plot(np.linspace(-0.5, 13.5, 50), models[i](np.linspace(-0.5, 13.5, 50)), color='red', alpha=0.5)

plt.show()