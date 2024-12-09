countrys = [
    "Brasil", "Argentina", "Canadá", "França", "Alemanha", "Itália", "Japão", "Austrália", "China", "India",
    "México", "Espanha", "Reino Unido", "Estados Unidos", "Rússia", "Egito", "Nigéria", "Indonésia",
    "Coreia do Sul"
]

# Convertendo para letras minúsculas
countrys_lower = [country.lower() for country in countrys]

# Exibindo a lista original em minúsculas
print("Países em letras minúsculas:", countrys_lower)

# Exibindo a lista em ordem alfabética
print("Países em ordem alfabética:", sorted(countrys_lower))

# Contagem de paises
print("A quantidade de paises na lista é de", len(countrys_lower), "no total")

# Invertendo  a lista 
countrys_lower.sort(reverse=True)
print(countrys_lower)