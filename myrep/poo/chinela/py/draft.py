class Chinela:
    def __init__(self):
        self.__tamanho:int = 0
    def get_tamanho(self)->int:
        return self.__tamanho
    def set_tamanho(self, value:int)->None:
        if not value in range(20,51) or value % 2 != 0:
            print("tamanho invalido")
            return
        else:
            self.__tamanho = value

def main():
    chinela = Chinela()
    while chinela.get_tamanho()==0:
        print("Digite seu tamanho de chinela")
        tamanho = int(input())
        chinela.set_tamanho(tamanho)
    print(f"Parabens vc comprou uma de chinela de tamanho {chinela.get_tamanho()}")

main()