from control.matlab import tf, feedback, minreal, step, lsim
import math
import matplotlib.pyplot as plt
import numpy as np

z = tf('z')

tp = 1
W_dis = (z + 3.82) / ((z - 1.0) * (z - 0.56))
R_dis = ((z - 0.56) * (33650/58081 * z - 21600/58081)) / ((z + 82512/58081) * (z - 1))

Wyg = minreal(feedback(W_dis * R_dis, 1, -1))
Weg = minreal(feedback(1, W_dis * R_dis, -1))
print(Wyg)
print(Weg)
# Установившаяся ошибка при воздействии g[lT] = (lT)^2 + 2lT + 1
t = np.arange(0, 1.1, 0.1)
g1 = (t * t) + (2 * t) + 1

response = lsim(Wyg, g1, t)
yout = response[0]
time = response[1]
plt.step(time, yout, 'y', time, g1, 'm')
print('Steady-state error: %.4f'% math.fabs(yout[-1] - g1[-1]))
plt.xlabel('t')
plt.ylabel('y')
plt.title('Yellow - output, purple - input.  Steady-state error: %.4f'% math.fabs(yout[-1] - g1[-1]))
plt.show()


# h[lT] при воздействии g[LT] = 1
h, t_step = step(Wyg, t)
plt.step(t_step, h, 'g')
plt.xlabel('t')
plt.ylabel('h step')
plt.title('h[lT], g[lT] = 1')
plt.show()


# e[lT] при воздействии g[lT] = (lT)^2 + 2lT + 1
g2 = (t * t) + (2 * t) + 1
error = lsim(Weg, g2, t)
error_yout = error[0]
error_time = error[1]
plt.step(error_time, error_yout, 'red')
plt.xlabel('t')
plt.ylabel('e[lT]')
plt.title('e[lT], g[lT] = (lT)^2 + 2lT + 1')
plt.show()