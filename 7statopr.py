import pandas as pd

n = int(input("Enter number of employees: "))

data = []

for i in range(n):
    salary = int(input(f"Enter salary of Employee {i+1} : "))

    data.append([salary])

df = pd.DataFrame(data, columns=["Salary"])

print("\nDataset:\n",df)

print("\nMean Salary:", df["Salary"].mean())
print("Median Salary:", df["Salary"].median())
print("Mode Salary:\n",df["Salary"].mode())
print("\nVariance:", df["Salary"].var())
print("Standard Deviation:", df["Salary"].std())