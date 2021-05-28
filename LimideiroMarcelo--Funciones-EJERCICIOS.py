#1) Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un
#cilindro usando la primera función.
# #import math #Importo libreria math para uso de pi
#
#INICIO
# def areaCirculo(radio):
#     area = math.pi * pow(radio,2)
#     #return print(f"El área del circulo es {area:.3f}")
#     return area

# def areaTotal(altura,radio):
#     areaLateral = 2 * math.pi * radio * altura
#     areaTotal = areaLateral + (areaCirculo(radio))
#     #return print(f"El área del cilindro es: {(areaTotal):3.f}")
#     return areaTotal
#
# radio = float(input("Ingrese el radio del circulo: "))
# altura = float(input("Ingrese la altura del cilindro: "))
#
##Llamada a funcion
# aCirculo = (areaCirculo(radio))
# aCilindro = (areaTotal(altura,radio))
##Impresión de resultados
# print(f"El área del circulo es {aCirculo:.3f}")
# print(f"El área del cilindro es: {aCilindro:.3f}")

#FIN
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
#2) Escribir una función que reciba una muestra de números en una lista y devuelva su media.

#INICIO
# def numeros():
#     cantidadNumeros = int(input("Ingrese la cantidad de números que desea promediar: "))
#     total = 0
#     listaNumeros = []
#     for i in range (cantidadNumeros): #For que agrega numeros a la lista
#         numero = float(input("Ingrese un numero: "))
#         listaNumeros.append(numero)
#     for j in (listaNumeros): #For que recorre la lista y totaliza los valores
#         total = total + j
#     promedio = total / cantidadNumeros
#     return print(f"El promedio es {promedio:.2f}")
#
# numeros()

#FIN
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
#3) Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario
# generado con la función anterior y devuelva una tupla con la palabra más repetida y su
# frecuencia.

#INICIO
# import operator
# cadenaCaracteres = str(input("Ingrese un texto: "))
#
# def armadoDicc(cadena): #Funcion que arma el diccionario
#     cadenaTexto = {}
#     listaPalabras = cadena.split()
#     for palabra in listaPalabras:
#         frecuencia = listaPalabras.count(palabra)
#         cadenaTexto[palabra] = frecuencia
#     return cadenaTexto
#
# def palabraMasRepetida(listaPalabras): #Funcion que muestra palabra y repeticiones
#     mayorFrecuencia = max(listaPalabras, key = listaPalabras.get)
#     repeticiones = listaPalabras.get(mayorFrecuencia)
#     return print(f"la palabra {mayorFrecuencia} es la que más se repite con {repeticiones} repeticiones.")
# #Llamado a funciones
# listaDePalabras =armadoDicc(cadenaCaracteres)
# palabraMasRepetida(listaDePalabras)
#FIN
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
#4) Escribir una función que reciba otra función y una lista, y devuelva otra lista con el
#resultado de aplicar la función dada a cada uno de los elementos de la lista.

#INICIO
# import math
#
# cadena = []
#
# def ingresoNumero(lista): #Función que ingresa números y arma la lista
#     contador = 10
#     for i in range(10):
#         numero = float(input("Ingrese un número cualquiera: "))
#         contador -= 1
#         print(f"Faltan ingresar {contador} numeros")
#         lista.append((numero))
#     return lista
#
# def aplicandoPI(lista): #Función llama a la funcion de listas que aplica PI a cada item de la lista
#     cadenaPI = []
#     for i in (ingresoNumero(lista)):
#         numPI = math.pi * i
#         cadenaPI.append(numPI)
#     return print(f"La cadena resultante al aplicar la multiplicación de PI es : {cadenaPI}")
#
# aplicandoPI(cadena)

#FIN
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
#5) Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con
#los elementos de la lista que devuelvan True al aplicarles la función booleana.

#INICIO
# nombreCalles = ["Avellaneda","Rivadavia1266","Moreno","Machado2"]
#
# def validacion(nombre): #Funcion que valida la calle
#     valido = nombre.isalpha()
#     return valido
#
# def busqueda(nombre): #Funcion que itera la lista
#     resultadoCalles = []
#     for i in nombre:
#         aprobacion = str(validacion(i))
#         resultadoCalles.append(aprobacion)
#     return resultadoCalles
#
# #Llamado a funcion
# resultado = busqueda(nombreCalles)
# resultadoBusqueda = zip(nombreCalles,resultado) #Une las listas intercaladas
# print(tuple(resultadoBusqueda))

#FIN
