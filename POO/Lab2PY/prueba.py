from Clase_Fecha import Fecha
from Clase_Usuario import Usuario
from Clase_Direccion import Direccion

#Usuario1
Fecha_nacimiento = Fecha(0, 0, 0)
Fecha_nacimiento.set_dd(23)
Fecha_nacimiento.set_mm(7)
Fecha_nacimiento.set_aa(2006)
print("\n", Fecha_nacimiento)

Direccion_casa = Direccion(0, "", "", "", "", 0)
Direccion_casa.set_calle(47)
Direccion_casa.set_nomenclatura("Sur #39B05")
Direccion_casa.set_barrio("Trianon")
Direccion_casa.set_ciudad("Envigado")
Direccion_casa.set_edificio("El amarillo")
Direccion_casa.set_apto(201)
print(Direccion_casa)


Usuario1 = Usuario("", 0, "", "", 0, "", "")
Usuario1.set_nombre("Jacobo")
Usuario1.set_Id(1036450439)
Usuario1.set_fecha_nacimiento(Fecha_nacimiento)
Usuario1.set_ciudad_nacimiento("Envigado")
Usuario1.set_tel(3168124306)
Usuario1.set_email("jacoboo8a@gail.com")
Usuario1.set_direccion(Direccion_casa)
print(Usuario1)

#Usuario2
nombre = input("\nIngrese su nombre: ")
Id = int(input("Ingrese su ID: "))

Fecha_nacimiento2 = Fecha("", "", "")
dia = input("Ingresa tu dia de nacimient: ")
Fecha_nacimiento2.set_dd(dia)
mes = input("Ingrese su mes de nacimiento: ")
Fecha_nacimiento2.set_mm(mes)
año = input("Ingrese su año de nacimiento: ")
Fecha_nacimiento2.set_aa(año)

ciudad = input("Ingrese su ciudad de nacimiento: ")
telefono = int(input("Ingrese su numero de telefono: "))
Email = input("Ingrese su E-mail: ")

Direccion_casa2 = Direccion(0, "", "", "", "", 0)
print("\nA continuacion le pediremos sus datos de residencia\n")
calle = input("Ingrese el numero de calle: ")
Direccion_casa2.set_calle(calle)
nomenclatura = input("Ingrese la nomemclatura: ")
Direccion_casa2.set_nomenclatura(nomenclatura)
barrio = input("Ingrese el barrio: ")
Direccion_casa2.set_barrio(barrio)
ciudad = input("Ingrese la ciudad: ")
Direccion_casa2.set_ciudad(ciudad)
edificio = input("Ingrese el edificio: ")
Direccion_casa2.set_edificio(edificio)
apto = input("Ingrese el apartamento:")
Direccion_casa2.set_apto(apto)

Usuario2 = Usuario("", 0, "", "", 0, "", "")
Usuario2.set_nombre(nombre)
Usuario2.set_Id(Id)
Usuario2.set_fecha_nacimiento(Fecha_nacimiento2)
Usuario2.set_ciudad_nacimiento(ciudad)
Usuario2.set_tel(telefono)
Usuario2.set_email(Email)
Usuario2.set_direccion(Direccion_casa2)


print(Usuario2)
print("")