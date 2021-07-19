#1) Escribir un programa que lea la información de vacunación por COVD-19 por provincias y
# almacene en estructuras que permitan dar respuestas a las siguientes consultas:
# 1. Dada una provincia informar total de vacunas aplicadas, tipo de vacuna con mayor
# cantidad de aplicaciones, tipo de vacuna con menor cantidad de aplicaciones.
# 2. Listar un ranking de las 10 provincias con mayor porcentaje de segundas dosis
# totales aplicadas
# 3. Listar un ranking de las vacunas por mayor porcentaje de segundas dosis totales
# aplicadas
#
#INICIO
# import csv
# import operator
#
# archivo = open("Covid19VacunasAgrupadas.csv", "r") #Puntero para el llamado del archivo
# leerDatos = csv.DictReader(archivo)
# datosVacunas = list(leerDatos)
# vacuna1 = int()
# vacuna2 = int()
# vacuna3 = int()
# vacuna4 = int()
#
#
# consulta = str(input("Ingrese la provincia a consultar: ")) #Input para consulta de provincia
# totalizador = 0
# for renglon in datosVacunas: #Bucle que totaliza las dosis
#     if renglon['jurisdiccion_nombre'] == consulta:
#         dosis1 = int(renglon['primera_dosis_cantidad'])
#         dosis2 = int(renglon['segunda_dosis_cantidad'])
#         totalVacunas = dosis2 + dosis1
#         totalizador = totalizador + totalVacunas
#
# for marcaVacuna in datosVacunas: #Bucle que totaliza por cada vacuna en variable
#     if marcaVacuna["vacuna_nombre"] == "AstraZeneca ChAdOx1 S recombinante":
#         vacuna1 = vacuna1 + int(marcaVacuna["primera_dosis_cantidad"])
#         vacuna1 = vacuna1 + int(marcaVacuna["segunda_dosis_cantidad"])
#     elif marcaVacuna["vacuna_nombre"] == "COVISHIELD ChAdOx1nCoV COVID 19":
#         vacuna2 = vacuna2 + int(marcaVacuna["primera_dosis_cantidad"])
#         vacuna2 = vacuna2 + int(marcaVacuna["segunda_dosis_cantidad"])
#     elif marcaVacuna["vacuna_nombre"] == "Sinopharm Vacuna SARSCOV 2 inactivada":
#         vacuna3 = vacuna3 + int(marcaVacuna["primera_dosis_cantidad"])
#         vacuna3 = vacuna3 + int(marcaVacuna["segunda_dosis_cantidad"])
#     elif marcaVacuna["vacuna_nombre"] == "Sputnik V COVID19 Instituto Gamaleya":
#         vacuna4 = vacuna4 + int(marcaVacuna["primera_dosis_cantidad"])
#         vacuna4 = vacuna4 + int(marcaVacuna["segunda_dosis_cantidad"])
#
# print(f"El total de vacunas aplicadas en {consulta} es de: {totalizador}.")
#
# if vacuna1 > vacuna2 and vacuna1 > vacuna3 and vacuna1 > vacuna4: #Condicional que chequea cual vacuna tiene mas dosis
#     print("La vacuna con MAYOR cantidad de aplicaciones es AstraZeneca ChAdOx1 S recombinante.")
# elif vacuna2 > vacuna1 and vacuna2 > vacuna3 and vacuna2 > vacuna4:
#     print("La vacuna con MAYOR cantidad de aplicaciones es COVISHIELD ChAdOx1nCoV COVID 19.")
# elif vacuna3 > vacuna1 and vacuna3 > vacuna2 and vacuna3 > vacuna4:
#     print("La vacuna con MAYOR cantidad de aplicaciones es Sinopharm Vacuna SARSCOV 2 inactivada.")
# elif vacuna4 > vacuna1 and vacuna4 > vacuna2 and vacuna4 > vacuna3:
#     print("La vacuna con MAYOR cantidad de aplicaciones es Sputnik V COVID19 Instituto Gamaleya.")
#
# if vacuna1 < vacuna2 and vacuna1 < vacuna3 and vacuna1 < vacuna4: #Condicional que chequea cual vacuna tiene menos dosis
#     print("La vacuna con MENOR cantidad de aplicaciones es AstraZeneca ChAdOx1 S recombinante.")
# elif vacuna2 < vacuna1 and vacuna2 < vacuna3 and vacuna2 < vacuna4:
#     print("La vacuna con MENOR cantidad de aplicaciones es COVISHIELD ChAdOx1nCoV COVID 19.")
# elif vacuna3 < vacuna1 and vacuna3 < vacuna2 and vacuna3 < vacuna4:
#     print("La vacuna con MENOR cantidad de aplicaciones es Sinopharm Vacuna SARSCOV 2 inactivada.")
# elif vacuna4 < vacuna1 and vacuna4 < vacuna2 and vacuna4 < vacuna3:
#     print("La vacuna con MENOR cantidad de aplicaciones es Sputnik V COVID19 Instituto Gamaleya.")
#
#
#
# provincias2dosis = {}
# provincias = ["Buenos Aires","CABA","Catamarca","Chaco","Chubut","Corrientes","CÃ³rdoba","Entre RÃ\xados","Formosa","Jujuy","La Pampa","La Rioja","Mendoza","Misiones","NeuquÃ©n","RÃ\xado Negro","Salta","San Juan","San Luis","Santa Cruz","Santa Fe","Santiago del Estero","Tierra del Fuego","TucumÃ¡n"]
# total = 0
# for nombre in provincias: #Bucle que arma un diccionario con la provincia y cantidad de segundas dosis
#     for renglon in datosVacunas:
#         if renglon["jurisdiccion_nombre"] == nombre:
#             total2dosis = float(renglon['segunda_dosis_cantidad'])
#             total += total2dosis
#         provincias2dosis[nombre] = total
#     total = 0
#
# total_dosis2 = sum(provincias2dosis.values())
#
# porcentaje2dosis = {}
# porcentaje = float()
#
# for clave, valor in provincias2dosis.items(): #Bucle para calculo de porcentaje
#     porcentaje = round((valor * 100) / total_dosis2, 2)
#     porcentaje2dosis[clave] = porcentaje
#     porcentaje = 0
#
# porcentajeOrdenado = sorted(porcentaje2dosis.items(), key=operator.itemgetter(1), reverse=True)
# provinciasMayorPorcentaje = {}
#
# contador = 10
# for prov,porC in porcentajeOrdenado: #Bucle que selecciona las 10 primeras provincias
#     contador -= 1
#     provinciasMayorPorcentaje[prov] = porC
#     if contador == 0:
#         break
#
# print(f"El ranking de las provincias con mayor porcentaje de segundas dosis aplicadas es: {provinciasMayorPorcentaje}")
#
# AstraZeneca = float()
# COVISHIELD = float()
# Sinopharm = float()
# Sputnik = float()
#
#
# for renglon in datosVacunas: #Bucle que suma las segundas dosis por nombre de vacuna
#     if renglon["vacuna_nombre"] == "AstraZeneca ChAdOx1 S recombinante":
#             AstraZeneca = AstraZeneca + float(renglon['segunda_dosis_cantidad'])
#     elif renglon["vacuna_nombre"] == "COVISHIELD ChAdOx1nCoV COVID 19":
#             COVISHIELD = COVISHIELD + float(renglon['segunda_dosis_cantidad'])
#     elif renglon["vacuna_nombre"] == "Sinopharm Vacuna SARSCOV 2 inactivada":
#             Sinopharm = Sinopharm + float(renglon['segunda_dosis_cantidad'])
#     elif renglon["vacuna_nombre"] == "Sputnik V COVID19 Instituto Gamaleya":
#             Sputnik = Sputnik + float(renglon['segunda_dosis_cantidad'])
#
# totalNombreVacunas = AstraZeneca + COVISHIELD + Sinopharm + Sputnik
#
# #print que calcula porcentaje e imprime resultado por vacuna
# print("La vacuna AstraZeneca ChAdOx1 S recombinante tiene un",f"{((AstraZeneca*100)/totalNombreVacunas):.2f}","% de segundas dosis dadas.")
# print("La vacuna COVISHIELD ChAdOx1nCoV COVID 19 tiene un",f"{((COVISHIELD*100)/totalNombreVacunas):.2f}","% de segundas dosis dadas.")
# print("La vacuna Sinopharm Vacuna SARSCOV 2 inactivada tiene un",f"{((Sinopharm*100)/totalNombreVacunas):.2f}","% de segundas dosis dadas.")
# print("La vacuna Sputnik V COVID19 Instituto Gamaleya tiene un",f"{((Sputnik*100)/totalNombreVacunas):.2f}","% de segundas dosis dadas.")

#FIN

#2) Escribir un programa que lea un archivo de texto y escriba en otro archivo, una lista con
# las 10 palabras con mayor ocurrencia ordenadas por cantidad de ocurrencias, tener en
# cuenta una lista de palabras ignoradas en el análisis de ocurrencias.

#INICIO
import operator

resultado = open("resultado.txt", "w") #Apertura del archivo para el resultado
palabrasOut = open("palabrasIgnoradas.txt", "w")  #Apertura del archivo para las palabras no tomadas
archivo = open("texto.txt", "r") #Apertura del archivo con el texto
leerArchivo = archivo.read()

losSignos = ",.\n?!"

for x in range(len(losSignos)): #Eliminacion de los signos
    leerArchivo = leerArchivo.replace(losSignos[x], "")

lista = leerArchivo.split(" ") #Separacion de palabras por un espacio
lista2 = lista
diccPalabras = {}

contador = 0
for palabra in lista: #Bucle que contabiliza las palabras
    for palabra2 in lista2:
        if palabra == palabra2:
            contador += 1
    diccPalabras[palabra] = contador
    contador = 0

diccPalabras = sorted(diccPalabras.items(), key=operator.itemgetter(1), reverse=True) #Ordenamiento del diccionario por cantidad de frecuencias

#Encabezados de los archivos txt
resultado.write("LAS PALABRAS CON MAS FRECUENCIA SON:")
resultado.write("\n")
palabrasOut.write("LAS PALABRAS MENOS FRECUENTAS SON: ")
palabrasOut.write(str("\n"))

contadorPalabras = 10
for palabra, cantidad in diccPalabras: #Armado del archivo con palabras con mas repeticiones
    if contadorPalabras > 0:
        resultado.write(str(palabra))
        resultado.write(str("="))
        resultado.write(str(cantidad))
        resultado.write(str("\n"))
        contadorPalabras -= 1
    else:
        palabrasOut.write(str(palabra)) #Armado del archivo con palabras ignoradas
        palabrasOut.write(str("="))
        palabrasOut.write(str(cantidad))
        palabrasOut.write(str("\n"))
print(("los archivos han sido grabados con exito."))
#FIN