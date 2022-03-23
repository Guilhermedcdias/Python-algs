'''
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 
Imprima os três vetores.
'''
import random;

lista = []
lista2 = []
inter = []
for x in range(10):
    lista.append(random.randint(1, 100))
for y in range(10):
    lista2.append(random.randint(1, 100))

for z in range(10):
    inter.append(lista[z])
    inter.append(lista2[z])

print('L1: ', lista)
print('L2: ', lista2)
print('Intercalado: ', inter)