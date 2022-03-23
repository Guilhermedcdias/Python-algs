# Faça um programa que peça dois números inteiros e imprima a soma desses dois números.

X = 0;
Y = 0;
Continue = '';

while(True):

    

    if(Continue == 'N'):
        break
    else:
        X=float(input("Insira um número:"));
        Y=float(input("insira outro número:"));
        print(X + Y);
        Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")
