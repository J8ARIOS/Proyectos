import random

A = []
B = []
size = int(input("Ingresa el tamaño de los arreglos: "))

while size >= 12:
    if size > 12:  #No puede ser mayor que 12
        print("El numero debe ser menor o igual a 12, intente de nuevo")
        size = int(input("Ingresa el tamaño de los arreglos: "))    #Se pide al usuario el tamaño del los arreglo

#Arreglo A
for i in range(size):

    value = input(f"Ingresa el elemento {i} del arreglo A: ")

    try:    #Se intenta convertir en un entero, si no da, se pide que se ingrese de nuevo para poder ser agregado al arreglo A
        value = int(value)
    except ValueError: 
        print("El elemento debe ser un numero, intente de nuevo: ")
        value = input(f"Ingresa el elemento {i} del arreglo A: ")
        value = int(value)
    A.append(value)

#Arreglo B    
for _ in range(size):
    value = random.randint(1, 20) #Se utiliza la libreria random para elegir un numero en ese rango
    B.append(value)               #Y para luego ser agregado al arreglo B "size" numero de veces

#Se realiza la suma de los dos arreglos y se muestra el resultante
#sumA = sum(A)
#sumB = sum(B)
#sumAB = sumA + sumB
#print(f"\nLa suma entre los arreglos A: {A}= {sumA} y B: {B}= {sumB} da como resultado: {sumAB}\n")
AB = []
for a, b in zip(A, B):
    ab = a + b
    AB.append(ab)

print(f"Arreglo A: {A}")
print(f"Arreglo B: {B}")
print(f"\nEl arreglo resultante de sumar A y B es: {AB}\n")

#Producto punto entre los arreglos A y B
Ppunto = []

for a, b in zip(A, B):  #Emparejo a los elementos por posicion para iterar con ellos con sus respectivas posiciones en el otro arreglo
    ab = a * b
    Ppunto.append(ab)

sumPpunto = sum(Ppunto)
print(f"El producto punto entre los arreglos A y B da como resultado: {sumPpunto}\n")


#Calculo de los enteros pares del arreglo A
pairsA = [] #Lista para almacenar los enteros pares del arreglo A 

for i in A:
    if i % 2 == 0: #Si el numero del index que se esta revisando el reciduo de su division entre 2 es 0, quiere decir que es te es par
        pairsA.append(i) #Agregandolo asi a una lista para despues sumarlos
    else:
        pass

sumpairs = sum(pairsA) #Suma los elementos pares guardados del arreglo A anteriormente
print(f"La suma entre los enteros pares del arreglo A: {pairsA} es: {sumpairs}\n")   


#Calculo del promedio de los elementos del arreglo B
summation = 0
for i in B:
    summation = summation + i
average = summation / len(B)

print(f"El promedio de los elementos del arreglo B: {B} es: {average}\n")

#Construccion del arreglo C a partir de los arreglos A y B
C = []
for a, b in zip(A, B): #Se emparejan los arreglos A y B para poder iterar sobre cada pareja
    C.append(a)        #de valores y agregarlos al arreglo C intercalando entre un elemento de A y uno de B
    C.append(b)

print(f"Al juntar los arreglos A y B da como resultado el arreglo C: {C}\n")

#Determinar el valor maximo del arreglo C y su posicion
max_value = max(C)
max_index = C.index(max_value)

print(f"El valor maximo del arreglo C es: {max_value} y esta ubicado en el indice: {max_index}")
