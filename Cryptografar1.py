import random

entrada = input("Digite a mensagem que deseja criptografar: ")

nc = [caractere for caractere in entrada]
#print (nc)
c = []
numeros= []

# Defina o intervalo de números inteiros desejado
inicio = 0
fim = 100 # Substitua pelo seu intervalo desejado

# Defina o tamanho da lista
tamanho = len (nc)  # Substitua pelo tamanho desejado da lista

# Crie uma lista de números inteiros aleatórios
chave = [random.randint(inicio, fim) for _ in range(tamanho)]

#printando a chave inteira na mesma linha, sem espaços
print("chave:", end=" ")
for i in range (tamanho):
    print (chave[i], end=" ")
print()


#encripitando a mensagem com a chave
for i in range(tamanho):
    novo_codigo = ord(nc[i]) + chave[i]
    #print (chr(novo_codigo - chave[i]))

    c.append(chr(novo_codigo))
    numeros.append(novo_codigo)


#printando mensagem encriptada
print("mensagem cript:", end=" ")
for i in range (tamanho):
    print ((numeros[i]), end=" ")
print()