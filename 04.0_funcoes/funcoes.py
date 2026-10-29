# Função sem retorno e sem parâmetro
def sobre():
    print("Desenvolvido por: Daniel Marques")

# Função sem retorno e com parâmetros
def turma(turma, ano):
    print(f"Turma: {turma} - {ano}")

# Função com retorno e com parâmetro
def somar(num1, num2):
    return num1 + num2

sobre()
turma("AD-05", 2026)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segunfo número: "))

resultado = somar(num1, num2)
print(f"A soma de {num1} + {num2} = {resultado}")