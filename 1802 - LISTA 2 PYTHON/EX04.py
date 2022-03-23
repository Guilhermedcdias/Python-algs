#Faça um Programa que leia três números e mostre o maior deles.
from ast import If


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
        if(n1> n2> n3):
            print('Primeiro Numero é maior')
            Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")
        elif(n2> n1> n3):
            print('Segundo Numero é maior')
            Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")
        elif(n3> n1> n2):
            print('Terceiro Numero é maior')
            Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")
        else:
            print('Numeros Iguais')
            Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")