#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

Pmercad = 0;
Percdesc = 0;
Continue = '';

while(True):


    if(Continue == 'N'):
        break
    else:
        Pmercad = float(input("Insira o valor do produto:"));
        Percdesc = float(input("insira o percentual de desconto:"));
        print(Pmercad * (1- (Percdesc/100)));
        Continue = input("Digite N para parar!");