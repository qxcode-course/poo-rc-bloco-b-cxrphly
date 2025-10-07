class Camisa:
    def __init__(self):
        self.__size:str = ""
    def get_size(self) -> str:
        return self.__size
    def set_size(self, size:str):
        acc_sizes:list[str] = ["PP", "P", "M", "G", "GG", "XG"]
        if size not in acc_sizes:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
        else:
            self.__size = size
    def __str__(self) -> str:
        return f"size: ({self.__size})"
# por algum motivo nao consegui realizar o TEST_CASE do tko
def main():
    camisa: Camisa = Camisa()
    while True:
        line: str = input()
        arg : list[str] = line.split(" ")
        print("$"+line)
        if arg[0] == "end":
            break
        elif arg[0] == "size":
            camisa.set_size(arg[1])
        elif arg[0] == "show":
            print(camisa)
        else:
            print("comando invalido")

main()