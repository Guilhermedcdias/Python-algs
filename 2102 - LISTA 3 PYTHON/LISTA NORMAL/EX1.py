'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

cont = ''
while(cont != 'N'):
    val = input('Insira valor entre 0 e 10:\n')
    if(isnumber(val)):
        if( int(val)<= 10 and int(val) >= 0 ):
            print('sua notaa: ', val)
            cont = input('Deseja continuar?\nenter para sim e\nN para não.\n')
        else:
            print('Tente novamente!!!')
    else:
        print('Tem que ser um numero!')
    



