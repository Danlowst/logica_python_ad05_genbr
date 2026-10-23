lista = [
    "Gabriel",
    "Vinicius",
    "Jussara",
    "Priscila",
    "Maurício",
    "Josiane",
    "Diogo"
]

print(lista)

print(lista[3])

# Inserindo dados na lista
lista.append(input("Digite um nome: "))
lista += ["Daniel", "Lucas", "Thulio"]

print(lista)

# Para apagar um nome da lista pelo indice
lista.pop(1)
print(lista)

# Para apagar um nome pelo valor
lista.remove("Gabriel")
print(lista)