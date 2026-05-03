import numpy as np

# Input matrices
print("Enter Array1:")
arr1 = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Array2:")
arr2 = np.array([list(map(int, input().split())) for i in range(3)])

a=np.hstack((arr1, arr2))
print("Horizontal Stack:")
print(a)
b=np.vstack((arr1, arr2))
print("Vertical Stack:")
print(b)
