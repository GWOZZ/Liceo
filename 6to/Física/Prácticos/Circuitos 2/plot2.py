import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from matplotlib import cm
from scipy.interpolate import interp1d
from scipy.interpolate import griddata
from matplotlib.ticker import MultipleLocator

x = [0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, -10, -10, 20, 20]

y =  [0.75, 0.7, 0.6, 0.6, 0.65, 0.5, 0.45, 0.5, 0.5, 0.7, 1, 2.1, 1.6, 1.5, 1.3, 1.2, 1.0, 0.9, 0.9, 1.1, 1.4, 2, 3.3, 2.8, 2.5, 2.2, 2, 1.5, 1.5, 1.4, 1.6, 2.4, 3.2, 4.7, 4, 3.4, 3.1, 2.7, 2.3, 2.1, 2.0, 2.1, 3.2, 4.4, 7, 6, 4.75, 4.2, 3.5, 2.8, 2.7, 2.6, 2.8, 4, 6.2, 13.2, 9.5, 6.5, 5.6, 4.5, 3.4, 3.1, 3.1, 3.7, 5.5, 12.1, -0.5, 20, -0.5, 20]

z = [2.50, 2.50, 2.50, 2.50, 2.50, 2.50, 2.50, 2.50, 2.50, 2.50, 2.50, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 2.4999, 12.0, 2.4999, 12.0]

x1 = [x[:66]]

y1 =  [y[:66]]

z1 = [z[:66]]

grid_resolution = 500
xi = np.linspace(min(x), max(x), grid_resolution)
yi = np.linspace(min(y), max(y), grid_resolution)
xi, yi = np.meshgrid(xi, yi)

zi = griddata((x, y), z, (xi, yi), method='linear', fill_value=0)

num_levels = 100
contour = plt.contourf(xi, yi, zi, num_levels, cmap=cm.viridis, zorder=0)

scatter = plt.scatter(x1, y1, c=z1, cmap=cm.viridis, edgecolors=(0, 0, 0, 0.5), linewidths=1, facecolors=1, zorder=1)

plt.minorticks_on()
plt.xticks(ticks=(tcks:=[0.0 , 2.0, 4.0, 6.0, 8.0, 10.0, 12.0]))
plt.yticks(ticks=tcks)
plt.xlabel(r"$x \pm \delta x \;\mathrm{(cm)}$")
plt.ylabel(r"$y \pm \delta y \;\mathrm{(cm)}$")
plt.colorbar(label=r'$\Delta V \pm \delta \Delta V \;\mathrm{(V)}$', extend='both', ticks=[2.5, 4.0, 6.0, 8.0, 10.0, 12.0])
plt.xlim([-0.5, 13.5])
plt.ylim([0, 14])

models = []
for i in range (6):
    models.append(interp1d(x[:11], y[11*i:11*i+11], kind = "cubic", fill_value="extrapolate"))
    plt.plot(np.linspace(-0.5, 13.5, 50), models[i](np.linspace(-0.5, 13.5, 50)), color='red', alpha=0.5)

plt.savefig('plot2.png', dpi=300)
plt.show()