'''
title() exibe cada palavra com uma letra maiúscula no início. Isso é
útil, pois, muitas vezes, você vai querer pensar em um nome como uma
informação.
'''
name = 'ada lovelace'
print(name.title())
'''
Vários outros métodos úteis estão disponíveis para tratar letras
maiúsculas e minúsculas também. Por exemplo, você pode mudar uma
string para que tenha somente letras maiúsculas ou somente letras
minúsculas, assim: name = "Ada Lovelace"
.upper() deixa todo o nome em maiusculo
.lower( deixa todo o nome em minusculo)
'''

print(name.upper())
print (name.lower())

'''
Combinando ou concatenando strings
'''
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)
print('Olá,' +full_name.title() + '!')
mesage = full_name.title() + '!' # com esse metodo ja salvo a variavel de 
# forma formatada sem precisar ficar editando no print()

