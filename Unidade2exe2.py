import pandas as pd
import numpy as np

shape = (3 , 3)
matrixA = np.zeros(shape)
matrixB = np.zeros(shape)

for i in range(3):
    for j in range (3):
        matrixA[i][j] = i + j
        matrixB[i][j] = i * j

pd.DataFrame(matrixA).astype(int).to_csv('Unidade2exe2martrixA.csv')
pd.DataFrame(matrixB).astype(int).to_csv('Unidade2exe2martrixB.csv')

dataframeA = pd.read_csv('Unidade2exe2martrixA.csv')
dataframeB = pd.read_csv('Unidade2exe2martrixB.csv')

matrixALida = np.delete(dataframeA.to_numpy(),0,1)
matrixBLida = np.delete(dataframeB.to_numpy(),0,1)

sumMatrix = np.add(matrixALida, matrixBLida)
dotProductMatrix = np.dot(matrixALida, matrixBLida)


print(sumMatrix, '\n \n', dotProductMatrix, '\n \n', dataframeA, '\n \n', dataframeA.describe())