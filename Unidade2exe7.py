from collections import Counter

arquivo = open('ciência_de_dados.txt', 'r')
print(Counter(arquivo.read().split()))

