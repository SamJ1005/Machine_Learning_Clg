#-----Program 1-----
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [i**2 for i in x]

plt.plot(x, y)
plt.title("y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#-----Program 2-----
import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.rand(10)
y1 = np.random.rand(10)

x2 = np.random.rand(10)
y2 = np.random.rand(10)

plt.scatter(x1, y1, color="red", label="Data 1")
plt.scatter(x2, y2, color="blue", label="Data 2")

plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

#-----Program 3-----
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)

plt.hist(data, bins=20)

plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

#-----Program 4-----
import matplotlib.pyplot as plt

products = ["A", "B", "C", "D"]
sales = [120, 200, 150, 100]

plt.bar(products, sales)

plt.title("Sales of Products")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

#-----Program 5-----
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Sine Wave")

plt.subplot(1, 2, 2)
plt.scatter(np.random.rand(20), np.random.rand(20))
plt.title("Random Scatter")

plt.tight_layout()
plt.show()

#-----Program 6-----
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("Customized Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.show()

#-----Program 7-----
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)

plt.boxplot(data)

plt.title("Box Plot")
plt.show()

#-----Program 8-----
import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
sizes = [30, 25, 20, 25]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")

plt.title("Pie Chart")
plt.show()

#-----Program 9-----
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

ax.plot_surface(X, Y, Z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

#-----Program 10-----
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 18, 20]
error = [1, 2, 1, 2, 1]

plt.errorbar(x, y, yerr=error, fmt='o-', capsize=5)

plt.title("Error Bar Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()