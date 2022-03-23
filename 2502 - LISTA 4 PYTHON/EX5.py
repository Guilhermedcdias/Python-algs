'''
Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. 
Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
'''
import string;
def filtrar(text):
    punct = string.punctuation
    for c in punct:
        text = text.replace(c, "")
    return text
txt = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone. Our community is based on mutual respect,
   tolerance, and encouragement, and we are working to
   help each other live up to these principles. We want
   our community to be more diverse: whoever you are, and
   whatever your background, we welcome you.'''
divtos = filtrar(txt)
div = divtos.split()
aeiou = []
cont = len(div)
for x in range(cont):
    y = div[x]
    num = len(y)
    if(num > 4):
        letra = 0
        for z in range(num):
            if(y[z].lower() in 'python'):
                letra +=1
        if(letra > 0):
            aeiou.append(y)

print(aeiou)
print(len(aeiou))


