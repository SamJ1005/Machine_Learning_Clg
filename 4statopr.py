import numpy as np

# 4(a) Generate a random 2D array and calculate the mean along each axis

rows = int(input("A\nEnter number of rows: "))
cols = int(input("Enter number of columns: "))

arr = np.random.randint(1, 100, (rows, cols))

print("\nRandom 2D Array:")
print(arr)

print("\nMean along rows (Axis = 1):")
print(np.round(np.mean(arr, axis=1),3))

print("\nMean along columns (Axis = 0):")
print(np.round(np.mean(arr, axis=0),3))


# 4(b) Find the minimum and maximum values

array = np.array(list(map(int, input("\nB\nEnter the elements: ").split())))

print("\nArray:", array)
print("Minimum Value:", np.min(array))
print("Maximum Value:", np.max(array))


# 4(c) Create a 1D array and add a constant value without using a loop

array = np.array(list(map(int, input("\nC\nEnter the elements: ").split())))

constant = int(input("Enter the constant value: "))

result = array + constant

print("\nOriginal Array:", array)
print("Updated Array:", result)


# 4(d) Multiply each row of a 2D array by a different constant

rows = int(input("\n\nD\nEnter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix elements:")

matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

A = np.array(matrix)

print("Enter", rows, "constants:")

constants = np.array(list(map(int, input().split())))

result = A * constants[:, np.newaxis]

print("\nOriginal Matrix:")
print(A)

print("\nResult after Broadcasting:")
print(result)