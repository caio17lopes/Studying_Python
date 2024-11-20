'''
Acrescentando espaços em branco em strings com tabulações ou
quebras delinha
'''
print("Languages:\nPython\nC\nJavaScript")
'''
A string "\n\t" diz a Python para passar para uma nova
linha e iniciar a próxima com uma tabulação.
'''

#Removendo espaços em branco
'''
Usando o metodo rstrip() ele remove os espaços em branco do lado direito
lstrip() do lado esquerdo , strip() dos dois lados
'''
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print (favorite_language)

favorite_language = ' python'
favorite_language = favorite_language.lstrip()
print (favorite_language)

favorite_language = ' python '
favorite_language = favorite_language.strip()
print (favorite_language)

message = "One of Python's strengths is its diverse community."
print(message)