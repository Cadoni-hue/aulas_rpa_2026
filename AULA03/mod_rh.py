def cadastrar_colaborador(nome: str, cargo: str, salario: float)->dict:
    return{
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }
def exibir_colaboradores (lista_colaboradores: list) -> None:
    if not lista_colaboradores:
        print("Nenhum colaborador cadastrado.\n")
        return
    for colaborador in lista_colaboradores:
        print(f"Nome: {colaborador['nome']}, Cargo: {colaborador['cargo']}, Salário: {colaborador['salario']}")