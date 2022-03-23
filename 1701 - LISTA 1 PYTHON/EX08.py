#Faça agora o contrário, de Fahrenheit para Celsius.

fah = 0;
Continue = '';

while(True):


    if(Continue == 'N'):
        break
    else:
        fah = float(input("Insira a temperatura em Fahrenheit:"));
        print(((fah -32)*5)/9)
        Continue = input("Digite N para parar!");