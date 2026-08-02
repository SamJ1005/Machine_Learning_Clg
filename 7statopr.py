import pandas as pd

n = int(input("Enter the number of employees: "))

data = []

for i in range(n):
    print("\nEnter details of Employee", i + 1)

    empid = int(input("Employee ID : "))
    name = input("Employee Name : ")
    salary = int(input("Salary : "))

    data.append([empid, name, salary])

df = pd.DataFrame(data, columns=["Employee ID", "Employee Name", "Salary"])

print("\nDataset:\n",df)

print("\nMean Salary:", df["Salary"].mean())
print("Median Salary:", df["Salary"].median())
print("Mode Salary:\n",df["Salary"].mode())
print("Variance:", df["Salary"].var())
print("Standard Deviation:", df["Salary"].std())