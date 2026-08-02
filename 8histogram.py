import matplotlib.pyplot as plt

data = (
    [12.5] * 5 +    # Midpoint of 10-15
    [17.5] * 6 +    # Midpoint of 15-20
    [22.5] * 9 +    # Midpoint of 20-25
    [27.5] * 8 +    # Midpoint of 25-30
    [32.5] * 2      # Midpoint of 30-35
)

bins = [10, 15, 20, 25, 30, 35]

plt.hist(data, bins=bins, edgecolor="black")

plt.title("Histogram")
plt.xlabel("Class Interval")
plt.ylabel("Frequency")

plt.show()