#houses_to_rent_v2.csv
import pandas as pd
import numpy as np
from collections import Counter
#O ap que eu alugo possui 2 quartos, 1 banheiro, 70 m^2, aluguel 580, condomínio 150, total 730
#vou comparar e descobrir se pago um valor justo

dataframe = pd.read_csv('houses_to_rent_v2.csv')
print(Counter(dataframe['city']))
#nenhuma cidade pequena para tornar a comparação mais justa
# mas ainda assim é possível verificar um apartamento parecido em São Paulo

dataframe = dataframe[dataframe['area'] > 50]
dataframe = dataframe[dataframe['area'] < 100]
dataframe = dataframe[dataframe['bathroom'] == 1]
dataframe = dataframe[dataframe['rooms'] == 2]
dataframe = dataframe[dataframe['parking spaces'] == 1]
dataframe = dataframe[dataframe['animal'] == "acept"]
dataframe = dataframe[dataframe['furniture'] == "furnished"]
dataframe = dataframe[dataframe['city'] == "São Paulo"]
print(dataframe.describe())
print(dataframe['total (R$)'])

#morar em São paulo custa caro