'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
'''


Continue = ''
n1 = 0
n2 = 0


nomes = ['Salario Bruto: R$ ', 'IR (11%) : R$ ', 'INSS (8%) : R$ ', 'Sindicato (5%) : R$ ', 'Salario Liquido : R$ ']



while(True):
    if(Continue == 'N'):
        break
    else:
        contas = []
        y = 0
        contador = 1
        n1 = int(input('Quanto você ganha por hora: '))
        n2 = int(input('Qual o numero de horas trabalhadas no mês: '))
        contas.append(n1*n2)
        contas.append(contas[0]*0.11)
        contas.append(contas[0]*0.08)
        contas.append(contas[0]*0.05)
        while(contador< len(contas)):
            y = y + contas[contador]
            contador = contador + 1
        contas.append(contas[0] - y)
        contador = 0
        while(contador< len(contas)):
            print(nomes[contador], contas[contador])
            contador = contador + 1
        Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")