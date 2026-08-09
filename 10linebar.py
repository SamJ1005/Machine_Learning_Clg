import matplotlib.pyplot as plt

elapsed_time = [0, 1, 2, 3, 4, 5, 6]
speed = [0, 3, 7, 12, 20, 30, 45.6]

# Line Plot
plt.plot(elapsed_time, speed, marker='o')
plt.title("Line Plot: Speed vs Elapsed Time")
plt.xlabel("Elapsed time (s)")
plt.ylabel("Speed (m/s)")
plt.grid(True)
plt.show()

# Bar Chart
plt.bar(elapsed_time, speed)
plt.title("Bar Chart: Speed vs Elapsed Time")
plt.xlabel("Elapsed time (s)")
plt.ylabel("Speed (m/s)")
plt.show()