import json 

class Conta:
    def __init__(self, id: int, idBanco: int, idCliente: int):
        self.id = id
        self.idBanco = idBanco
        self.idCliente = idCliente
        self.saldo = 0.01
    def __str__(self):
        return f"ID da conta: {self.id}; ID do Banco: {self.idBanco}; ID do Cliente: {self.idCliente}; Saldo da conta: {self.saldo}"

class Contas:
    contas = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.contas:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.contas.append(obj)
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.contas.remove(c)
            cls.salvar()
    # @classmethod
    # def atualizar(cls, obj):
    #     b = cls.listar_id(obj.id)
    #     if b != None:
    #         b.nome = obj.nome 
    #         b.idBanco = obj.idBanco
    #         b.cpf = obj.cpf
    #         cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.contas
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.contas:
            if c.id == id: return c
        return None  
    @classmethod
    def listar_contas_cliente(cls, idBanco, idCliente):
        cls.abrir()
        contas = []
        for c in cls.contas:
            if c.idBanco == idBanco and c.idCliente == idCliente: contas.append(c)
        return contas
    @classmethod
    def salvar(cls):
        with open("contas.json", mode="w") as arquivo:   # w - write
            json.dump(cls.contas, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.contas = []
        try:
            with open("contas.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Conta(obj["id"], obj["idBanco"], obj["idCliente"])
                    cls.contas.append(c)
        except FileNotFoundError:
            pass