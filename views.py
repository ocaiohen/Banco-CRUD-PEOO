from cliente import Cliente, Clientes
from banco import Banco, Bancos

def listar_todos_clientes():
    return Clientes.listar()
def inserir_banco(nome):
    Bancos.inserir(Banco(0, nome))
def inserir_cliente(idBanco, nome, cpf):
    Clientes.inserir(Cliente(0, idBanco, nome, cpf))
def listar_bancos():
    return Bancos.listar()
def listar_todos_clientes():
    return Clientes.listar()
def listar_clientes_banco(idBanco):
    return Bancos.listar_clientes_banco(idBanco) 