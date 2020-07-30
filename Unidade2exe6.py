import numpy as np
import pandas as pd

i = 0
while i < 5:
    dataframeX = pd.read_csv('ex6.csv', skiprows=2000*i,nrows=2000)
    dataframeX.to_csv('Unidade2exe6csv' + str(i))
    i = i + 1
