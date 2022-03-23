#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = horas = minutos = segundos = 0;
conta = [24, 60];
Continue = '';

while(True):


    if(Continue == 'N'):
        break
    else:
        dias = float(input("Insira quantos dias:"));
        horas = float(input("Insira quantas horas:"));
        minutos = float(input("Insira quantos minutos:"));
        segundos = float(input("Insira quantos segundos:"));
        conta.append((dias * conta[0] * conta[1] * conta[1]) + (horas * conta[1] * conta[1]) + (minutos * conta[1]) + segundos);
        print(conta[2]);
        Continue = input("Digite N para parar!");