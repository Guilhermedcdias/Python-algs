'''
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
'''

cont = ''
while(cont != 'N'):
    n = int(input('Insira N:\n'))
    fib = [1, 1]
    contador = 1
    while(contador <= n-2):
        fib.append(fib[-1] + fib[-2])
        contador += 1
    print('SEU NUM: ', fib[-1])
    print(fib)
    cont = input('Deseja continuar?\nenter para sim e\nN para não.\n')