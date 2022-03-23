'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

cont = ''
while(cont != 'N'):
    user = input('Insira o nome de usuario:\n')
    password = input('Insira a senha:\n')
    if (user != password):
        print('Parabens!!')
    else:
        print('Tente novamente!!!')
    cont = input('enter para continuar\nN para parar!\n\n')