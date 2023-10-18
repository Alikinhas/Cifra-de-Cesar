c = [int(i) for i in input("A mensagem encriptada: ").split()]
#print (c)
tamanho = len (c)
#print (tamanho)
nc = []

chave = [int(i) for i in input("Digite a chave de acesso: ").split()]
#print (chave)

for i in range (tamanho):
    nc.append (c[i] - chave[i])


for i in range (tamanho):
    print (chr(nc[i]), end="")

