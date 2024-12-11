# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:23:34 2024

@author: bamay
"""
import math

"""
 Función mediaAritmetica():
     Calcula el valor de la media aritmetica de todos los valores de una lista de números ingresada
     Divide la suma total de los datos ingresados por el número de datos ingresados, retornando el promedio
    
 Variables:
    -suma: Suma de todos los valores de la lista
    -x_aritmetica: Media aritmética calculada del cociente entre las 2 variables mencionadas
"""

def mediaAritmetica(valores):
    
    lista = []
    for i in valores:   #Ciclo para deshacerse de los nans
        if math.isfinite(i):
            lista.append(i)
        
    suma = sum(lista)
    n = len(lista)
    x_aritmetica = suma/n   #Se realiza el cálculo de la media aritmética
        
    return x_aritmetica     #Se retorna x_aritmetica

"""
 Función Mediana():
     Retorna la mediana de una lista de números ingresada
     Ordena la lista con tal de buscar el valor medio de la misma mediante división entera
     Mediante el módulo entre la cantidad de datos y 2 se determina si la lista es par o no
     Si es par, retorna el promedio de la suma entre los 2 valores medios de la lista
     Si es impar, retorna el valor medio calculado

 Variables:
    -largo_lista: Largo de la lista de valores ingresada
    -valor_medio: División entera de largo_lista en 2, equivale a la posición media del conjunto de datos
    -determinante: Módulo entre largo_lista y 2. Determina si largo_lista es par dependiendo si da 0 o distinto de 0
    -med: Valor de la mediana de la lista de valores ingresados
        Si es impar equivale al valor ubicado en el valor medio de la lista
        Si es par equivale al promedio de la suma entre el número ubicado en valor_medio y su predecesor (ya que era división entera)
"""
    
def mediana(valores):
    
    lista = []  #Ciclo para deshacerse de los nans
    for i in valores:
        if math.isfinite(i):
            lista.append(i)
    
    lista.sort()
    largo_lista = len(lista)
    valor_medio = len(lista)//2
    determinante = largo_lista%2
    
    if determinante != 0:
        med = lista[valor_medio]
        return med
    
    elif determinante == 0:
        med = (lista[valor_medio]+lista[valor_medio-1])/2
        return med

"""
 Función moda():
     Función que calcula la moda de una lista dada y retorna cada variable que se repite el máximo de veces
     Primero genera una lista con todas las variables sin repetición y otra con la cantidad de veces que se repiten respectivamente
     Después genera otra lista adicional, donde se añade cada variable que se repite la mayor cantidad de veces
     Finalmente, retorna dos listas:
        La lista con todas las modas y su cantidad de repeticiones en el índice 0
        Una lista con listas pareadas, las cuales contienen cada variable y numero de repeticiones
             La variable esta en el índice 0 y su cantidad de repeticiones en el índice 1
             La lista está ordenada desde el menos repetido hacia los más repetidos

 Variables:
    -listaVariables: Lista con cada variable individual de la lista ingresada
    -Cantidades: Lista con la cantidad respectiva de repeticiones de los valores en listaModa
    -cont: Contador empleado para determinar la cantidad de veces que se repite cada variable en listaVariables
    -listaModas: Lista con cada moda de la lista, la cantidad de veces se halla en el índice 0
    -maximo: Valor máximo de repeticiones que alcanza una variable, equivale al valor máximo en Cantidades
    -listaCantidades: Lista que contiene una listas pareadas con cada variable y su cantidad respectiva de repeticiones     
"""

def moda(valores):
    
    listaVariables = []
    Cantidades = []
    for i in valores:    #Ciclo para añadir los valores de la lista sin repetir a listaVariables
        if i not in listaVariables:
            listaVariables.append(i)
            
    for j in listaVariables:    #Ciclo usado para comparar la lista ingresada con listaVariables
        cont = 0        
        for k in valores:     #Cada vez que se repita la variable correpondiente en lista se suma 1 a cont
            if j == k:
                cont +=1
        Cantidades.append(cont)
    
    listaModas = []
    maximo = max(Cantidades)
    listaModas.append(maximo)
    
    for l in range(len(Cantidades)):   #Ciclo usado para añadir cada variable que se repita el máximo de veces a listaModas
        if maximo == Cantidades[l]:
            listaModas.append(listaVariables[l])
    
    listaCantidades = []
    for m in range(maximo+1):    #Ciclo usado para crear las listas pareadas de listaCantidades
        for n in range(len(listaVariables)):    #Recorre la lista de cantidades comparando la cantidad
            if m == Cantidades[n]:              
                lista = []
                lista.append(listaVariables[n])     
                lista.append(Cantidades[n])
                listaCantidades.append(lista)       
    
    return listaModas, listaCantidades    #Retorna listaModas y listaCantidades

"""
 Función rango():
     Calcula el rango de una lista de datos ingresada, siendo este la diferencia entre el valor máximo y el mínimo de la lista

 variables:
    -maximo: Valor máximo de la lista
    -minimo: Valor mínimo de la lista
    -rango: resto entre máximo y mínimo
"""

def rango(valores):
    
    lista = []
    for i in valores:   #Ciclo para deshacerse de los nans
        if math.isfinite(i):
            lista.append(i)
            
    maximo = max(lista)
    minimo = min(lista)
    rango = maximo-minimo
    return rango

"""
 Función varianza():
     Calcula la varianza de un lista de números ingresada
     Esto mediante la sumatoria de la diferencia entre cada valor de la lista y su promedio al cuadrado dividido por el largo del conjunto

 Variables:
     -prom: Media aritmética de los datos calculada con la función mediaAritmetica()
     -datosMinusProm: Lista que contiene el resto de cada valor de la lista y su promedio al cuadrado
     -n: Cantidad de valores de la lista ingresada
     -varianza: Varianza de los datos ingresados. Calculada como la suma de cada valor de datosMinusProm dividido por n
"""
    
def varianza(valores):
    
    lista = []
    for i in valores:   #Ciclo para deshacerse de los nans
        if math.isfinite(i):
            lista.append(i)
            
    prom = mediaAritmetica(lista)
    
    n = len(lista)
    
    datosMinusProm = []        
    for i in range(n):  #Ciclo para añadir el resto de cada valor de la lista y su promedio al cuadrado a datosMinusProm
        datosMinusProm.append((lista[i]-prom)**2)

    varianza = (sum(datosMinusProm)/n)
    
    return varianza

"""
 Función desvEst():
     Calcula la desviación estándar de una lista de números ingresada
     Ya que la desviación estándar se puede calcular como la raiz de la varianza, se llama a la función varianza y se eleva a 0.5

 Variables:
    #varianza_lista: 
"""

def desvEst(valores):
    
    lista = []
    for i in valores:   #Ciclo para deshacerse de los nans
        if math.isfinite(i):
            lista.append(i)
    
    varianza_lista = varianza(valores)
            
    return varianza_lista**0.5  #retorna la varianza elevada a 0.5

"""
 Función percentil():
     Retorna una lista con cada percentil de la lista de datos ingresada [1-99]
     Calcula cada percentil como n*k/100
        Donde:
             k = número respectivo del percentil
             n = largo del conjunto de datos

 Variables:
     -listaPercentiles: Lista que contiene cada percentil de la lista ingresada
         Ya que son 99 datos, el percentil correspondiente equivale a percentil-1
         ej: el percentil 78 en listaPercentiles se llama como listaPercentiles[77]
     -n: Cantidad de datos de la lista ingresada
     -percentil: Valor individual de un percentil, equivale a la posición del percentil en la lista
         Se calcula como n multiplicado al numero del percentil correspondiente dividido en 100
"""

def percentil(valores):
    
    lista = []  #Ciclo para deshacerse de los nans
    for k in valores:
        if math.isfinite(k):
            lista.append(k)
            
    lista.sort()
    listaPercentiles = []
    n = len(lista)
    
    for i in range(1,100):    #En este caso i en el for equivale al número correspondiente del percentil
        percentil = n*i//100    #De esta manera, en cada ciclo se añade el percentil correspondiente con i a listaPercentiles
        listaPercentiles.append(lista[percentil])

    return listaPercentiles

"""
 Función intercuartil():
     Devuelve el rango intercuartílico de una lista de datos, siendo este la diferencia entre su respectivo cuartil 3 y 1
     Ya que los cuartiles son equivalentes a los percentiles 25, 50 y 75, se utiliza la función percentil para ello

 Variables:
     -percentiles: Lista con los percentiles de la lista de números ingresada, obtenida con la función percentil()
     -rangoInter: Valor equivalente al rango intercuartílico, resto entre el cuartil 3 y el 1
         Utilizando percentiles: cuartil 3 = percentil 75, cuartil 1 = percentil 25
"""

def intercuartil(valores):
    
    percentiles = percentil(valores)    #Se llama a la función percentiles()
    
    rangoInter = percentiles[74]-percentiles[24]
    
    return rangoInter   #Retorna el rango Intercuartílico

"""
 Función MAD():
     Calcula la desviación mediana absoluta de una lista de números ingresada
     Se calcula la mediana mediante la misma lógica usada en la función de mediana()
     Genera una lista donde se incluye cada el valor absoluto de la diferencia entre cada valor de la lista ingresada y su mediana
     Ordena la lista y, retorna la desviación mediana absoluta correspondiente en caso de si:
         Es impar, retorna el valor ubicado al medio de la lista
         Es par, retorna el promedio de la suma de los 2 valores ubicados al medio de la lista

 Variables:
     -n: Cantidad de datos en la lista
     -med: Mediana de la lista ingresada, calculada con la función mediana()
     -datosMinusMed: Lista que contiene el valor absoluto de la diferencia entre cada valor de la lista y su mediana
     -medio: Posición media de la lista, calculada con división entera
     -determinante: Variable que define mediante el módulo de n y 2 si la lista es par o no
     -MAD: Valor de la desviación mediana absoluta de la lista ingresada
"""
    
def MAD(valores):
    
    lista = []  #Ciclo para deshacerse de los nans
    for k in valores:
        if math.isfinite(k):
            lista.append(k)
    
    lista.sort()
    n = len(lista)
    medio = n//2
    determinante = n%2
    
    if determinante != 0:
        med = lista[medio]
    elif determinante == 0:
        med = (lista[medio]+lista[medio-1])/2
        
    n = len(lista)    
    datosMinusMed = []
    for i in range(n):
        datosMinusMed.append(abs(lista[i]-med))
    
    datosMinusMed.sort()
    
    if determinante!=0:     #Si la lista es impar, devuelve el valor de la posición media de la lista
        MAD = datosMinusMed[medio]
        return MAD
    
    else:   #Si la lista es par, devuelve el promedio entre los valores medios de la lista
        MAD = (datosMinusMed[medio]+datosMinusMed[medio-1]/2)
        return MAD
    

