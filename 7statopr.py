import pandas as pd

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

print("\nDataFrame:")
print(df)

print("\nMean :", df["Marks"].mean())
print("Median :", df["Marks"].median())
print("Mode :")
print(df["Marks"].mode())
print("Variance :", df["Marks"].var())
print("Standard Deviation :", df["Marks"].std())