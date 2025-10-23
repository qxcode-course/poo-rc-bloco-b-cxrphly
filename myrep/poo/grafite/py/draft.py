class Lead:
    def __init__(self, thickness:int, hardness:str, size:int ):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerPage(self):

    def __str__(self):
        return f"{self.__thickness}:{self.__hardness}:{self.__size}"
    
class Pencil:
    def __init__(self, thickness:int):
        self.__thickness = thickness
        self.__tip: Lead | None = None

    def hasLead(self):
        return self.tip if not None else False
    
    def __str__(self):
        return f""
    def insertLead(self, tip:Lead):
        self.__tip = tip
    def removeLead(self):
        self.__tip = None
    def writePage(self):
