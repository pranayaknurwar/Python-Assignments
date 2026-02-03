import numpy as np

matrix1 = np.random.randint(1, 10, size=(3, 3))
matrix2 = np.random.randint(1, 10, size=(3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)
