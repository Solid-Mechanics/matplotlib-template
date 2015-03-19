"""
Simple demo with line plots.
"""
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.exp(-x1)


fig = plt.figure(figsize=(10, 7.5))
ax = fig.add_subplot(111)
ax.plot(x1, y1, 'ko-',x1, y2, 'b^-', markersize=9,fillstyle='none',markeredgewidth=1,linewidth = 1)
plt.legend(('Model length', 'Data length'), 'lower right', shadow=False)
ax.set_xlim(0, 5)
ax.set_ylim(-1, 1)
plt.title('A tale of 2 subplots')
plt.xlabel('time (s)')
plt.ylabel('Stress $\sigma$')
plt.grid(False)
plt.show()