#Faça um Programa que leia três números e mostre o maior e o menor deles.
Continue = ''
n1 = 0
n2 = 0
n3 = 0




while(True):
    if(Continue == 'N'):
        break
    else:
        n1 = int(input('Primeiro Numero: '))
        n2 = int(input('Segundo Numero: '))
        n3 = int(input('Terceiro Numero: '))
        if(n1> n2 and n1> n3):
            print('Primeiro Numero é maior')
        elif(n2> n1 and n2> n3):
            print('Segundo Numero é maior')
        elif(n3> n1 and n3> n2):
            print('Terceiro Numero é maior')
        elif(n1 == n2 == n3):
            print('Numeros Iguais')
        if(n1< n2 and n1< n3):
            print('Primeiro Numero é menor')
        elif(n2< n1 and n2< n3):
            print('Segundo Numero é menor')
        elif(n3< n1  and n3< n2):
            print('Terceiro Numero é menor')
        Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")