from mod_rh import cadastrar_colaborador, exibir_colaboradores
def exibir_menu():
    print("=== Sistema de Cadastro de Colaboradores ===")
    print("1. Cadastrar colaborador")
    print("2. Exibir colaboradores cadastrados")
    print("3. Sair")

def main():
    colaboradores = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do colaborador: ")
            cargo = input("Digite o cargo do colaborador: ")
            while True:
                salario = float(input("Digite o salário do colaborador: "))
                if salario < 0:
                    print("Salário inválido. Digite um valor positivo.")
                else:
                    break
            colaborador = cadastrar_colaborador(nome, cargo, salario)
            colaboradores.append(colaborador)
            print("Colaborador cadastrado com sucesso!")
        elif opcao == "2":
                exibir_colaboradores(colaboradores)
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
             print("Opção inválida. Escolha uma opção: ")
main()