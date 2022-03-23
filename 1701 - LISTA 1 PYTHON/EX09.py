#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

dias = 0;
km = 0;
val = [60, 0.15]
Continue = '';

while(True):


    if(Continue == 'N'):
        break
    else:
        dias = float(input("Insira quantos dias o carro foi alugado:"));
        km = float(input("Insira quantos km rodados:"));
        print((dias*val[0]) + (km*val[1]))
        Continue = input("Digite N para parar!");