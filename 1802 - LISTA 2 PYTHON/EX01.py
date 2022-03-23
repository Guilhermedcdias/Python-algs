#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Continue = ''
x = 0
y = 0
z = 0


while(True):
    if(Continue == 'N'):
        break
    else:
        x = float(input('Insira o valor de um dos lados do triangulo: '))
        y = float(input('Insira o valor de um dos lados do triangulo: '))
        z = float(input('Insira o valor de um dos lados do triangulo: '))
        if(x>y+z or y>x+z or z>x+y):
            print('Não é triangulo')
            Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")

        else:
            if(x == y == z):
                print('equilatero')
                Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")
            elif(x == y and y != z):
                print('isoceles')
                Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")
            else:
                print('escaleno')
                Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")
