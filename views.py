from cliente import Cliente, Clientes
from banco import Banco, Bancos
from conta import Conta, Contas


def inserir_banco(nome):
    Bancos.inserir(Banco(0, nome))
def inserir_cliente(idBanco, nome, cpf):
    Clientes.inserir(Cliente(0, idBanco, nome, cpf))
def inserir_conta(idBanco, idCliente, tipo):
    cliente = Clientes.listar_id(idCliente)
    if cliente is None:
        print(f"Cliente com ID {idCliente} não encontrado.")
    else:
        if idBanco != cliente.id:
            print("Não é possível adicionar uma conta associada a um banco em que o cliente não tem cadastro.")
        else:
            Contas.inserir(Conta(0, idBanco, idCliente, tipo, 0.01))
def listar_todos_clientes():
    return Clientes.listar()
def listar_todas_contas():
    return Contas.listar()
def listar_contas_cliente(idBanco, idCliente):
    return Contas.listar_contas_cliente(idBanco, idCliente)
def listar_bancos():
    return Bancos.listar()
def listar_clientes_banco(idBanco):
    return Bancos.listar_clientes_banco(idBanco) 
def atualizar_banco(idBanco, novoNome):
    novoObj = Banco(idBanco, novoNome)
    Bancos.atualizar(novoObj)
def atualizar_cliente(idCliente, novoNome, novoCPF):
    obj = Clientes.listar_id(idCliente)
    novoObj = Cliente(idCliente, obj.idBanco, novoNome, novoCPF)
    Clientes.atualizar(novoObj)
def atualizar_conta(idConta, idBanco, idCliente, tipo):
    obj = Contas.listar_id(idConta)
    novoObj = Conta(obj.id, idBanco, idCliente, tipo, obj.saldo)
    Contas.atualizar(novoObj)
def excluir_banco(id):
    obj = Bancos.listar_id(id)
    Bancos.excluir(obj)
def excluir_cliente(id):
    obj = Clientes.listar_id(id)
    Clientes.excluir(obj)
def excluir_conta(id):
    obj = Contas.listar_id(id)
    Contas.excluir(obj)
def sacar(idConta, quantia):
    if quantia > 0:
        Contas.sacar(idConta, quantia)
def depositar(idConta, quantia):
    if quantia > 0:
        Contas.depositar(idConta, quantia)

