'''
Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321
'''


continuar = ''

while(continuar != 'N'):
    final = ''
    Npos = str(input('Numero: \n'))
    for c in range(1, len(str(Npos))+1):
        f = Npos[-c]
        final += f
    print(final)
    continuar = input('Deseja Continuar?\nenter para continuar\nN para parar\n')
