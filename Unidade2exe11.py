from collections import Counter
import pandas as pd
import numpy as np

arquivo = open('ciência_de_dados.txt', 'r')
dict2 = Counter(arquivo.read().split())
dataframeA = pd.DataFrame.from_dict(dict2, orient='index', columns=["Quantity"])
print(dataframeA)

