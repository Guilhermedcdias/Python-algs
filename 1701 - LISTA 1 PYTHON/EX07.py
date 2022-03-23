#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

celsius = 0;
Continue = '';

while(True):


    if(Continue == 'N'):
        break
    else:
        celsius = float(input("Insira a temperatura em celsius:"));
        print(((9*celsius)/(5))+32);
        Continue = input("Digite N para parar!");