s = set()
s.add(1)
s.add(2)
print(len(s))
print(2 in s)
print(3 in s)

stopwords_list = ["a", "an", "at"] + ["yet", "you"]
print("zip" in stopwords_list)

#Mais rápido em relação a localização na lista
stopwords_set = set(stopwords_list)
print("zip" in stopwords_set)
