import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 100)
z = np.linspace(0, 1, 100)
y = 2 * x**2 + 30 * z

plt.figure()
plt.plot(x, y, 'b.')