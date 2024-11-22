motorcycles =['honda', 'yamaha', 'suzuki', 'ducatti']
print(motorcycles)
motorcycles.remove('ducatti') # Aqui passei a instrução de remover um iten da lista que sei que ele esta lá 
print(motorcycles)

# Outro exemplo
motorcycles =['honda', 'yamaha', 'suzuki', 'ducatti']
print(motorcycles)
too_expansive = 'ducatti'
motorcycles.remove(too_expansive)
print(motorcycles)
print("A " +too_expansive.title() + " is too expansive for me.")
# Aqui foi criado um motivo para remover ela , apesar de ter removido ela , ela esta salvo na variavel too_expansive
# se eu colocar print (too_expansive) vai aparecer ela salva lá 
#### NOTA!!!!!
# O método remove() apaga apenas a primeira ocorrência do valor que eu especificar. Se ele aparecer masi de uma vez na lista
# será necessário usar um laço para determinar todas as ocorrências
