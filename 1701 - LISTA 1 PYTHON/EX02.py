#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

Val = 0;
Continue = '';

while(True):

    
    if(Continue == 'N'):
        break
    else:
        Val = float(input("Insira um valor em metros:"));
        print(Val*1000);
        Continue = input("Digite N para parar!");