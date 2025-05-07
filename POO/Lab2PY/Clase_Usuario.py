class Usuario():
    def __init__(self,nombre, Id, fecha_nacimiento , ciudad_nacimiento, tel, email, direccion):
        
        self.__nombre = nombre
        self.__Id = Id
        self.__fecha_nacimiento = fecha_nacimiento
        self.__ciudad_nacimiento = ciudad_nacimiento
        self.__tel = tel
        self.__email = email
        self.__direccion = direccion

    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_Id(self, Id):
        self.__Id = Id

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_ciudad_nacimiento(self, ciudad_nacimiento):
        self.__ciudad_nacimiento = ciudad_nacimiento

    def set_tel(self, tel):
        self.__tel = tel

    def set_email(self, email):
        self.__email = email

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_nombre(self):
        return self.__nombre
    
    def get_Id(self):
        return self.__Id
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    def get_ciudad_nacimiento(self):
        return self.__ciudad_nacimiento
    
    def get_tel(self):
        return self.__tel
    
    def get_email(self):
        return self.__email
    
    def get_direccion(self):
        return self.__direccion
    
    def __str__(self):
        return "\nNombre: " + str(self.__nombre) + "\nID: " + str(self.__Id) + "\nFecha de nacimiento: " + str(self.__fecha_nacimiento) + "\nCiudad de nacimiento: " + str(self.__ciudad_nacimiento) + "\nTelefono: " + str(self.__tel) + "\nE-mail: " + str(self.__email) + "\nDireccion: " + str(self.__direccion)



#mi_usuario = Usuario("Jacobo", 1036450439, "23 de julio", "Envigado", 3168124306, "jacoboo8a@gmail.com", "clle 40")

