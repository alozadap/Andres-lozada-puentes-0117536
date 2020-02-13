# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:57:12 2020

@author: ANDRES FELIPE LOZADA
"""


#Valor Absoluto
num = float(input("Ingrese número: \n"))  
  #Se usa float, ya que el valor absoluto 
  #se puede aplicar a cualquier número real

if num<0:
    num=0-num
                #El else: se puede dejar vacío, u omitir
print (num)




#%%
#Primalidad de diferencias
num1 = int(input("Ingrese el primer número"))
num2 = int(input("Ingrese el segundo número"))
dif=0
esPrimo=True
    #Verificar el mayor, para tener la diferencia positiva
if(num1>num2):
    dif=num1-num2
else:
    dif=num2-num1

    #Verificar primalidad  /////mayor a dos, igual, menor (0,1)
if (dif>2):
    for i in range(dif-2):
        if(dif%(dif-i-1)==0): #Se resta uno para que no evalúe el mismo número 
                              #sino solo los que están dentro del intervalo
         esPrimo=False
elif(dif<2):
    esPrimo=False
    #Si es dos, continúa como primo

    #Imprimir
if(esPrimo==True):
    print("La magnitud entre "+str(num1)+
          " y "+str(num2)+" es un número primo \n")
else:
    print("La magnitud entre "+str(num1)+
          " y "+str(num2)+" no es un número primo \n")
    
#%%
#Múltiplicidad dentro de 100 primeros enteros positivos
contador=0
lista1=[]
lista2=[]
for i in range(1,101):
    if (contador<15):
        if (i%3==0):
            lista1.append(i)
            contador+=1
    else:
        if (i%4==0):
            lista2.append(i)
    #Imprimir listas
print (lista1[:])
print (lista2[:])

#%%

#Círculos y contenencia
import math

contCirculo1=False
contCirculo2=False

x1 = float(input("Ingrese x circulo 1: \n"))
y1 = float(input("Ingrese y circulo 1: \n"))
r1 = float(input("Ingrese r circulo 1: \n"))            
    
x2 = float(input("Ingrese x circulo 2: \n"))
y2 = float(input("Ingrese y circulo 2: \n"))
r2 = float(input("Ingrese r circulo 2: \n"))

a = float(input("Ingrese x punto: \n"))
b = float(input("Ingrese y punto: \n"))

 #Formula, distancia entre dos puntos (Centro del círculo y punto)

distCirculo1 = math.sqrt((a-x1)**2 + (b-y1)**2) 
distCirculo2 = math.sqrt((a-x2)**2 + (b-y2)**2)

    #Verificar contenencia

if (distCirculo1 <= r1):
    contCirculo1=True

if (distCirculo2 <= r2):
    contCirculo2=True


    #Imprimir
if(contCirculo1==True):
    if(contCirculo2==True):
        print("El punto está contenido en ambos círculos")
    else:
        print("El punto está contenido en el círculo 1")
else:
    if(contCirculo2==True):
        print("El punto está contenido en el círculo 2")
    else:
        print("El punto no está contenido en ningún círculo")
    
#%%
        
#Análisis cadena
cadena = str(input("Ingrese cadena: \n"))
a=0
b=0
c=0
d=0
e=0

marcador=0
for i in cadena:
    if (i in "AEIOU"):
        a+=1
    elif(i in "áéíóúÁÉÍÓÚ"):
         b+=1
    elif(i.isdigit()):
        c+=1
    elif(i ==" "):
        d+=1
while (cadena.find("in",marcador,len(cadena))!= -1):
    e+=1
    marcador=cadena.find("in",marcador,len(cadena))+1
        
print("a)Letras vocales mayúsculas: ",a)
print("b)Letras con tilde: ",b)
print("c)Dígitos encontrados: ",c)
print("d)Espacios encontrados: ",d)
print("e)palabras reservadas: ",e)
"""
"""
#Organizar alfabeticamente
cadena = str(input("Ingrese cadena: \n"))
listaCadena= list(cadena)
listaCadena.sort()

cadenaOrganizada=""

for i in listaCadena:
    if(i!=" "):
        cadenaOrganizada+=i 


print(cadenaOrganizada)
"""
"""
numeros=[]
estaOrdenado=True
x = int(input("¿Cuantos números ingresará a la lista?: \n"))
for i in range(x):
    aux=int(input("Ingrese el siguiente elemento"))
    numeros.append(aux)

    #Verificar orden
for i in range(len(numeros)-1):
    if (numeros[i]>numeros[i+1]):
        estaOrdenado=False
        
if(estaOrdenado==False):
    print("La lista no está ordenada")
else:
    nuevoNumero=int(input("Ingresar nuevo número"))
        
    #Verificar el índice del número menor o igual al número nuevo
aux2=0
for i in numeros:
    if (i>aux2 and i<=nuevoNumero):
        aux2=i
    #Encontrar el índice del número menor/igual al número nuevo
if(aux2!=0):    
    indice=numeros.index(aux2)
    numeros.insert(indice+1,nuevoNumero)
    #Se ingresa el número en el índice posterior
else:
    numeros.insert(0,nuevoNumero)
print (numeros)

    
#%%

#Verificar lista de números ascendentes
esOrdenado=True
strNumeros = int(input("Ingrese la lista de números"))
listaNumeros = list(str(strNumeros))
print(listaNumeros)

for i in range(len(listaNumeros)-1):
    if(listaNumeros[i] > listaNumeros[i+1]):
        esOrdenado=False
print(esOrdenado)
    #Verificar que estén ordenados

lista = list(input("ingresa lista"))

print
(lista)

#%%

#Segundo entero mayor
lista = [3,2,1,1,1]
primerMayor=lista[0]
segundoMayor=lista[0]

for i in lista:
    if (i > primerMayor):
        primerMayor=i
    if (i < primerMayor and i > segundoMayor):
        segundoMayor=i
if(primerMayor==segundoMayor):
    print("No existe un segundo elemento mayor")
else:
    print("El segundo elemento mayor es : ",segundoMayor)
    
#%%
   
#Términos de la sucesión
u = int(input("Ingrese u: \n"))
x = int(input("Ingrese el número de términos a calcular"))
listaTerminos=[]
listaTerminos.append(u)

for i in range(x):
    if(u % 2 == 0): #Par
        u=int(u/2)
    else:           #Inpar
        u=(u*3)+1
    listaTerminos.append(u)
print (listaTerminos)    

#%%

"""
 0,0 0,1 0,2 0,3 0,4
 1,0 1,1 1,2 1,3 1,4
 2,0 2,1 2,2 2,3 2,4
 3,0 3,1 3,2 3,3 3,4     
"""

matriz=[[59,99,95,12,88],
        [63,32,49,4,73],
        [40,28,62,78,6],
        [45,63,51,85,26]]
x=len(matriz[0])#5
y=len(matriz)#4
for i in range(y):
    for j in range(x):
        print (x-j,y-i)
    
    
#%%
        falta el 10
        
        
        
        
        
#%%

#Dibujar rectángulo
altura = int(input("Ingrese altura del rectangulo: \n"))
anchura = int(input("Ingrese ancho del rectangulo: \n"))
caracter = str(input("Ingrese caracter para dibujar: \n"))
caracter=caracter[0] #Verificar que sólo sea un caracter

def funcionRectangulo(alto,ancho,char):
    for i in range (alto):
        print ((char+" ")*ancho)

funcionRectangulo (altura,anchura,caracter)    


#%%

#Dibujar triangulo
anchura = int(input("Ingrese ancho del triángulo: \n"))

def funcionTriangulo(ancho):
    for i in range(ancho+1):
        espacios=ancho-i
        print(" "*espacios+"* "*i)

funcionTriangulo(anchura)

#%%

#Años bisiestos
primerAño = int(input("Ingrese el primer año (menor): \n"))
segundoAño = int(input("Ingrese el primer año (mayor): \n"))

def contarBisiesto(año1,año2):
    contador=0
    for i in range(año2-año1+1):
        if((año1+i)%4 == 0 and (año1+i) % 100 != 0 or (año1+i)%400==0):
            contador+=1

    print("hay ",contador,"años bisiestos entre el intervalo de años")

contarBisiesto(primerAño,segundoAño)

#%%


#Sumas
#def sumasAleatorias(respuesta):
import random
def sumasAleatorias():
    i=0
    while (i<5):
        numAleatorio1=random.randint(1,101)
        numAleatorio2=random.randint(1,101)
        respuestaCorrecta= numAleatorio1 + numAleatorio2
        respuestaUsuario=-1 #Fuera del rango de suma de enteros positivos
        print(numAleatorio1," + ",numAleatorio2," = ?")
        respuestaUsuario=int(input("Respuesta: "))
        while (respuestaCorrecta!=respuestaUsuario):
            respuestaUsuario=int(input("Respuesta: "))
        i+=1

sumasAleatorias() #Llamado


#%%

#Función juego mastter mind
import random
longitudCadena=int(input("Ingresa la cantidad de cifras del número a adivinar"))

def masterMind(cifras):
    esAcertado=False
    respuesta=0 #Fuera de rango
    numAleatorio=[]
    coincidencias=0

    for i in range(cifras):
        numAleatorio.append(str(random.randint(0,9)))
    while (esAcertado!=True):
        coincidencias=0
        respuesta=list(input("Intenta adivinar la cadena"))
        if(respuesta==numAleatorio):
            esAcertado=True
            print("Felicidades")
        else:
            for i in range(cifras):
                if (respuesta[i]==numAleatorio[i]):
                    coincidencias+=1
            print ("Ha adivinado ",coincidencias," valores")

masterMind(longitudCadena)    

    
    
    
