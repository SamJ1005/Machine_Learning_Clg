import numpy as np

# 2(a). Create 10 evenly spaced values between 0 and 1

arr = np.linspace(0,1,10)
print(arr)

# 2(b). Generate a 3x3 Identity Matrix

arr = np.eye(3)
print(arr)

# 2(c). Reshape a 1D array into (2x5)

arr = np.array(list(map(int, input("Enter 10 elements: ").split())))

arr = arr.reshape(2,5)
print(arr)

# 2(d). Stack Two Arrays

a = np.array(list(map(int, input("Enter first array (3 elements): ").split())))
b = np.array(list(map(int, input("Enter second array (3 elements): ").split())))

print("Vertical Stack")
print(np.vstack((a,b)))

print("Horizontal Stack")
print(np.hstack((a,b)))