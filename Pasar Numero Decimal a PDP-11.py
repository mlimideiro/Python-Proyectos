##################### REPRESENTACION DE NUMERO DECIMAL EN SISTEMA PDP/11 ###########################
#Parte entera
parteEntera=int(input("Ingresar la parte entera de un numero positivo o negativo para ser convertido a PDP/11: "))
signo=""
if parteEntera<0:
  signo="1"
else:
  signo="0"
enteroimp=parteEntera
corte = True
entera=[]
while corte == True:
  if parteEntera<0:
    parteEntera=parteEntera*-1
  if parteEntera%2==0:
    entera.append(0)
    parteEntera = parteEntera//2
    if parteEntera<=0:
        corte = False
  else:
    entera.append(1)
    parteEntera = parteEntera//2
    if parteEntera<=0:
        corte = False

enteroImpresion=entera[:]
enteroImpresion=enteroImpresion[::-1]
enteraNormalizada=entera[::-1] #ROTACION LISTA PARA NORMALIZAR
enteraNormalizada.pop(0) 


#Parte decimal
parteDecimal=float(input("Ingresar la parte decimal del numero anterior para ser convertido PDP/11 (Ej.: 0.x): "))
decimalimp=parteDecimal
decimal=[]
for i in range(1,25): #Generacion de lista con numeros decimales binarios
    parteDecimal = parteDecimal*2
    if parteDecimal <1:
      decimal.append(0)
      parteDecimal = parteDecimal - 0
    else:
      decimal.append(1)
      parteDecimal = parteDecimal - 1


juntoEntero=' '.join(map(str, entera)) #Conversion de lista resultante a str para impresion
parteEnteraImpresion=' '.join(map(str, enteroImpresion))
juntoDecimal=' '.join(map(str, decimal))
juntoNormalizado=''.join(map(str, enteraNormalizada))

print()
print("El número ",enteroimp+decimalimp, " en binario es: ",parteEnteraImpresion,",",juntoDecimal)
binarioEntero=''.join(map(str, entera)) #Transformacion de lista a str parte entera
binarioDecimal=''.join(map(str, decimal)) #Transformacion de lista a str parte decimal

#################### NORMALIZACION DE NUMERO BINARIO ##########################

print("NORMALIZACION Y CÁLCULO DE EXPONENTE EN CD(2,8)")
listaExponente=[]

#CALCULO rcd
exponente=len(entera)
print("el exponente es: ",exponente)
rcd=128+exponente

while rcd !=0:
  if parteEntera<0:
    parteEntera=parteEntera*-1
  if rcd%2==0:
    listaExponente.append(0)
    rcd = rcd//2
  else:
    listaExponente.append(1)
    rcd = rcd//2
listaExponenteFlip=listaExponente[::-1] #Rotación de lista de exponente en binario


juntoExponente=''.join(map(str, listaExponenteFlip)) #Conversion de lista resultante a str para impresion   
print("El exponente en binario es: ",juntoExponente)


binarioConvertir=signo+juntoExponente+juntoNormalizado+binarioDecimal #Generación del numero binario final/Union de strings
print("Número binario a convertir en hexadecimal : ",binarioConvertir)

#################### CONVERSION BINARIO A HEXA ##########################
contador=int(0)
digito1=""
digito2=""
digito3=""
digito4=""
digito5=""
digito6=""
digito7=""
digito8=""

for i in binarioConvertir: #Separación de a 4 caracteres del binario final para empaquetar
  contador +=1
  if 1<=contador<=4:
    digito1= digito1 + i
  elif 5<=contador<=8:
    digito2= digito2 + i
  elif 9<=contador<=12:
    digito3= digito3 + i
  elif 13<=contador<=16:
    digito4= digito4 + i
  elif 17<=contador<=20:
    digito5= digito5 + i
  elif 21<=contador<=24:
    digito6= digito6 + i
  elif 25<=contador<=28:
    digito7= digito7 + i
  elif 29<=contador<=32:
    digito8= digito8 + i


def hexa(bin): #Función de busqueda de caracter hexa
  resultado=""
  if bin=="0000":
    resultado= resultado + "0"
  elif bin=="0001":
    resultado= resultado + "1"
  elif bin=="0010":
    resultado= resultado + "2"
  elif bin=="0011":
    resultado= resultado + "3"
  elif bin=="0100":
    resultado= resultado + "4"
  elif bin=="0101":
    resultado= resultado + "5"
  elif bin=="0110":
    resultado= resultado + "6"
  elif bin=="0111":
    resultado= resultado + "7"
  elif bin=="1000":
    resultado= resultado + "8"
  elif bin=="1001":
    resultado= resultado + "9"
  elif bin=="1010":
    resultado= resultado + "A"
  elif bin=="1011":
    resultado= resultado + "B"
  elif bin=="1100":
    resultado= resultado + "C"
  elif bin=="1101":
    resultado= resultado + "D"
  elif bin=="1110":
    resultado= resultado + "E"
  elif bin=="1111":
    resultado= resultado + "F"
  return resultado

  
digitoHexa1=hexa(digito1)
digitoHexa2=hexa(digito2)
digitoHexa3=hexa(digito3)
digitoHexa4=hexa(digito4)
digitoHexa5=hexa(digito5)
digitoHexa6=hexa(digito6)
digitoHexa7=hexa(digito7)
digitoHexa8=hexa(digito8)

numeroHexa=digitoHexa1+digitoHexa2+digitoHexa3+digitoHexa4+digitoHexa5+digitoHexa6+digitoHexa7+digitoHexa8 #Armado de str final con el nunero hexa
print("El número ",enteroimp+decimalimp,"en PDP/11 se representa: ",numeroHexa)








