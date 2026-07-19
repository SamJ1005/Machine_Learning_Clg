import pandas as pd

# Create a Pandas DataFrame from a list

n = int(input("Enter the number of students: "))

data = []

for i in range(n):
    print("\nEnter details of Student", i + 1)

    roll = int(input("Roll No : "))
    name = input("Name : ")
    marks = int(input("Marks : "))

    data.append([roll, name, marks])

df = pd.DataFrame(data, columns=["Roll No", "Name", "Marks"])

print("\nDataFrame:")
print(df)