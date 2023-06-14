import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from matplotlib import cm
from scipy.interpolate import interp1d
from scipy.interpolate import griddata
from matplotlib.ticker import MultipleLocator
from pylab import *
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

x = [0, 4.5, 9.0, 0, 4.5, 9.0, 0, 4.5, 9.0, 0, 4.5, 9.0, 0, 4.5, 9.0, -0.5, -0.5, -0.5, 9.5, 9.5, 9.5]

y =  [2.0, 2.0, 2.0, 4.0, 4.0, 4.5, 6.5, 7.0, 7.0, 9.5, 9.5, 9.5, 12.0, 12.0, 12.0, 1.5, 12.5, 4, 1.5, 12.5, 4]

z = [2.50, 2.50, 2.50, 4.0, 4.0, 4.0, 6.0, 6.0, 6.0, 8.0, 8.0, 8.0, 10.0, 10.0, 10.0, 2.499, 10.001, 4, 2.499, 10.001, 4]


grid_resolution = 60
xi = np.linspace(min(x), max(x), grid_resolution)
yi = np.linspace(min(y), max(y), grid_resolution)
xi, yi = np.meshgrid(xi, yi)

zi = griddata((x, y), z, (xi, yi), method='cubic')

gradient = np.gradient(zi)
mag = np.sqrt(abs(-gradient[0])**2 + abs(-gradient[1])**2)

num_levels = 500
contour = plt.contourf(xi, yi, mag, num_levels, cmap=cm.viridis, zorder=0)

plt.minorticks_on()
plt.xticks(ticks=(tcks:=[0.0 , 2.0, 4.0, 6.0, 8.0, 10.0, 12.0]))
plt.yticks(ticks=tcks)
plt.xlabel(r"$x \pm \delta x \;\mathrm{(cm)}$")
plt.ylabel(r"$y \pm \delta x \;\mathrm{(cm)}$")

plt.colorbar(label=r'$|\vec{E}| \pm \delta |\vec{E}| \;\mathrm{(V/m)}$', ticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4])
plt.xlim([-0.5, 9.5])
plt.ylim([1.5, 12.5])

plt.savefig('plot3.png', dpi=500)
plt.show()
