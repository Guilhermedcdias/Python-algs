'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento
'''
cont = ''
while(cont != 'N'):
    pa = [0, 0, 0]
    pb = [0, 0, 0]
    anos = 0
    # POP -- PORC -- CALC/NVPOP -- ANOS
    pa[0] = float(input('Insira a População atual de A:\n'))
    pb[0] = float(input('Insira a População atual de B:\n'))
    pa[1] = float(input('Insira o Crescimento atual de A:\n'))
    pb[1] = float(input('Insira o Crescimento atual de B:\n'))
    if(pa[1] > pb[1]):
        while(pa[0] < pb[0]):
            pa[0] = pa[0] * (1 + (pa[1]/100))
            pb[0] = pb[0] * (1 + (pb[1]/100))
            anos += 1
        if(pa[0] >= pb[0]):
            print('Será necessario', anos, 'anos para População A ser maior ou igual a População B.')
            print('Em ', anos, 'anos:\n')
            print('A População A terá aproximadamente: ', int(pa[0]), 'habitantes.')
            print('A população B terá aproximadamente: ', int(pb[0]), 'habitantes.')
    else:
        print('NUNCA!')
    cont = input('Deseja continuar?\nenter para sim e\nN para não.\n')