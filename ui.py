import views

class UI:
    @staticmethod
    def menu():
        print("Cadastro de Bancos")
        print("  1 - Inserir, 2 - Listar bancos, 3-Listar todos os clientes de um banco em específico 4 - Atualizar , 5 - Excluir")
        print("Cadastro de Clientes")
        print("  6 - Inserir, 7 - Listar todos, 8 - Atualizar , 9 - Excluir")
        print("Gerenciamento de contas")
        print("10-Inserir conta, 11- Listar todas as contas, 12- Listar contas do cliente, 13- Atualizar conta, 14- Excluir conta, 15- Depositar, 16- Sacar")
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
            if op == 10: UI.inserir_conta()
            if op == 11: UI.listar_todas_contas()
            if op == 12: UI.listar_contas_cliente()
            if op == 13: UI.atualizar_conta()
            if op == 14: UI.excluir_conta()
            if op == 15: UI.depositar()
            if op == 16: UI.sacar()

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
    def inserir_conta():
        UI.listar_bancos()
        idBanco = int(input("Insira o id do banco associado à conta: "))
        UI.listar_todos_clientes()
        idCliente = int(input("Insira o id do cliente associado à conta: "))
        tipo = input("Insira o tipo da conta: ")
        views.inserir_conta(idBanco, idCliente, tipo)
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
    def listar_todas_contas():
        contas = views.listar_todas_contas()
        for c in contas: print(c)
    def listar_contas_cliente(): 
        UI.listar_bancos()
        idBanco = int(input("Insira o id do banco associado à conta: "))
        UI.listar_todos_clientes()
        idCliente = int(input("Insira o id do cliente associado à conta: "))
        contas = views.listar_contas_cliente(idBanco, idCliente)
        for c in contas: print(c)
    def atualizar_banco():
        UI.listar_bancos()
        idBanco = int(input("Insira o id do banco a ser atualizado: "))
        novoNome = input("Insira o novo nome do banco: ")
        views.atualizar_banco(idBanco, novoNome)
    def atualizar_cliente():
        UI.listar_todos_clientes()
        idCliente = int(input("Insira o id do cliente a ter informações atualizadas: "))
        novoNome = input("Insira o novo nome do cliente: ")
        novoCPF = input("Insira o novo CPF do cliente: ")
        views.atualizar_cliente(idCliente, novoNome, novoCPF)
    def atualizar_conta():
        UI.listar_contas_cliente()
        idConta = int(input("Insira o id da conta a ser atualizada: "))
        idBanco = int(input("Insira o novo id do banco: "))
        idCliente = int(input("Insira o novo id do cliente: "))
        tipo = input("Insira o novo tipo da conta: ")
        views.atualizar_conta(idConta, idBanco, idCliente, tipo)
    def excluir_banco():
        UI.listar_bancos()
        idBanco = int(input("Insira o id do banco a ser excluído: "))
        views.excluir_banco(idBanco)
    def excluir_cliente():
        UI.listar_todos_clientes()
        idCliente = int(input("Insira o id do cliente a ser excluído: "))
        views.excluir_cliente(idCliente)
    def excluir_conta():
        UI.listar_contas_cliente()
        idConta = int(input("Insira o id da conta a ser excluída: "))
        views.excluir_conta(idConta)
    def sacar():
        UI.listar_contas_cliente()
        idConta = int(input("Insira o id da conta: "))
        quantia = float(input("Insira a quantia a ser sacada: "))
        if quantia > 0:
            views.sacar(idConta, quantia)
        else: print("Quantia deve ser maior que zero!")
    def depositar():
        UI.listar_contas_cliente()
        idConta = int(input("Insira o id da conta: "))
        quantia = float(input("Insira a quantia a ser depositada: "))
        if quantia > 0:
            views.depositar(idConta, quantia)
        else: print("Quantia deve ser maior que zero!")

UI.main()