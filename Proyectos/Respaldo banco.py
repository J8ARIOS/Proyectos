import random

#FUNCION CONTADORA DE ERRORES
num_error = 0
def errores():
    if num_error == 3:
        print("\nNumero intentos fallidos excedidos, por favor ponte en contacto con nuestro soporte.")
        raise SystemExit
    else:
        pass
# Constante para el saldo inicial en pesos colombianos 

SALDO_INICIAL = 1000000 

# Variable para almacenar el saldo actual. Empieza con el saldo inicial. 

saldo = SALDO_INICIAL 

# Ejemplo de un bucle while en Python 

while True:

    print("\n1. Depositar dinero") 

    print("2. Retirar dinero") 

    print("3. Consultar saldo") 

    print("4. Imprimir tu saldo")

    print("5. Transferencia a otra cuenta")

    print("9. Salir") 

  # cambio de prueba para commit

    # Ejemplo de una variable en Python 

    opcion = input("\nSeleccione una opción: ") 

  

    # Ejemplo de conversión entre tipos de datos en Python 

    opcion = int(opcion) 

  

    # Ejemplo de condiciones if, elif, else en Python 

    if opcion == 1: 

        cantidad = input("\nIngrese la cantidad a depositar en pesos colombianos: ") 

        cantidad = float(cantidad)  # Conversión de string a float 

        saldo += cantidad  # Ejemplo de operaciones en variables en Python 

        print("\nDepósito realizado con éxito.") 

  

    elif opcion == 2: 

        cantidad = input("\nIngrese la cantidad a retirar en pesos colombianos: ") 

        cantidad = float(cantidad) 

        if cantidad <= saldo: 

            saldo -= cantidad 

            print("\nRetiro realizado con éxito.") 

        else: 

            print("\nNo tienes suficiente saldo para esta operación.") 

  

    elif opcion == 3: 

        print(f"\nTu saldo actual es: {saldo} pesos colombianos") 

  
    elif opcion == 4:
        
        archivo = open("Recibo.txt", "w") #Generar archivo txt

        num_cuenta = 0
        num_cuenta = num_cuenta
        num_cuenta = (random.randint(1000000000, 9999999999 ))
        
        cuenta = ("\nNumero de cuenta: ", num_cuenta)
        saldo_actual = ("\nSaldo actual: ", saldo)

        cuenta = str(cuenta)
        saldo_actual = str(saldo_actual)

        archivo.write(cuenta) #Imprimir numero de cuenta
        archivo.write(saldo_actual)  #Imprimir saldo actual

        archivo.close

        print("\nComprobante creado de manera correcta")

    elif opcion == 5: 

        intentos = 3
        #LOGICA CONTROL DE ERRORES
        Ficho = False
        while Ficho == False:
            #NUMERO DE CUENTA Y CONTROL 
            cuenta_ext = input("\n¿Cual es el numero de cuenta a donde se va a realizar la transaccion?: ")
            if len(cuenta_ext) == 10: 
                pass
                if cuenta_ext.isdigit():
                    Ficho = True
                else:
                    print("\nERROR: La cuenta solo debe contener numeros")
                    num_error = num_error+1
                    intentos = intentos-1
                    print("Intentos restantes: ", intentos)
                    errores()
            else:
                print("\nERROR: El numero de cuenta es invalido")
                num_error = num_error+1
                intentos = intentos-1
                print("Intentos restantes: ", intentos)
                errores()
        
        #LOGICA CONTROL DE ERRORES
        Ficho = False
        while Ficho == False:
            #CANTIDAD A TRANSFERIR Y CONTROL
            cantidad = input("\n¿Cual es la cantidad a trasnferir a la cuenta: " + cuenta_ext +" ?:  ")
            if cantidad.isdigit():
                if int(cantidad) > saldo:
                    print("\nSaldo insuficiente para realizar la transaccion")
                    num_error = num_error+1
                    intentos = intentos-1
                    print("Intentos restantes: ", intentos)
                    errores()
                else:
                    Ficho = True
            else:
                print("\nERROR: El valor a enviar solo debe contener numeros")
                num_error = num_error+1
                intentos = intentos-1
                print("Intentos restantes: ", intentos)
                errores()
            

        #MENSAJE COMPROBANTE
        opcion = input("\n¿Deseas enviar un mensaje junto a la transaccion? (s/n): ")
        if opcion == "s":
            mensaje = input("\nIntroduce el mensaje que deseas enviar: ")
        else:
            pass
        
        saldo = saldo - int(cantidad)

        #CREACION COMPROBANTE CON SUS DATOS
        comprobante = open("Comprobante de pago.txt", "w")

        NO_cuenta = ("\nNumero de cuenta: " + cuenta_ext + "\n")
        valor = ("Cantidad: $" + cantidad + "\n")

        comprobante.write("BANCOLOMBIA")
        comprobante.write(NO_cuenta)
        comprobante.write(valor)
        if opcion == "s":
            comprobante.write(mensaje) 
        else:
            pass   

        print("\nTrasferencia realizada con exito") 
        print("Comprobante creado")
        print("\nSaldo disponible:  ", saldo)
        print("\nSaldo cuenta externa: ", cantidad)

        comprobante.close

    elif opcion == 6:

        """
        Artu
        Historial de transacciones:
		• Mantener un registro de todas las transacciones realizadas (depósitos, retiros, transferencias).
		• Permitir a los usuarios consultar su historial de transacciones, mostrando una lista de todas las operaciones junto con las fechas y horas en que se realizaron.

        """ 

    elif opcion == 7: 

        """
        Nicolas
        Cambio de moneda:
		Permitir a los usuarios convertir una cantidad de su saldo a otra moneda (por ejemplo, de pesos colombianos a dólares o euros).
		Solicitar la cantidad que desean convertir y la moneda destino.
		Utilizar una tasa de cambio predefinida o integrar una API que proporcione tasas de cambio en tiempo real.
        Mostrar la cantidad convertida al usuario y actualizar su saldo si decide realizar la conversión.
        """

    elif opcion == 8: 

        """
        Robinson
        
        Agregar un pin a toda esta aplicacion.
        
        5. Cambio de PIN (Número de Identificación Personal):

        Permitir al usuario cambiar su PIN actual por uno nuevo.
        Solicitar al usuario que ingrese su PIN actual para verificar su identidad.
        Luego, pedir al usuario que ingrese el nuevo PIN y confirme ingresándolo nuevamente.
        Si los dos nuevos PIN ingresados coinciden, actualizar el PIN del usuario.
        Informar al usuario si el cambio fue exitoso o si hubo algún error (por ejemplo, si el PIN actual ingresado es incorrecto o si los dos nuevos PIN no coinciden).

        """

    elif opcion == 9: 

        print("\nGracias por utilizar nuestro servicio de cajero automático. ¡Hasta pronto!") 

        break  # Ejemplo de la sentencia break en Python 

  

    else: 

        print("\nOpción inválida. Por favor, intente de nuevo.") 

        continue  # Ejemplo de la sentencia continue en Python