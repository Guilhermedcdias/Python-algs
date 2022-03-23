#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
#a um milhão

elev = 0;
num = 0;
Continue = 'Milhão';

while(True):
    if(Continue == 'N'):
        break
    elif(Continue == 'Milhão'):
        elev = 1000000;
        num = 2;
        conta = num ** elev
        print(
            'O numero ', conta, 'tem ', len(str(conta)), 'digitos!'
        )
        Continue = input("Digite N para parar, Milhão para saber dois elevado a um milhão \n e enter para elevar outro numero.");
    else:
        num = int(input("Insira o numero a elevar: "));
        elev = int(input("Insira elevado a quanto o numero vai ser: "));
        conta = num ** elev
        print(
            'O numero ', conta, 'tem ', len(str(conta)), 'digitos!'
        )
        Continue = input("Digite N para parar!");