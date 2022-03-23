'''
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
'''
import random;

lista = []
maior = 0
menor = 999
for x in range(10):
    lista.append(random.randint(1, 100))
    if(len(lista) > 0):
        if(lista[x] >= maior):
            maior = lista[x]
        if(lista[x] <= menor):
            menor = lista[x]
        
print ('Numeros: ', lista)
print ('Maior: ', maior)
print ('Menor: ', menor)