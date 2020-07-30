import numpy as np
import pandas as pd

x = pd.DataFrame(np.random.random((2, 3)))
y = pd.DataFrame(np.random.random((2, 3)))
#claramente vai dar erro linha.size != coluna.size
mult = np.dot(x,y)

print(mult)