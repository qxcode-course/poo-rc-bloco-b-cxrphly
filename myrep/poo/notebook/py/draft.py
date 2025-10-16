class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getBateria(self):
        return f"{self.__carga}/{self.__capacidade}"
    def usingBateria(self, tempo:int):
        self.__carga -= tempo
        if self.__carga < 0:
            self.__carga = 0
    def carregar(self, potencia:int , tempo:int):
        self.__carga += potencia * tempo
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    
    def temCarga(self):
        return self.__carga > 0
    

class Carregador:
    def __init__(self, potencia:int):
        self.__potencia = potencia
    def getPotencia(self):
        return self.__potencia
    
class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def ligar(self):
        if self.__bateria and self.__bateria.temCarga():
            self.__ligado = True
            print("msg: Notebook ligado")
        elif self.__carregador:
            self.__ligado = True
        else:
            print("fail: sem bateria ou carregador")

    def desligar(self):
        self.__ligado = False
        print("msg: Notebook desligado")

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria
        print("msg: Bateria conectada")

    def rmBateria(self, bateria: Bateria):
        self.__bateria = None
        print("msg: Bateria removida")
    def setCarregador(self, carregador:Carregador):
        self.__carregador = carregador
        print("msg: Carregador conectado")
    def rmCarregador(self, carregador:Carregador):
        self.__carregador = None
        print("msg: carregador desconectado")
    def usar(self, tempo: int):
        if not self.__ligado:
            print("fail: ligue o notebook primeiro")
            return
        print(f"msg: Usando por {tempo} minutos")
        if self.__bateria and self.__carregador:
            self.__bateria.carregar(self.__carregador.getPotencia(), tempo)
        elif self.__bateria:
            self.__bateria.usingBateria(tempo)
            if not self.__bateria.temCarga():
                print("bateira zeradad, notebook desligado")
                self.__ligado = False
        elif not self.__bateria or not self.__carregador():
            print("fail: sem bateria e sem carregador")
            self.__ligado = False
        if self.__bateria:
            print(self.__bateria.getBateria)

    def show(self):
        status = "ligado" if self.__ligado else "desligado"
        print(f"Notebook: {status}")
        if self.__bateria or self.__carregador:
            print(f"bateria: {self.__bateria.getBateria()}, potencia carregador: {self.__carregador.getPotencia()}")
        else:
            print("sem bateria")


""" 
def main():
    notebook:Notebook = Notebook()
    while True:
        
        line = input()
        print("$"+line)
        args:list[str] = line.split(" ")
        comando:str = args[0]

        match comando:
            case "end":
                break
 """