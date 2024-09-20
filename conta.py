import json 

class Conta:
    def __init__(self, id: int, idBanco: int, idCliente: int, tipo: str, saldo: float):
        self.id = id
        self.idBanco = idBanco
        self.idCliente = idCliente
        self.tipo = tipo
        self.saldo = saldo
    def sacar(self, quantia : float):
        if self.saldo - quantia >= 0 and quantia > 0:
            self.saldo -= quantia
            self.arredondar_saldo()
    def depositar(self, quantia : float):
        if quantia > 0:
            self.saldo += quantia
            self.arredondar_saldo()
    def arredondar_saldo(self):
        self.saldo = round(self.saldo)
    def __str__(self):
        return f"ID da conta: {self.id}; ID do Banco: {self.idBanco}; ID do Cliente: {self.idCliente}; Tipo da conta: {self.tipo}; Saldo da conta: {self.saldo}"

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
    @classmethod
    def atualizar(cls, obj):
        b = cls.listar_id(obj.id)
        if b != None:
            b.tipo = obj.tipo
            b.idBanco = obj.idBanco
            b.idCliente = obj.idCliente
            cls.salvar()
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
                    c = Conta(obj["id"], obj["idBanco"], obj["idCliente"], obj["tipo"], obj["saldo"])
                    cls.contas.append(c)
        except FileNotFoundError:
            pass
    @classmethod
    def sacar(cls, id, quantia):
        cls.abrir()
        conta = cls.listar_id(id)
        conta.sacar(quantia)
        cls.salvar()
    @classmethod
    def depositar(cls, id, quantia):
        cls.abrir()
        conta = cls.listar_id(id)
        conta.depositar(quantia)
        cls.salvar()