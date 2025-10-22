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
    def __init__(self, power:int=1, time:int=0):
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
            print(f"{self.__pessoa.getName()}:{self.__pessoa.getAge()}")
            self.__pessoa = None
    def buyTime(self, amount:int):
        self.__time += amount
        return
    def driveMotoca(self, distance:int ):
        if self.__time == 0:
            print("fail: buy time first")
            return
        elif not self.__pessoa:
            print("fail: empty motorcycle")
            return
        elif self.__pessoa.getAge() > 10:
            print("fail: too old to drive")
            return
        else:
            aux_time = self.__time
            self.__time -= distance
            if self.__time <= 0:
                print(f"fail: time finished after {aux_time} minutes")
                self.__time = 0

    def honk(self):
        honk = ['P','','m']
        for i in range(self.__power):
            honk.insert(1,"e")
        print("".join(honk))

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
            moto = Moto(int(arg[1]))
        elif arg[0] == "enter":
            person = Pessoa(arg[1],int(arg[2]))
            moto.insertPerson(person)
        elif arg[0] == "leave":
            moto.removePerson()
        elif arg[0] == "show":
            print(moto)
        elif arg[0] == "buy":
            moto.buyTime(int(arg[1]))
        elif arg[0] == "drive":
            moto.driveMotoca(int(arg[1]))
        elif arg[0] == "honk":
            moto.honk()
        else:
            print("comando invalido")

main()
