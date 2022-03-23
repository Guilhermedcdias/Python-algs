'''
Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se n é triangular.
'''
continuar = ''
while(continuar != 'N'):
    num = int(input('Insira N:'))
    cotador = num
    while(cotador >= 0):
        if((cotador) * (cotador - 1) * (cotador - 2) == num):
            print('é triangular!')
            continuar = input('Deseja Continuar? Digite N para parar!')
            break
        else:
            cotador = cotador - 1
        if(cotador == 0):
            print('Não é triangular')
            continuar = input('Deseja Continuar? Digite N para parar!')
            break
