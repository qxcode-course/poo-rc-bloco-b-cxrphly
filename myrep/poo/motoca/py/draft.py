class Pessoa:
    def __init__(self, name:str = "", age:int = 0):
        self.__age = age
        self.__name = name
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def __str__(self) -> str:
        return f"{self.__name} {self.__age}"
    
class Moto:
    def __init__(self, power:int, time:int):
        self.__pessoa: Pessoa | None = None
        self.__power: int =  power
        self.__time: int = time
        
    def insertPerson(self, person: Pessoa):
        if self.__pessoa:
            print("fail: busy motorcycle")
        else:
            self.__pessoa = person

    def removePerson(self):
        if not self.__pessoa:
            print("fail: empty motorcycle")
        else:
            aux = self.__pessoa
            self.__pessoa = None
            return print(f"{aux} removed")

    def __str__(self):
        statusPerson = f"({self.__pessoa.getName()}:{self.__pessoa.getAge()})" if self.__pessoa else "(empty)"
        return f"power:{self.__power}, time:{self.__time}, person:{statusPerson}"
    

def main():
    moto = Moto()
    while True:
        line = input()
        print("$"+line)
        arg = line.split(" ")

        if arg[0] == "end":
            break
        if arg[0] == "init":
            moto = Moto(1,0)
        elif arg[0] == "enter":
            person = Pessoa(arg[1],arg[2])
            moto.insertPerson(person)
        elif arg[0] == "leave":
            moto.removePerson()
        elif arg[0] == "show":
            print(moto)
        else:
            print("comando invalido")

main()
