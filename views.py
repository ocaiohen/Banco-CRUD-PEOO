from cliente import Cliente, Clientes
from banco import Banco, Bancos
from conta import Conta, Contas


def inserir_banco(nome):
    Bancos.inserir(Banco(0, nome))
def inserir_cliente(idBanco, nome, cpf):
    Clientes.inserir(Cliente(0, idBanco, nome, cpf))
def inserir_conta(idBanco, idCliente):
    if idBanco != Contas.listar_id(idCliente).id:
        print("Não é possível adicionar uma conta associada a um banco em que o cliente não tem cadastro. Caso queira adicionar uma conta a esse banco, crie um novo cadastro nele e associe esse novo cadastro à nova conta.")
    else:
        Contas.inserir(Conta(0, idBanco, idCliente))
def listar_todos_clientes():
    return Clientes.listar()
def listar_todas_contas():
    return Contas.listar()
def listar_contas_cliente(idBanco, idCliente):
    return Contas.listar_contas_cliente(idBanco, idCliente)
def listar_bancos():
    return Bancos.listar()
def listar_todos_clientes():
    return Clientes.listar()
def listar_clientes_banco(idBanco):
    return Bancos.listar_clientes_banco(idBanco) 