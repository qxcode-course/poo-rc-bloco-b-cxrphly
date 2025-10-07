class Camisa:
    def __init__(self, size:str = ""):
        self.__size:str = ""
    def get_size(self) -> str:
        return self.__size
    def set_size(self, size:str):
        acc_sizes:list[str] = ["PP", "P", "M", "G", "GG", "XG"]
        if size not in acc_sizes:
            print("fail: tamanhos validos -> PP, P, M, G, GG e XG")
        else:
            self.__size = size

def main():
    camisa: Camisa = Camisa()
    while camisa.get_size() == "":
        print("Digie seu tamanho de roupa")
        camisa.set_size(input().upper())

    print(f"roupa tamanho {camisa.get_size()}")

main()