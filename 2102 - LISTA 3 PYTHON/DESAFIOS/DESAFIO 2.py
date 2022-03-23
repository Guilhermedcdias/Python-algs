'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.
'''
continuar = ''
while(continuar != 'N'):
    notas = [0, 0, 0, 0, 0, 0]
    corresp = ['50', '20', '10', '5', '2', '1']
    conta = int(input('Insira o valor da conta a ser paga: '))
    pago =  int(input('Insira a quantia de dinheiro recebida: '))
    troco =  pago - conta
    if(troco>0):
        while(troco>=50):
            troco -= 50 
            notas[0] += 1
        while(troco < 50 and troco >= 20):
            troco -= 20
            notas[1] += 1
        while(troco < 20 and troco >= 10):
            troco -= 10
            notas[2] += 1
        while(troco < 10 and troco >= 5):
            troco -= 5
            notas[3] += 1
        while(troco < 5 and troco >= 2):
            troco -= 2
            notas[4] += 1
        while(troco < 2 and troco >= 1):
            troco -= 1
            notas[5] += 1
    if(troco == 0):
        print('\nVocê dará de troco:')
        for i in range(6):
            print(notas[i], ' notas de ', corresp[i])
    elif (troco == 0):
        print(troco)
        print('Não há troco!')
    elif(troco < 0):
        print('Faltam R$ ', troco *(-1))

    continuar = input('\nDeseja Continuar?\nSe Sim aperte enter\nSe Não aperte N.\n')
