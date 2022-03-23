'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
'''
Continue = ''
n1 = 0





while(True):
    if(Continue == 'N'):
        break
    else:
        contas = []
        y = 80
        x = 18
        contador = 1
        n1 = int(input('Insira quantos metros quadrados tem o local a ser pintado: '))
        contas.append(n1/3)      
        while(contas[0] > x):
            contador = contador + 1
            x = 18 *contador
        if(contas[0] <= x):
            print("Você vai precisar de ", (x/18), "latas de tinta para pintar!")
            print("Para pintar você gastará: R$ ", ((x/18)*80), "reais")
        Continue = input("Deseja continuar? Digite N para parar ou aoperte enter para continuar.")