class Clock:
    def __init__(self, hour:int, minute:int, second:int):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
    def __str__(self)->str:
        return f""
    def getHour(self)->int:
        return self.__hour
    def setHour(self, increment:int)->int:
        hour:int = self.__hour + 1
        if hour not in range(0,24):
            self.__hour = 0
        else:
            self.__hour = hour