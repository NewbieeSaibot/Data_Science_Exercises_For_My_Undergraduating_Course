x = 0
list = []
aux = ''
arquivo = open('arquivoExe1.txt','w')
while x < 4:
    aux = str(input())
    arquivo.write(aux + '\n')
    x = x+1
arquivo.close()
