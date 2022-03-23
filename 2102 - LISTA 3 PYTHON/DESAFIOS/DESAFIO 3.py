'''
Verifique se um inteiro positivo n é primo.
'''
continuar = ''
while (continuar != 'N'):
    n = int(input('Insira o Número:\n'))
    contador = [n, 0]
    while (contador[0] > 0):
        contar = n % contador[0]
        if(contar == 0):
            contador[1] += 1
            contador[0] -= 1
        else:
            contador[0] -= 1
    if(contador[0] == 0):
        if(contador[1] == 2):
            print('Primo')
        else:
            print('Não é Primo')
            
    continuar = input('\nDeseja Continuar?\nAperte enter para sim\nAperte N para não\n')
    
