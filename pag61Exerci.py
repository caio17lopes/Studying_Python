# Exercicios python

nome = input('Escreva sue nome: ')
nome = nome.title()
print('Olá', nome, 'você gostaria de aprender um pouco sobre Python hoje?')
print('Olha so que legal seu nome em maiusculo e minusculo a baixo ')
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
print('Esse é seu nome maiúsculo ',nome_maiusculo, 'e esse é ele minúsculo',\
      nome_minusculo)
print('Esse é seu nome sem espaços', nome.strip(),nome.rstrip(), nome.lstrip(),\
      'e ai o que você achou?')