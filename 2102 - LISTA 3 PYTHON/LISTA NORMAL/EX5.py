'''
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides.
'''
def euclides(a, b):
    conta = [a, b]
    while(conta[-1] != 0):
        conta.append(conta[-2] % conta[-1])
    return conta[-2]
cont = ''
while(cont != 'N'):
    a = int(input('Insira Numero A:\n'))
    b = int(input('Insira Numero B:\n'))
    print(euclides(a, b),' é o maior divisor comum!\n')

    cont = input('Deseja continuar?\nenter para sim e\nN para não.\n')