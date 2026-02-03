import numpy as np

# Input 5x3 matrix
print("Enter elements for 5x3 matrix:")
matrix1 = []
for i in range(5):
    row = list(map(int, input(f"Enter 3 elements for row {i+1}: ").split()))
    matrix1.append(row)

print("\nEnter elements for 3x2 matrix:")
matrix2 = []
for i in range(3):
    row = list(map(int, input(f"Enter 2 elements for row {i+1}: ").split()))
    matrix2.append(row)

A = np.array(matrix1)
B = np.array(matrix2)

product = np.dot(A, B)

print("\n5x3 Matrix:")
print(A)

print("\n3x2 Matrix:")
print(B)

print("\nProduct Matrix (5x2):")
print(product)
