num = []
resultado = []
contador = 0
while True:
    try:
        entrada = (int(input("Digite um número: ")))
        num.append(entrada)
    except ValueError:
        break


# for i in range(contador):
#     if num[i] % 3 == 0:
#         print("FizzBuzz" if num[i] % 5 == 0 else "Fizz")
#     elif num[i] % 5 == 0:
#         print("Buzz")
#     else:
#         print(num[i])

for i in range(len(num)):
    if num[i] % 3 == 0:
        if num[i] % 5 == 0:
            resultado.append("FizzBuzz")
        else:
            resultado.append("Fizz")
    elif num[i] % 5 == 0:
        resultado.append("Buzz")
    else:
        resultado.append(num[i])

# print(resultado)

saida = ", ".join(map(str, resultado))
print(saida)
