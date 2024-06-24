import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 100)
y = 3 * x**3

plt.plot(x, y, 'b.')
plt.show()
