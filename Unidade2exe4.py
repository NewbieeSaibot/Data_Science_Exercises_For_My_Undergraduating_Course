import numpy as np

matrix = np.random.random((3, 3))
matrixB = np.random.random((3, 3))

np.save('Unidade2exe4matrix', matrix)
matrixB = np.load("Unidade2exe4matrix.npy")

print(matrix, '\n \n',  matrixB)


