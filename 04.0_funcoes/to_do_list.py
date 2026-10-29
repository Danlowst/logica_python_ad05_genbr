from cores import *

tarefas = []

def menu():
    print("\n" + FRENTE_MAGENTA_CLARO + "_______MENU_______" + RESET)
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")

def adicionar_tarefa():
    tarefa = input("Digite o nome da tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa Adicionada!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada")
    else:
        for numero, tarefa in enumerate(tarefas, start=1):
            print(numero, "-", tarefa)

def remover_tarefa():
    listar_tarefas()

    if len(tarefas) > 0:
        numero = int(input("Digite o número da tarefa a ser removida: "))

        if 1 <= numero <= len(tarefas):
            tarefas.pop(numero - 1)
            print("Tarefa removida!")
        else:
            print("Número inválido!")

opcao = ""

while opcao != "4":
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n")
        adicionar_tarefa()
    elif opcao == "2":
        print("\n")
        listar_tarefas()
    elif opcao == "3":
        print("\n")
        remover_tarefa()
    elif opcao == "4":
        print("Até logo!")
    else:
        print("Opção inválida!")
    