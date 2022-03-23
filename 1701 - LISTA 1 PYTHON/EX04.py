#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a 
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

Salario = 0;
Pa = 0;
Continue = '';

while(True):

    
    if(Continue == 'N'):
        break

    else:       
        Salario = float(input("Insira o salário:"));
        Pa = float(input("insira o percentual de aumento:"));
        print((Salario * (1 + (Pa/100))))
        Continue = input("Digite N para parar!");