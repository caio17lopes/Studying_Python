# Removendo um item com o método pop()
# O método pop() remove o ultimo item da lista mas permite trabalhar com ele mesmo depois da remoção 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop() # o ultimo item da lista ficou salvo na variavel
print(motorcycles)
print(popped_motorcycles)# o print prova que o item da lista "suzuki" ainda esta salvo e disponivel 

# teste

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle i owned was a " + last_owned.title() + ".")