'''
Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator.
'''


continuar = ''

while(continuar != 'N'):
    Npos = int(input('Numero: \n'))
    for k in range(2, Npos):
        while(Npos%k == 0):
            print(k)
            Npos = Npos / k
    continuar = input('Deseja Continuar?\nenter para continuar\nN para parar\n')