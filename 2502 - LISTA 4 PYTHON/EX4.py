'''Seja o statement sobre diversidade: “The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement,
and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, 
and whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as 
palavras que começam ou terminam com uma das letras “python”. 
Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
'''
txt = 'Seja o statement sobre diversidade: “The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”'
div = txt.split()
aeiou = []
cont = len(div)
for x in range(cont):
    y = div[x]
    if(y[0].lower() in 'python' or y[-1].lower() in 'python'):
        aeiou.append(y)

print(aeiou)