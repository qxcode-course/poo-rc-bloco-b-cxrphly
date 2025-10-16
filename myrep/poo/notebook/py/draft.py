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
    # def carregar?
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

    def ligar(self):
        if self.__bateria and self.__bateria.temCarga():
            self.__ligado = True
            print("msg: Notebook ligado")
        else:
            print("fail: sem bateria")

    def desligar(self):
        self.__ligado = False
        print("msg: Notebook desligado")

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria
        print("msg: Bateria conectada")

    def setBateria(self, bateria: Bateria):
        self.__bateria = None
        print("msg: Bateria removida")

    def usar(self, tempo: int):
        if not self.__ligado:
            print("fail: ligue o notebook primeiro")
            return

        if not self.__bateria or not self.__bateria.temCarga():
            print("fail: sem carga na bateria")
            self.__ligado = False
            return

        print(f"msg: Usando por {tempo} minutos")
        self.__bateria.usingBateria(tempo)
        print("bateria:", self.__bateria.getBateria())
