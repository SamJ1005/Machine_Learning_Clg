import matplotlib.pyplot as plt
import numpy as np

data = [3, 7, 8, 5, 12, 14, 21, 13, 18]

plt.boxplot(data)

plt.title("Box-and-Whisker Plot")
plt.ylabel("Values")
plt.yticks(np.arange(0,24,3))
plt.show()