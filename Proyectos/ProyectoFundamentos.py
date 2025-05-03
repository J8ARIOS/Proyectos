# LISTAS INICIALES
Cedulas = [1000556648, 1036450439, 1067887707, 22132486]
PuntoN = [800, 1500, 2500, 4000]
Nombres = ["Natalia Giraldo", "Jacobo Ochoa", "Fernando Alvarino", "Juan Gabriel Goez"]
# FUNCIONES
import random

def membresias(puntos):
    """Determina la membresía del usuario basado en los puntos acumulados."""
    if puntos >= 3000:
        return ["Gold", 25, 0.75]
    elif 2000 <= puntos <= 2999:
        return ["Silver", 20, 0.8]
    elif 1000 <= puntos <= 1999:
        return ["Bronze", 15, 0.85]
    elif 0 <= puntos <= 999:
        return ["Aqua", 5, 0.95]
    else:
        return ["Sin membresía", 0, 1.0]

def usuario_nuevo():
    """Registra un nuevo usuario en el sistema."""
    nombre_nuevo = input("\nPor favor, digite su nombre: ")
    cedula_nueva = obtener_entero("\nPor favor, digite su cédula: ")
    if cedula_nueva in Cedulas:
        print("\n¡Error! La cédula ya está registrada.")
        return
    Nombres.append(nombre_nuevo)
    Cedulas.append(cedula_nueva)
    PuntoN.append(0)
    print("\n¡Usuario registrado con éxito!")

def obtener_entero(mensaje):
    """Solicita un número entero al usuario y maneja errores de entrada."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def participar_rifa():
    print("A continuacion vas a sacar un valor de descuento al azar, y este se aplicara a su proxima compra mas el que posea por su membresia, ¡Buena Suerte!")
    lista_rifa = [75, 50, 25, 10]
    global rifa
    rifa = random.choice(lista_rifa)
    print(f"¡¡¡Felicidades!!!, acaba de ganar un descuento de {rifa}% valido para su proxima compra")

def registrar_compra(Cedula, puntos):
    """Registra una compra y actualiza los puntos del usuario."""
    membresia = membresias(puntos)
    venta = obtener_entero('\nIngresa el monto de la venta: ')
    puntos_venta = round(venta / 1000)
    puntos_acumulados = round((venta / 1000) + puntos)
    compra = round(venta * (membresia[2] - (rifa / 100))) 
    print(rifa)
    ahorro = round(venta * (1 - membresia[2]))

    if rifa > 0:
        ahorro = round(venta *((1 - membresia[2]) + (rifa / 100)))
        print(f'\nEres socio {membresia[0]}, tienes un descuento del {membresia[1]}% mas {rifa}% que obtuviste en la rifa')
        print(f'Precio a pagar es de ${compra} y su ahorro fue de ${ahorro}')
        print(f'Puntos en esta compra: {puntos_venta}; Puntos acumulados: {puntos_acumulados}')
    else:
        print(f'\nEres socio {membresia[0]}, tienes un descuento del {membresia[1]}%')
        print(f'Precio a pagar es de ${compra} y su ahorro fue de ${ahorro}')
        print(f'Puntos en esta compra: {puntos_venta}; Puntos acumulados: {puntos_acumulados}')
    
    for i in range(len(Cedulas)):
        if Cedula == Cedulas[i]:
            PuntoN[i] = puntos_acumulados
            return puntos_acumulados

def consultar_puntos(Cedula, puntos):
    """Muestra la información del usuario, incluyendo su membresía y puntos acumulados."""
    membresia = membresias(puntos)
    print("\nNombre:", Nombres[Cedulas.index(Cedula)])
    print("C.C.", Cedula)
    print("Membresia:", membresia[0])
    print("Puntos Acumulados:", puntos)



def eliminar_usuario(Cedula):
    """Elimina un usuario del sistema."""
    pregunta = input("\n¿Está seguro de querer borrar este usuario? s/n: ").lower()
    if pregunta == "s":
        index = Cedulas.index(Cedula)
        Nombres.pop(index)
        Cedulas.pop(index)
        PuntoN.pop(index)
        print("\nUsuario eliminado con éxito.")
        return True
    else:
        print("\nOperación cancelada.")
        return False

def mostrar_menu(Nombre):
    """Muestra el menú de opciones al usuario."""
    print("\nHola", Nombre, "¿Qué deseas hacer?")
    print("\n1. Registrar una compra")
    print("2. Consultar Puntos")
    print("3. Agregar usuario")
    print("4. Eliminar Usuario")
    print("5. Cambiar de usuario")
    print("6. Participar en rifa")
    print("7. Salir")
    


# CÓDIGO PRINCIPAL
print("\n>>> Bienvenido a MASxMENOS-MARKET <<<\n")
rifa = 0
def seleccionar_usuario():
    """Permite seleccionar un usuario existente o registrar uno nuevo."""
    while True:
        Cedula = obtener_entero('Ingresa número de cédula sin puntos o espacio (o 0 para salir): ')
        if Cedula == 0:
            print("\nGracias por visitarnos. ¡Vuelva pronto!")
            exit()
        if Cedula in Cedulas:
            index = Cedulas.index(Cedula)
            return Cedula, Nombres[index], PuntoN[index]
        else:
            print("\nEl usuario no se encuentra registrado.")
            pregunta = input("¿Deseas registrarlo? s/n: ").lower()
            if pregunta == "s":
                usuario_nuevo()
                Cedula = Cedulas[-1]  # Asignar la cédula del nuevo usuario
                return Cedula, Nombres[-1], PuntoN[-1]
            elif pregunta == "n":
                continue
            else:
                print("\nOpción incorrecta, intente de nuevo.")

# Bucle principal para manejar múltiples usuarios
while True:
    Cedula, Nombre, puntos = seleccionar_usuario()

    # Menú principal para el usuario seleccionado
    while True:
        mostrar_menu(Nombre)
        opcion = obtener_entero("\nPor favor, selecciona una opción: ")

        if opcion == 1:  # Registrar una compra
            puntos = registrar_compra(Cedula, puntos)
            rifa = 0
        elif opcion == 2:  # Consultar puntos
            consultar_puntos(Cedula, puntos)
        elif opcion == 3:  # Agregar usuario
            usuario_nuevo()
        elif opcion == 4:  # Eliminar usuario
            if eliminar_usuario(Cedula):
                break  # Salir del bucle si el usuario fue eliminado
        elif opcion == 5:  # Cambiar de usuario
            break  # Volver al menú de selección de usuario
        elif opcion == 6:  
            participar_rifa()
        elif opcion == 7:  # Salir
            print("\nGracias por utilizar nuestros servicios. ¡Vuelva pronto!")
            exit()
        else:
            print("\nOpción inválida, intente de nuevo.")