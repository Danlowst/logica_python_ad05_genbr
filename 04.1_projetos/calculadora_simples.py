# Variaveis

num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
print("Operadores válidos: + , - , * , /")
operador = input("Digite um operador válido: ")
resultado = 0.0

if operador == "+":
    resultado = num1 + num2
    print(resultado)
elif operador == "-":
    resultado = num1 - num2
    print(resultado)
elif operador == "*":
    resultado = num1 * num2
    print(resultado)
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(resultado)
    else:
        print("Não é possível dividir por zero")
else:
    print("Operador inválido")