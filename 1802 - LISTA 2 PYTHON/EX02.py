#Determine se um ano é bissexto. Verifique no Google como fazer isso...
Continue = ''
x = 0



while(True):
    if(Continue == 'N'):
        break
    else:
        x = int(input('Qual ano você quer saber se é bissexto: '))
        if(x%4 == 0):
            print('O ano ', x, 'é bissexto')
            Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")

        else:
            print('O ano ', x, 'não é bissexto')
            Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")
