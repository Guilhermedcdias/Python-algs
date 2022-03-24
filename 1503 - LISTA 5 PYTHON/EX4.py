'''Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995'''

numl = []
nums = []
for u in range(18644, 33088):
    numl.append(u)
for z in range(len(numl)):
    y = numl[z]
    tem = 0
    cancela = 0
    print(y)
    if (y == 2):
        tem = tem + 1
    if (y == 7):
        cancela = cancela + 1
    if (cancela > 0):
        tem = 0
        cancela = 0
    else:
        nums.append(y)
print(len(nums))

