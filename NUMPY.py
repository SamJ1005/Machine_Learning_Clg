# 1
# import numpy as np

# arr = np.arange(10)
# print(arr)

# 2
# import numpy as np

# arr = np.random.rand(3, 4)
# print(arr)

# 3
# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])

# print("Mean:", np.mean(arr))
# print("Standard Deviation:", np.std(arr))

# 4
# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])

# mean = np.mean(arr)
# std = np.std(arr)

# normalized = (arr - mean) / std
# print(normalized)

# 5
# import numpy as np

# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])

# print(arr[:, 2])

# 6
# import numpy as np

# arr = np.array([1,2,3,4,5])

# print(arr[::-1])

# 7
# import numpy as np

# A = np.array([[1,2,3],
#               [4,5,6]])

# B = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12]])

# C = np.matmul(A, B)

# print(C)

# 8
# import numpy as np

# A = np.array([[1,2,3],
#               [0,1,4],
#               [5,6,0]])

# print(np.linalg.det(A))

# 9
# import numpy as np

# arr = np.linspace(0, 1, 10)

# print(arr)

# 10
# import numpy as np

# I = np.eye(3)

# print(I)

# 11
# import numpy as np

# arr = np.arange(10)

# new_arr = arr.reshape(2,5)

# print(new_arr)

# 12
# import numpy as np

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print("Vertical Stack")
# print(np.vstack((a,b)))

# print("Horizontal Stack")
# print(np.hstack((a,b)))

# 13
# import numpy as np

# arr = np.random.rand(10)

# print(arr[arr > 0.5])

# 14
# import numpy as np

# arr = np.array([2,-3,4,-5,6])

# arr[arr < 0] = 0

# print(arr)

# 15
# import numpy as np

# arr = np.random.rand(3,4)

# print("Mean of rows:", np.mean(arr, axis=1))
# print("Mean of columns:", np.mean(arr, axis=0))

# 16
# import numpy as np

# arr = np.array([5,10,15,20,25])

# print("Minimum:", np.min(arr))
# print("Maximum:", np.max(arr))

# 17
# import numpy as np

# arr = np.array([1,2,3,4,5])

# result = arr + 10

# print(result)

# 18
# import numpy as np

# arr = np.array([[1,2],
#                 [3,4],
#                 [5,6]])

# constants = np.array([2,3,4])

# result = arr * constants[:, np.newaxis]

# print(result)

# 19
# import numpy as np

# def square(x):
#     return x * x

# arr = np.array([1,2,3,4,5])

# result = square(arr)

# print(result)

# 20
import numpy as np

A = np.array([[1,1],
              [2,3]])

B = np.array([5,12])

X = np.linalg.solve(A, B)

print("Solution:", X)