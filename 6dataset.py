import pandas as pd
import matplotlib.pyplot as plt

n = int(input("Enter the number of students: "))

data = []

for i in range(n):
    print("\nEnter details of Student", i + 1)

    roll = int(input("Roll No : "))
    name = input("Name : ")
    marks = int(input("Marks : "))

    data.append([roll, name, marks])

# Create DataFrame
df = pd.DataFrame(data, columns=["Roll No", "Name", "Marks"])

print("\nDataFrame:\n",df)

# Dataset Information
print("\nDataset Information:\n",df.info())

# Statistical Summary
print("\nStatistical Summary:\n",df.describe())

# Plot Marks
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()