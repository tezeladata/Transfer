import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0, np.pi*6, 0.1)
amplitude = np.sin(data)

data2 = np.arange(0, np.pi*6, 0.1)
amplitude2 = np.cos(data2)

plt.plot(data, amplitude, label="Sinusoidal")
plt.plot(data2, amplitude2, label="Cosinusoidal")
plt.legend()
plt.grid(True)
plt.xlabel("Value")
plt.ylabel("Amplitude")
plt.show()