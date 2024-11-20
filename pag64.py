#Evitando erros detipo comafunção str()

age = 28
#message = 'Happy' + age +'rd birthday' esta comentado porque gera erro
'''
Python vê que você está usando uma
variável em cujo valor é um inteiro (int), mas não tem certeza de como
interpretar esse valor. O interpretador sabe que a variável poderia
representar um valor numérico 23 ou os caracteres 2 e 3. Quando usar
inteiros em strings desse modo, você precisará especificar explicitamente
que quer que Python utilize o inteiro como uma string de caracteres.
Podemos fazer isso envolvendo a variável com a função str();
'''
message = 'Happy ' + str(age) +'rd birthday'
print(message)

# Inteiros em Python
'''
Python devolve um resultado um pouco diferente quando dividimos
dois inteiros:
 3 / 2 = 1
Em vez de 1.5, Python devolve 1. A divisão de inteiros em Python 2
resulta em um inteiro com o resto truncado. Observe que o resultado
não é um inteiro arredondado; o resto é simplesmente omitido.

Para evitar esse comportamento em Python , certifique-se de que pelo
menos um dos números seja um número de ponto flutuante. Ao fazer
isso, o resultado também será um número de ponto flutuante:
'''
inteiro = 3.0/2
print(inteiro)
inteiro_2 = 3./2.0
print(inteiro_2)
inteiro_3 = 3.0 /2.0
print(inteiro_3)
