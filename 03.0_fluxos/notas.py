nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"O aluno(a) {nome} foi aprovado(a) com média: {media}")
elif media >= 5:
    print(f"O aluno(a) {nome} está de exame com média: {media}")
else:
    print(f"O aluno(a) {nome} foi reprovado(a) com média: {media}")

