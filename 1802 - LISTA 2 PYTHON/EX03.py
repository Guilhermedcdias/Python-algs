#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
Continue = ''
peso = 0




while(True):
    if(Continue == 'N'):
        break
    else:
        peso = int(input('Quantos quilos de peixe você trouxe: '))
        if(peso> 50):
            print('Peso Excedente: ', (peso - 50))
            print('Multa:', 4 * (peso - 50))
            Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")

        else:
            print('Sem Multa')
            print('Peso Excedente: ', 0)
            print('Multa:', 0)
            Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")
