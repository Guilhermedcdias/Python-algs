'''
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
'''
import random;

lista = []
par = []
impar = []
for x in range(10):
    lista.append(random.randint(1, 100))
    if(len(lista) > 0):
        if(lista[x] %2 == 0):
            par.append(lista[x])
        else:
            impar.append(lista[x])
        
print ('Numeros: ', lista)
print ('Par: ', par)
print ('Impar: ', impar)