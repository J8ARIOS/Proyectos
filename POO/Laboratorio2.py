from Clase_Fecha import Fecha
from Clase_Usuario import Usuario
from Clase_Direccion import Direccion

Fecha_nacimiento = Fecha(23, 7, 2006)
print(Fecha_nacimiento)

Direccion_casa = Direccion("Calle 47", "Sur #39B05", "Trianon", "Envigado", "El amarillo", 201 )
print(Direccion_casa)

Usuario1 = Usuario("Jacobo", 1036450439, "23 de julio", "Envigado", 3168124306, "jacoboo8a@gmail.com", "clle 40")
print(Usuario1)


nombre = input("\nIngrese su nombre: ")
Id = int(input("Ingrese su ID: "))
Fecha_nac = input("Ingrese su fecha de nacimiento: ")
ciudad = input("Ingrese su ciudad de residencia: ")
telefono = int(input("Ingrese su numero de telefono: "))
Email = input("Ingrese su E-mail: ")
direcc = input("Ingrese su direccion: ")

Usuario2 = Usuario(nombre, Id, Fecha_nac, ciudad, telefono, Email, direcc)
print(Usuario2)