import math
import matplotlib.pyplot as plt
import numpy as np

xvalues, yvalues = np.meshgrid(np.arange(-10, 10, 0.1), np.arange(-10, 10, 0.1))

plane_x1 = np.arange(-8, 8, 1)
plane_x2 = (-3) * plane_x1  # фазовая плоскость
separ_y = np.arange(-8, 8, 1)
separ_x_1 = ((-math.sqrt(3) - 1)/2) * separ_y
separ_x_2 = ((math.sqrt(3) - 1)/2) * separ_y

xdot = yvalues
x2_1dot = 2 * xvalues + 2 * yvalues  # x2' = 2x1 + 2x2
x2_2dot = 6 * xvalues + 2 * yvalues  # x2' = 6x1 + 2x2
phasePlane = xvalues * (yvalues + 3 * xvalues)
x2_1dot[phasePlane < 0] = np.nan  # убираем всё, что не подходит под условие первой системы
x2_2dot[phasePlane > 0] = np.nan  # убираем всё, что не подходит под условие второй системы
plt.streamplot(xvalues, yvalues, xdot, x2_1dot)
plt.streamplot(xvalues, yvalues, xdot, x2_2dot)
plt.plot(plane_x1, plane_x2, color="red", label="phase", linestyle="-")
plt.plot(separ_x_1, plane_x1, color="gray", linestyle="--", label="separ")
plt.plot(separ_x_2, plane_x1, color="gray", linestyle="--")
plt.plot([0, 0], [-10, 10], color='black', label='x2', linestyle="--")
plt.plot([-10, 10], [0, 0], color='black', label='x1', linestyle="--")
plt.axis([-10, 10, -10, 10])
plt.legend()
plt.grid()
plt.title(0)
plt.show()
print(0)
