import json
from cliente import Clientes

class Banco:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome
        self.lista_clientes = []
    def listar_clientes(self):
        print("Atualizando clientes")
        self.lista_clientes = Clientes.clientes_banco_x(self.id)
        return self.lista_clientes
    def __str__(self):
        return f"ID: {self.id}; Nome: {self.nome}"
class Bancos:
    bancos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.bancos:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.bancos.append(obj)
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        b = cls.listar_id(obj.id)
        if b != None:
            cls.bancos.remove(b)
            cls.salvar()
    @classmethod
    def atualizar(cls, obj):
        b = cls.listar_id(obj.id)
        if b != None:
            b.nome = obj.nome
            cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.bancos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for b in cls.bancos:
            if b.id == id: return b
        return None
    @classmethod 
    def listar_clientes_banco(cls, id):
        b = cls.listar_id(id)
        return b.listar_clientes()
    @classmethod
    def salvar(cls):
        with open("bancos.json", mode="w") as arquivo:   # w - write
            json.dump(cls.bancos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.bancos = []
        try:
            with open("bancos.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    b = Banco(obj["id"], obj["nome"])
                    cls.bancos.append(b)
        except FileNotFoundError:
            pass