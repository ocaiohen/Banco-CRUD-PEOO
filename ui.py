import views

class UI:
    @staticmethod
    def menu():
        print("Cadastro de Bancos")
        print("  1 - Inserir, 2 - Listar bancos, 3-Listar todos os clientes de um banco em específico 4 - Atualizar , 5 - Excluir")
        print("Cadastro de Clientes")
        print("  6 - Inserir, 7 - Listar todos, 8 - Atualizar , 9 - Excluir")
        print("Gerenciamento de contas")
        print("10- Depositar, 11- Sacar")
        print("Outras opções")
        print("  0 - Fim")

        return int(input("Insira uma opção: "))
    def main():
        op = -1
        while op != 0:
            op = UI.menu()
            if op == 1: UI.inserir_banco()
            if op == 2: UI.listar_bancos()
            if op == 3: UI.listar_clientes_banco()
            if op == 4: UI.atualizar_banco()
            if op == 5: UI.excluir_banco()
            if op == 6: UI.inserir_cliente()
            if op == 7: UI.listar_todos_clientes()
            if op == 8: UI.atualizar_cliente()
            if op == 9: UI.excluir_cliente()
            if op == 10: UI.depositar()
            if op == 11: UI.sacar()

    def inserir_banco():
        nome = input("Insira o nome do banco a ser adicionado: ")
        views.inserir_banco(nome)
    def inserir_cliente():
        UI.listar_bancos()
        idBanco = int(input("Insira o id do banco: "))
        idsBancos = UI.ids_bancos()
        if idBanco not in idsBancos:
            raise ValueError("Insira um id de banco válido!")
        nome = input("Insira o nome do cliente: ")
        cpf = input("Insira o CPF do cliente: ")
        views.inserir_cliente(idBanco, nome, cpf)
    def ids_bancos():
        bancos = views.listar_bancos()
        ids = set()
        for b in bancos:
            if b.id not in ids: ids.add(b.id)
        return ids
    def listar_bancos():
        bancos = views.listar_bancos()
        for b in bancos: print(b)
    def listar_todos_clientes():
        clientes = views.listar_todos_clientes()
        for c in clientes: print(c)
    def listar_clientes_banco():
        UI.listar_bancos()
        idBanco = int(input("Insira o id do banco: "))
        idsBancos = UI.ids_bancos()
        if idBanco not in idsBancos:
            raise ValueError("Insira um id de banco válido!")
        clientes = views.listar_clientes_banco(idBanco)
        for c in clientes:
            print(c)
        

    def atualizar_banco():
        pass
    def atualizar_cliente():
        pass
    def excluir_banco():
        pass
    def excluir_cliente():
        pass
    def sacar():
        pass
    def depositar():
        pass

UI.main()