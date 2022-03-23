#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.

anos = 0;
cigarros = 0;
val = [10]
Continue = '';

while(True):
    if(Continue == 'N'):
        break
    else:
        anos = float(input("Insira quantos anos fumados:"));
        cigarros = float(input("Insira quantos cigarros por dia:"));
        print(
            ((anos* 365 * cigarros * val[0])/60)/24 )
        Continue = input("Digite N para parar!");