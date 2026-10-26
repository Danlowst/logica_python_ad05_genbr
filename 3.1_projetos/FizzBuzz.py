lista_resultado = []
for i in range(1, 1001):
    string = ""
    
    if i % 3 == 0:
        string += "FIZZ"
    if i % 5 == 0:
        string += "BUZZ"
    
    resultado = string if string else i
    print(resultado)
#     lista_resultado.append(resultado)

# print(lista_resultado)

