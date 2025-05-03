class Direccion():
    
    def __init__(self, calle, nomenclatura, barrio, ciudad, edificio, apto):
        self.__calle = calle
        self.__nomenclatura = nomenclatura 
        self.__barrio = barrio
        self.__ciudad = ciudad
        self.__edificio = edificio 
        self.__apto = apto 
        
    def set_calle(self, calle):
        self.__calle = calle
        
    def set_nomenclatura(self, nomenclatura):
        self.__nomenclatura = nomenclatura
        
    def set_barrio(self, barrio):
        self.__barrio = barrio
        
    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad
        
    def set_edificio(self, edificio):
        self.__edificio = edificio
        
    def set_apto(self, apto):
        self.__apto = apto 
        
    def get_calle(self):
        return self.__calle
        
    def get_nomenclatura(self):
        return self.__nomenclatura
        
    def get_barrio(self):
        return self.__barrio
        
    def get_ciudad(self):
        return self.__ciudad
        
    def get_edificio(self):
        return self.__edificio
        
    def get_apto(self):
        return self.__apto
        
    def __str__(self):
        return "\nCalle: " + str(self.__calle) + "\n" + "Nomenclatura: " + str(self.__nomenclatura) + "\n" + "Barrio: " + str(self.__barrio) + "\n" + "Ciudad: " + str(self.__ciudad) + "\n" + "Edificio: " + str(self.__edificio) + "\n" + "Apto: " + str(self.__apto)
    
#tomas = Direccion("calle", "nomen", "trianon", "envigado", "amarillo", 201)

