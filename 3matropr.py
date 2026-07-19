import numpy as np

# # 3(a). Extract Third Column

# print("Enter 9 elements:")
# arr = np.array(list(map(int, input().split()))).reshape(3,3)

# print("Third Column:")
# print(arr[:,2])

# # 3(b). Reverse a 1D Array

# arr = np.array(list(map(int, input("\nEnter array elements: ").split())))

# print("Reversed Array:")
# print(arr[::-1])

# # 3(c). Matrix Multiplication

# print("\nEnter 6 elements for Matrix A:")
# A = np.array(list(map(int, input().split()))).reshape(2,3)

# print("Enter 12 elements for Matrix B:")
# B = np.array(list(map(int, input().split()))).reshape(3,4)

# C = np.matmul(A,B)

# print("Result:")
# print(C)

# # 3(d). Determinant of a 3x3 Matrix

# print("\nEnter 9 elements:")
A = np.array(list(map(int, input().split()))).reshape(3,3)

print("Determinant =", np.round(np.linalg.det(A),3))