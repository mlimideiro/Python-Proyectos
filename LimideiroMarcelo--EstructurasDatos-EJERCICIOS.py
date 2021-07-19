# 1) Escribir una función contar(x,y) que cuente cuántas veces aparece un carácter x dado en
# una cadena y.

#INICIO
# frase = str(input("Ingrese una cadena de caracteres: "))
# letra = str(input("Ingrese un caracter: "))
#
# # función de contador de palabras
# def contar(l,f):
#     contador = 0
#     for i in f:
#         if i == l:
#          contador = contador+1
#     return contador
#
# #llamado a función
# resultado = contar(letra,frase)
# print("La letra ", letra, " se repite ",resultado, " veces.")

#FIN
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
# 2) Escribir un programa que decida si hay más letras “A” o más letras “E” en una
# cadena.
#
#INICIO
# frase = str(input("Ingrese una cadena de caracteres: "))
#
# # función de contador de e y a
# def contar(f):
#     f = f.lower()
#     contadorA = 0
#     contadorE = 0
#     for i in f:
#         if i == "a":
#           contadorA += 1
#         elif i=="e":
#           contadorE += 1
#     #Condicional para respuesta
#     if contadorE > contadorA:
#         resultado = "La letra e aparece más veces que la letra a"
#     elif contadorA > contadorE:
#         resultado = "La letra a aparece más veces que la letra e"
#     elif contadorA == contadorE == 0:
#         resultado = "La letra a y la letra e no aparecen"
#     elif contadorA == contadorE and contadorA > 0:
#         resultado = "La letra e y la letra a aparecen igual cantidad de veces"
#     return resultado
#
# #llamado a función
# print(contar(frase))

#FIN
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
# 3)Escribir un programa que cuente cuantas veces aparecen cada una de las vocales en una
# cadena. No importa si la vocal aparece en mayúscula o en minúscula.
#frase = str(input("Ingrese una cadena de caracteres: "))

#INICIO
# función de contador de vocales
# def contar(f):
#     f = f.lower()
#     contadorA = 0
#     contadorE = 0
#     contadorI = 0
#     contadorO = 0
#     contadorU = 0
#     for i in f:
#      if i == "a":
#         contadorA += 1
#      elif i=="e":
#         contadorE += 1
#      elif i=="i":
#         contadorI += 1
#      elif i=="o":
#         contadorO += 1
#      elif i=="u":
#         contadorU += 1
#     return print("Recuento de vocales: a) ", contadorA, " e) ", contadorE, " i) ", contadorI, " o) ", contadorO, " u) ", contadorU)
#
# #llamado a función
# contar(frase)

#FIN
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#4)Escribir una función que reciba como parámetro una cadena de palabras separadas por
#espacios y devuelva, como resultado, cuántas palabras de más de cinco letras tiene la
#cadena dada.

#INICIO
# frase = str(input("Ingrese una cadena de caracteres: "))
# #función de contador de letras en palabras
# def contar(f):
#     cantLetras = f.split() #Separa la cadena por espacios
#     contador = 0
#     for i in cantLetras:
#         if len(i) > 4:
#             contador += 1
#     return print("El número de palabras de cinco o más letras es de : ",contador)
# # #llamado a función
# contar(frase)

#FIN
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#5)Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su
# oficina cortando todas las palabras de más de cinco letras a sólo cinco letras e indicando
# que una palabra fue cortada con el agregado de una arroba). Por otro lado cobra un valor
# para las palabras cortas y otro valor para las palabras largas (que deben ser cortadas).
# Escribir una función que reciba un texto, la longitud máxima de las palabras, el costo de
# cada palabra corta, el costo de cada palabra larga, y devuelva como resultado el texto del
# telegrama y el costo del mismo.

#INICIO
# telegrama = str(input("Ingrese el telegrama: "))
#
# #Procesado del telegrama
# def contar(f):
#      cantLetras = telegrama.split(" ")  # Separa el telegrama por espacios
#      contador = 0
#      telegResultante = []
#      for i in cantLetras:
#          if len(i) < 5:
#              telegResultante.append(i)
#          if len(i) > 4:
#              i = i.replace(i[4:], "@")
#              telegResultante.append(i)
#      return telegResultante
#
# #Costo telegrama
# def costoLargas(t):
#     palLargas = 0
#     for i in t:
#         if "@" in i:
#             palLargas += 1
#     return palLargas
#
# def costoCortas(t):
#     palCortas = 0
#     for i in t:
#         if not "@" in i:
#             palCortas += 1
#     return palCortas
#
# #Programa
# telegramaFinal = contar(telegrama)
# teleCostoCortas = costoCortas(telegramaFinal)
# teleCostoLargas = costoLargas(telegramaFinal)
# precioPalabrasCortas = 5
# precioPalabrasLargas = 8
# precioFinal = (precioPalabrasCortas*teleCostoCortas)+(precioPalabrasLargas*teleCostoLargas)
# print("El precio del telegrama es de: ",precioFinal," pesos")
# print(" ".join(telegramaFinal))

#FIN
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#6) Implementar un diccionario Inglés – Español, permitiendo agregar una palabra en inglés
# y su traducción al español, consultar la traducción de una palabra en ambos sentidos
# (inglés a español y español a inglés) contar la cantidad de palabras y mostrar el
# diccionario ordenado de la Z a la A.

#INICIO
# espaniolIngles = {"lluvia":"rain", "sol":"sun","loco":"crazy","telefono":"phone","brazo":"arm"}
# inglesEspaniol = {"rain":"lluvia","sun":"sol","crazy":"loco","phone":"telefono","arm":"brazo"}
#
# #Funciones
# def agregarPalabra(dicc1,dicc2):
#     palabra = str(input("Ingrese la palabra a agregar: "))
#     traduccion = str(input("Ingrese la traducción: "))
#     dicc1[palabra] = traduccion
#     dicc2[traduccion] = palabra
#     return "Palabra agregada."
#
# def accionRealizar(opcion):
#     opcion = int(input("¿Qué acción desea realizar?\n"
#                        "1) Agregar una palabra al diccionario Español-Ingles\n"
#                        "2) Agregar una palabra al diccionario Ingles-Español\n"
#                        "3) Consultar una palabra del Español al Inglés\n"
#                        "4) Consultar una palabra del Inglés al Español\n"
#                        "5) Contar la cantidad de palabras que tiene el diccionario\n"
#                        "6) Mostrar diccionario\n"))
#     return opcion
#
# def consultarPalabra(dicc):
#     consulta = str(input("Ingrese la palabra a consultar: "))
#     if consulta in dicc:
#        resultado = print("La traducción de ",consulta, " es: ",dicc[consulta])
#     else:
#         resultado = print("La palabra no se encuentra en el diccionario")
#     return resultado
#
# def largoDiccionario(dicc):
#     largo = len(dicc.keys())
#     return print("La cantidad de palabras con las que cuenta el diccionarios es de",largo)
#
# def ordenado(dicc):
#     sortdic = sorted(dicc.items(),reverse=True)
#     return print("El diccionario ordenado es: ",sortdic)
#
# #PROGRAMA PRINCIPAL
# loop = True
# opcion = 0
# while loop == True:
#     numOpcion = accionRealizar(opcion)
#     if numOpcion == 1:
#         agregarPalabra(espaniolIngles,inglesEspaniol)
#     elif numOpcion == 2:
#         agregarPalabra(inglesEspaniol,espaniolIngles)
#     elif numOpcion == 3:
#         consultarPalabra(espaniolIngles)
#     elif numOpcion == 4:
#         consultarPalabra(inglesEspaniol)
#     elif numOpcion == 5:
#         largoDiccionario(espaniolIngles)
#     elif numOpcion == 6:
#         ordenado(espaniolIngles)
#     elif numOpcion <1 or numOpcion > 6:
#         print("Opción no válida")
#
#     respuesta_ok = True
#     while respuesta_ok == True:  # bucle infinito para seguir consultado. Sólo acepta s o n
#         print()
#         respuesta = input("Desea continuar operando (S/N): ")
#         if not (respuesta.upper() == 'S' or respuesta.upper() == 'N'):
#             print("ERROR. Caracter no válido")
#             respuesta_ok = True
#         else:
#             if respuesta.upper() == "N":
#                 respuesta_ok = False
#                 loop = False
#             else:
#                 respuesta_ok = False
#
# FIN
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#7)Implementar una lista de precios que permita grabar el precio de un producto, consultar
# el precio de un producto, consultar todos los productos cuto precio sea mayor a un valor
# ingresado y mostrar los productos ordenados del más barato al más caro.

#INICIO
# import operator
# precioProductos = {"jabon":55 , "desodorante":197,"alcohol":240,"desodorante":170,"cotonetes":130}
#
# #Funciones
# def agregarProducto(dicc):
#     producto = str(input("Ingrese el producto a agregar: ")).lower()
#     precio = int(input("Ingrese el precio del producto: "))
#     dicc[producto] = precio
#     return "Producto agregado."
#
# def accionRealizar(opcion):
#     opcion = int(input("¿Qué acción desea realizar?\n"
#                        "1) Agregar un producto y su precio\n"
#                        "2) Consultar el precio de un producto\n"
#                        "3) Consultar todos los productos con un precio mayor a $\n"
#                        "4) Mostrar todos los productos ordenados por precio\n"))
#     return opcion
#
# def consultarPrecio(dicc):
#     consulta = str(input("Ingrese el producto a consultar: ")).lower()
#     if consulta in dicc:
#        resultado = print("El precio de ",consulta, " es: ",dicc[consulta])
#     else:
#         resultado = print("El producto no se encuentra en la lista de precios")
#     return resultado
#
# def baratoACaro(dicc):
#     precioBaratoCaro = dict(sorted(dicc.items(), key=operator.itemgetter(1)))
#     return print("El listado de productos ordenados por precios es: ",precioBaratoCaro)
#
# def mayorPrecio(dicc):
#     productosListados = {}
#     precioBase = int(input("Ingrese el precio mínimo a consultar: "))
#     for producto,precio in dicc.items():
#         if precio >= precioBase:
#             productosListados[producto] = precio
#     productosListados = sorted(productosListados.items(),reverse=True)
#     return print("La lista de productos resultantes ordenada por precio es: ",productosListados)
#
# #PROGRAMA PRINCIPAL
# loop = True
# opcion = 0
# while loop == True:
#     numOpcion = accionRealizar(opcion)
#     if numOpcion == 1:
#         agregarProducto(precioProductos)
#     elif numOpcion == 2:
#         consultarPrecio(precioProductos)
#     elif numOpcion == 3:
#         mayorPrecio(precioProductos)
#     elif numOpcion == 4:
#         baratoACaro(precioProductos)
#     elif numOpcion <1 or numOpcion > 4:
#         print("Opción no válida")
#
#     respuesta_ok = True
#     while respuesta_ok == True:  # bucle infinito para seguir consultado. Sólo acepta s o n
#         print()
#         respuesta = input("Desea continuar operando (S/N): ")
#         if not (respuesta.upper() == 'S' or respuesta.upper() == 'N'):
#             print("ERROR. Caracter no válido")
#             respuesta_ok = True
#         else:
#             if respuesta.upper() == "N":
#                 respuesta_ok = False
#                 loop = False
#             else:
#                 respuesta_ok = False
#
#FIN













