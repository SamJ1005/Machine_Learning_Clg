import numpy as np

# 1(a). Create a 1D array with elements from 0 to 9

arr = np.arange(10)
print(arr)

# 1(b). Create a 2D array (3x4) with random numbers

arr = np.random.rand(3,4)
print(arr)

# 1(c). Calculate Mean and Standard Deviation

arr = np.array(list(map(int, input("Enter array elements: ").split())))

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# 1(d). Normalize the Array

arr = np.array(list(map(int, input("Enter array elements: ").split())))

mean = np.mean(arr)
std = np.std(arr)

normal = (arr - mean) / std

print("Normalized Array:", normal)