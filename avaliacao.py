from datetime import datetime
import json
class Jogo:
    def __init__(self, id, nome, empresa, data):
        self.id = id
        self.nome = nome
        self.empresa = empresa
        self.data = data
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.empresa} - {self.data}"
    def to_json(self):
        dic = { }
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["empresa"] = self.empresa
        dic["data"] = self.data.strftime("%d/%m/%Y")
        return dic

class Jogos:
    jogos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.jogos:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.jogos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.jogos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for j in cls.jogos:
            if j.id == id: return j
        return None  
      
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.empresa = obj.empresa
            c.data = obj.data
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.jogos.remove(c)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("jogos.json", mode="w") as arquivo:   # w - write
            json.dump(cls.jogos, arquivo, default = Jogo.to_json)
    @classmethod
    def abrir(cls):
        cls.jogos = []
        try:
            with open("jogos.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    j = Jogo(obj["id"], obj["nome"], obj["empresa"], datetime.strptime(obj["data"], "%d/%m/%Y"))
                    cls.jogos.append(j)
        except FileNotFoundError:
            pass

    @classmethod
    def novos(cls):
        lista = cls.jogos[:]
        lista.sort(key=lambda j: j.data, reverse=True)
        return lista

class UI:
    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Listar Novos, 6-Sair")
        return int(input())
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
            if op == 5: UI.novos()
    @staticmethod
    def inserir():
        id = 0
        nome = input("Insira o nome do jogo: ")
        empresa = input("Insira a empresa: ")
        data = datetime.strptime(input("Insira a data de lançamento(dd/mm/aaaa): "), "%d/%m/%Y")
        j = Jogo(id, nome, empresa, data)
        Jogos.inserir(j)
    @staticmethod
    def listar(): 
        jogos = Jogos.listar()
        for j in jogos:
            print(j)
    @staticmethod
    def atualizar():
        UI.listar()
        id = int(input("Insira o ID do jogo a ser atualizado: "))
        nome = input("Insira o novo nome do jogo: ")
        empresa = input("Insira a nova empresa: ")
        data = datetime.strptime(input("Insira a nova data de lançamento(dd/mm/aaaa): "), "%d/%m/%Y")
        j = Jogo(id, nome, empresa, data)
        Jogos.atualizar(j)
    @staticmethod
    def excluir():
        UI.listar()
        id = int(input("Insira o id do jogo a ser excluido: "))
        j = Jogo(id, "", "", "")
        Jogos.excluir(j)
    @staticmethod
    def novos():
        lista = Jogos.novos()
        for j in lista:
            print(j)

UI.main()