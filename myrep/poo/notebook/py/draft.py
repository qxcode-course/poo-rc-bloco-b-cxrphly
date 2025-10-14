class Bateria:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__carga = capacidade
    
class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria = Bateria | None = None
    def ligar(self):
        self.__ligado = True
        print("msg: notebook ligado")

    def desligar(self):
        self.__ligado = False
        print("msg: notebook desligado")

    def usar(self, tempo: int):
        if self.__ligado:
            print(f"msg: Usando por {tempo} minutos")
        else:
            print("msg: Ligue o notebook primeiro")

    def isLigado(self):
        if self.__ligado:
            print("status: ligado")
            return True
        else:
            print("status: desligado")
            return False

def main():
    notebook = Notebook()
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            notebook.isLigado()
        elif args[0] == "usar":
            notebook.usar(int(args[1]))
        elif args[0] == "desligar":
            notebook.desligar()
        elif args[0] == "ligar":
            notebook.ligar()
        else:
            print("invalido")
main()
