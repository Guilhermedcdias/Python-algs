#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem.

velmed = 0;
distperc = 0;
Continue = '';

while(True):


    if(Continue == 'N'):
        break
    else:
        velmed = float(input("Insira o valor da velocidade media:"));
        distperc = float(input("insira a distancia a percorrer em km:"));
        print(distperc/velmed);
        Continue = input("Digite N para parar!");