class Clock:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def getSecond(self) -> int:
        return self.__second

    def setSecond(self, second: int) -> bool:
        if second in range(0,60):
            self.__second = second
            return True
        else:
            print("fail: segundo invalido")
            return False

    def getMinute(self) -> int:
        return self.__minute

    def setMinute(self, minute: int) -> bool:
        if minute in range(0,60):
            self.__minute = minute
            return True
        else:
            print("fail: minuto invalido")
            return False

    def getHour(self) -> int:
        return self.__hour

    def setHour(self, hour: int) -> bool:
        if hour in range(0,24):
            self.__hour = hour
            return True
        else:
            print("fail: hora invalida")
            return False

    def __str__(self) -> str:
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

    def nextSecond(self):
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.__minute += 1
            if self.__minute == 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

def main():
    clock: Clock = Clock()
    while True:
        line: str = input()
        arg: list[str] = line.split()
        print("$" + line)
        if len(arg) == 0:
            continue
        if arg[0] == "end":
            break
        elif arg[0] == "init":
            h, m, s = map(int, arg[1:])
            clock = Clock(h,m,s)
        elif arg[0] == "set":
            h, m, s = map(int, arg[1:])
            clock.setHour(h)
            clock.setMinute(m)
            clock.setSecond(s)
        elif arg[0] == "show":
            print(clock)
        elif arg[0] == "next":
            clock.nextSecond()
        else:
            print("fail: comando invalido")
main()
