######################## Trabajo Final 2020 ########################
#Profesor: Diego Rodriguez
#Alumnos: Pía Tamborenea - Marcelo Limideiro - Grupo 3 - Tema: A

import csv
import wget
import os

os.mkdir('c:/TPFinal') #crea directorio TPFinal para almacenar los archivos importados
url = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/direccion-general-de-estadisticas-y-censos/registro-precipitaciones-ciudad/historico_precipitaciones.csv"
wget.download(url, 'c:/TPFinal/historico_precipitaciones.csv') #descarga archivo a carpeta temporal
url = "https://data.buenosaires.gob.ar/dataset/13df72f9-0080-4480-ad89-68baa02e38b6/resource/6e20f472-3e39-4a5c-93b2-9d5d58cdfc04/download/historico_velocidad_maxima_viento.csv"
wget.download(url, 'c:/TPFinal/historico_velocidad_maxima_viento.csv')
url = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/direccion-general-de-estadisticas-y-censos/registro-temperatura-ciudad/historico_temperaturas.csv"
wget.download(url, 'c:/TPFinal/historico_temperaturas.csv')

datos_vientos = []
datos_precipitaciones = []
datos_temperaturas = []
lista_meses =["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

with open('c:/TPFinal/historico_velocidad_maxima_viento.csv','r') as archivo_vientos: #se declara un handler de apertura de archivo (with)
      l_vientos = archivo_vientos.read().splitlines() #asignamos a la lista la lectura del archivo y dividimos en lineas
      l_vientos.pop(0) #eliminamos la primer fila que contiene los titulos
      for i in l_vientos: #iteramos la lista de vientos y creamos una lista nueva con las posiciones de los datos que vamos a utilizar
          lineas_vientos = i.split(',')
          datos_vientos.append([str(lineas_vientos[0]),str(lineas_vientos[1]),float(lineas_vientos[3])])

with open('c:/TPFinal/historico_precipitaciones.csv.', 'r') as archivo_precipitaciones: #idem vientos, cambia el dato que se busca
      l_precipitaciones = archivo_precipitaciones.read().splitlines()
      l_precipitaciones.pop(0)
      for i in l_precipitaciones:
            lineas_precipitaciones = i.split(',')
            datos_precipitaciones.append([str(lineas_precipitaciones[0]), str(lineas_precipitaciones[1]), float(lineas_precipitaciones[2])])

with open('c:/TPFinal/historico_temperaturas.csv', 'r') as archivo_temperaturas: #idem vientos, cambia el dato que se busca
      l_temperaturas = archivo_temperaturas.read().splitlines()
      l_temperaturas.pop(0)
      for i in l_temperaturas:
            lineas_temperaturas = i.split(',')
            datos_temperaturas.append([str(lineas_temperaturas[0]), str(lineas_temperaturas[1]), float(lineas_temperaturas[4])])

def busqueda_general (agno,mes,datos): #funcion para realizar busquedas en las listas (temperaturas y vientos) generadas anteriormente
    resultado = float(0)
    for i in datos:
        if agno in i and mes in i:
            resultado = [i[-1]]
    resultado_funcion = ''.join(map(str, resultado))
    return resultado_funcion

def busqueda_precipitaciones (agno,mes,datos): #funcion para realizar busquedas en la lista de precipitaciones generada anteriormente
    resultado = float(0)
    for i in datos:
        if agno in i and mes in i:
            resultado = [i[2]]
    resultado_lluvias = ''.join(map(str, resultado))
    return resultado_lluvias

def preguntar_agno(): #funcion que pregunta el año a buscar. Bucle infinito para evitar error de tipeo
    agno_ok = True
    while agno_ok == True:
        consulta_agno = int(input("Por favor, ingrese el año que desea consultar (1991 a 2019): "))
        if 1990 < consulta_agno < 2020:
            agno_ok = False
        else:
            agno_ok = True
    consulta_agno = str(consulta_agno)
    return consulta_agno


def preguntar_mes(): #función que pregunta el mes a buscar. Bucle infinito para evitar error de tipeo
    meses_ok = True
    while meses_ok == True:
        consulta_mes = str(input("Por favor, ingrese el mes que desea consultar: "))
        if consulta_mes.lower() in lista_meses: #cambia a minúsculas los datos ingresados del mes y verifica que se encuentre en la lista de meses
            meses_ok = False
        else:
            meses_ok = True
    return consulta_mes

print("Este programa fue realizado para obtener datos estadísticos consultados de \n"
       "fuentes valederas. Muestra los milímetros de las precipitaciones, la velocidad\n"
      "máxima de los vientos y la temperatura media de un mes y año determinado. ")

#PROGRAMA PRINCIPAL
loop = True
while loop == True:

    consulta_agno = preguntar_agno() #llamado a función de busqueda de año
    consulta_mes = preguntar_mes() #llamado a función de busqueda de mes
    consulta_mes = consulta_mes.capitalize() #cambia a mayúsculas el primer caracter del mes a buscar ya que en la lista descargada está de esa manera
    resultado_precipitaciones = busqueda_precipitaciones(consulta_agno,consulta_mes,datos_precipitaciones) #asignación a variable del resultado de la busqueda de las precipitaciones
    resultado_temperaturas = busqueda_general(consulta_agno, consulta_mes,datos_temperaturas) #asignación a variable del resultado de la busqueda de las temperaturas
    resultado_vientos = busqueda_general(consulta_agno, consulta_mes,datos_vientos) #asignación a variable del resultado de la busqueda de los vientos
    print("\nEn", consulta_mes, "del año", consulta_agno, "la temperatura media fue de",resultado_temperaturas,"grados.\n" 
        "Los vientos fueron de", resultado_vientos,"Km/h y las precipitaciones fueron de", resultado_precipitaciones, "mm.\n")
    print("Para realizar la relación entre datos se necesitaría que ingrese nuevos parámetros. ")
    re_consulta_agno = preguntar_agno() #pide que se ingrese un año para luego relacionarlo con el anterior
    re_consulta_mes = preguntar_mes() #pide que se ingrese un mes para luego relacionarlo con el anterior
    re_consulta_mes = re_consulta_mes.capitalize()
    re_resultado_precipitaciones = busqueda_precipitaciones(re_consulta_agno,re_consulta_mes, datos_precipitaciones)
    re_resultado_temperaturas = busqueda_general(re_consulta_agno,re_consulta_mes, datos_temperaturas)
    re_resultado_vientos = busqueda_general(re_consulta_agno,re_consulta_mes, datos_vientos)
    print("\nEn", re_consulta_mes, "del año", re_consulta_agno, "la temperatura media fue de", re_resultado_temperaturas,
          "grados.\n"
          "Los vientos fueron de", re_resultado_vientos, "Km/h y las precipitaciones fueron de", re_resultado_precipitaciones,
          "mm.\n")

    if float(resultado_temperaturas) <= float(re_resultado_temperaturas): #relaciona las dos temperaturas ingresas anteriormente y determina cual es mayor
        relacion_temperaturas = str("La temperatura que se registró en el primer dato es menor a la del segundo. ")
    else:
        relacion_temperaturas = str("La temperatura que se registró en el primer dato es mayor a la del segundo. ")

    if float(resultado_vientos) <= float(re_resultado_vientos): #relaciona los dos vientos ingresas anteriormente y determina cual es mayor
        relacion_vientos = str("El viento que se registró en el primer dato es menor al del segundo. ")
    else:
        relacion_vientos = str("El viento que se registró en el primer dato es mayor al del segundo. ")

    if float(resultado_precipitaciones) <= float(re_resultado_precipitaciones): #relaciona las dos precipitaciones ingresas anteriormente y determina cual es mayor
        relacion_precipitaciones = str("Las precipitaciones que se registraron en el primer dato es menor a la del segundo. ")
    else:
        relacion_precipitaciones = str("las precipitaciones que se registraron en el primer dato son mayores a la del segundo. ")

    print(relacion_temperaturas)
    print(relacion_vientos)
    print(relacion_precipitaciones)


    respuesta_ok = True
    while respuesta_ok == True: #bucle infinito para seguir consultado. Sólo acepta s o n
        print()
        respuesta = input("Desea continuar consultando (S/N): ")
        if not (respuesta.upper() == 'S' or respuesta.upper() == 'N'):
           print ("ERROR. Caracter no válido")
           respuesta_ok = True
        else:
           if respuesta.upper() == "N":
               respuesta_ok = False
               loop = False
           else:
               respuesta_ok = False


os.remove('c:/TPFinal/historico_precipitaciones.csv') #remueve el archivo temporal descargado en el inicio del programa para realizar las busquedas
os.remove('c:/TPFinal/historico_temperaturas.csv')
os.remove('c:/TPFinal/historico_velocidad_maxima_viento.csv')
os.removedirs("c:/TPFinal") #remueve la carpeta temporal de trabajo creada al inicio del programa
print()
print("Gracias por usar nuestra aplicación.")
print("Programa Finalizado. Pía y Marcelo.")

