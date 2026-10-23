# Pedir ao usuário três itens, um após o outro. Não peça mais nem menos que três.
# Reunir os três itens em uma lista chamada lista_de_compras. Essa lista não pode conter nenhum outro item, além dos três informados.
# Exibir a lista na tela.

lista_de_compras = []
contador = 0

while contador < 3:
    lista_de_compras.append(input(f"Item {contador + 1}: "))
    contador += 1

print(lista_de_compras)
