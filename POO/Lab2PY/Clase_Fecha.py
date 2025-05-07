class Fecha:   
    def __init__(self,dd,mm,aa):
        self.__dd=dd
        self.__mm=mm
        self.__aa=aa
    
    def get_dd(self):
        return self.__dd
    
    def get_mm(self):
        return self.__mm
    
    def get_aa(self):
        return self.__aa
    
    def set_dd(self,dd):
        self.__dd=dd
    
    def set_mm(self,mm):
        self.__mm=mm
    
    def set_aa(self,aa):
        self.__aa=aa

    def __str__(self):
        return str(self.__dd)+"/"+str(self.__mm)+"/"+str(self.__aa)
    


    