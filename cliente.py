import json
class Cliente:
    def __init__(self, id: int, idBanco: int, nome: str, cpf: str):
        self.id = id
        self.idBanco = idBanco
        self.nome = nome
        self.cpf = cpf
    def __str__(self):
        return f"ID: {self.id}; ID do Banco: {self.idBanco}; Nome: {self.nome}; CPF: {self.cpf}"
class Clientes:
    clientes = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.clientes:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.clientes.append(obj)
        cls.salvar()
    @classmethod
    def clientes_banco_x(cls, idB):
        cls.abrir() #sempre tem que abrir o arquivo, estava com um problema porque tinha esquecido de abrir
        lista = []
        for c in cls.clientes:
            if c.idBanco == idB:
                lista.append(c)
                print("Achamos um cliente do banco")
        return lista
    @classmethod
    def excluir(cls, obj):
        b = cls.listar_id(obj.id)
        if b != None:
            cls.clientes.remove(b)
            cls.salvar()
    @classmethod
    def atualizar(cls, obj):
        b = cls.listar_id(obj.id)
        if b != None:
            b.nome = obj.nome 
            b.idBanco = obj.idBanco
            b.cpf = obj.cpf
            cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.clientes
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for b in cls.clientes:
            if b.id == id: return b
        return None  
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:   # w - write
            json.dump(cls.clientes, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.clientes = []
        try:
            with open("clientes.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    b = Cliente(obj["id"], obj["idBanco"], obj["nome"], obj["cpf"])
                    cls.clientes.append(b)
        except FileNotFoundError:
            pass