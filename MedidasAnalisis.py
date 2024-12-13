



# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:23:34 2024

@author: bamay
"""
import math

def mediaAritmetica(valores):
    
    """
     Función mediaAritmetica():
         input: lista de datos(list), output: promedio de los datos(float)
         Calcula el valor de la media aritmetica de todos los valores de una lista de números ingresada
         Divide la suma total de los datos ingresados por el número de datos ingresados, retornando el promedio
        
     Variables:
        -suma(float): Suma de todos los valores de la lista
        -x_aritmetica(float): Media aritmética calculada del cociente entre las 2 variables mencionadas
    """
    
    lista = []
    for i in valores:   #Ciclo para deshacerse de los nans
        if math.isfinite(i):
            lista.append(i)
        
    suma = sum(lista)
    n = len(lista)
    x_aritmetica = suma/n   #Se realiza el cálculo de la media aritmética
        
    return x_aritmetica     #Se retorna x_aritmetica

def mediana(valores):
    
    """
     Función Mediana():
         input: lista de datos(list), output: mediana de los datos(float)
         Retorna la mediana de una lista de números ingresada
         Ordena la lista con tal de buscar el valor medio de la misma mediante división entera
         Mediante el módulo entre la cantidad de datos y 2 se determina si la lista es par o no
         Si es par, retorna el promedio de la suma entre los 2 valores medios de la lista
         Si es impar, retorna el valor medio calculado

     Variables:
        -largo_lista(int): Largo de la lista de valores ingresada
        -valor_medio(int): División entera de largo_lista en 2, equivale a la posición media del conjunto de datos
        -determinante(int): Módulo entre largo_lista y 2. Determina si largo_lista es par dependiendo si da 0 o distinto de 0
        -med(float): Valor de la mediana de la lista de valores ingresados
            Si es impar equivale al valor ubicado en el valor medio de la lista
            Si es par equivale al promedio de la suma entre el número ubicado en valor_medio y su predecesor (ya que era división entera)
    """
    
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

def moda(valores):
    
    """
     Función moda():
         input: lista de datos(list), output: listas con moda y variables (list)
         Función que calcula la moda de una lista dada y retorna cada variable que se repite el máximo de veces
         Primero genera una lista con todas las variables sin repetición y otra con la cantidad de veces que se repiten respectivamente
         Después genera otra lista adicional, donde se añade cada variable que se repite la mayor cantidad de veces
         Finalmente, retorna dos listas:
            La lista con todas las modas y su cantidad de repeticiones en el índice 0
            Una lista con listas pareadas, las cuales contienen cada variable y numero de repeticiones
                 La variable esta en el índice 0 y su cantidad de repeticiones en el índice 1
                 La lista está ordenada desde el menos repetido hacia los más repetidos

     Variables:
        -listaVariables(list): Lista con cada variable individual de la lista ingresada
        -Cantidades(list): Lista con la cantidad respectiva de repeticiones de los valores en listaModa
        -cont(int): Contador empleado para determinar la cantidad de veces que se repite cada variable en listaVariables
        -listaModas(list): Lista con cada moda de la lista, la cantidad de veces se halla en el índice 0
        -maximo(int): Valor máximo de repeticiones que alcanza una variable, equivale al valor máximo en Cantidades
        -listaCantidades(list): Lista que contiene una listas pareadas con cada variable y su cantidad respectiva de repeticiones     
    """
    
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

def rango(valores):
    
    """
     Función rango():
         input: lista de datos(list), output: rango de los datos(float)
         Calcula el rango de una lista de datos ingresada, siendo este la diferencia entre el valor máximo y el mínimo de la lista

     variables:
        -maximo(float): Valor máximo de la lista
        -minimo(float): Valor mínimo de la lista
        -rango(float): resto entre máximo y mínimo
    """
    
    lista = []
    for i in valores:   #Ciclo para deshacerse de los nans
        if math.isfinite(i):
            lista.append(i)
            
    maximo = max(lista)
    minimo = min(lista)
    rango = maximo-minimo
    return rango
    
def varianza(valores):
  
    """
    Función varianza():
        input: lista de datos(list), output: varianza de los datos(float)
        Calcula la varianza de un lista de números ingresada
        Esto mediante la sumatoria de la diferencia entre cada valor de la lista y su promedio al cuadrado dividido por el largo del conjunto

     Variables:
         -prom(float): Media aritmética de los datos calculada con la función mediaAritmetica()
         -datosMinusProm(list): Lista que contiene el resto de cada valor de la lista y su promedio al cuadrado
         -n(int): Cantidad de valores de la lista ingresada
         -varianza(float): Varianza de los datos ingresados. Calculada como la suma de cada valor de datosMinusProm dividido por n
    """
    
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

def desvEst(valores):
    
    """
     Función desvEst():
         input: lista de datos(list), output: desviación estándar de los datos(float)
         Calcula la desviación estándar de una lista de números ingresada
         Ya que la desviación estándar se puede calcular como la raiz de la varianza, se llama a la función varianza y se eleva a 0.5

     Variables:
         -varianza_lista(float): llamado a la funcion varianza()
    """
    
    lista = []
    for i in valores:   #Ciclo para deshacerse de los nans
        if math.isfinite(i):
            lista.append(i)
    
    varianza_lista = varianza(valores)
            
    return varianza_lista**0.5  #retorna la varianza elevada a 0.5

def percentil(valores):
    
    """
     Función percentil():
         input: lista de datos(list), output: lista con los percentiles 1-99(list)
         Retorna una lista con cada percentil de la lista de datos ingresada [1-99]
         Calcula cada percentil como n*k/100
            Donde:
                 k = número respectivo del percentil
                 n = largo del conjunto de datos

     Variables:
         -listaPercentiles(list): Lista que contiene cada percentil de la lista ingresada
             Ya que son 99 datos, el percentil correspondiente equivale a percentil-1
             ej: el percentil 78 en listaPercentiles se llama como listaPercentiles[77]
         -n(int): Cantidad de datos de la lista ingresada
         -percentil(int): Valor individual de un percentil, equivale a la posición del percentil en la lista
             Se calcula como n multiplicado al numero del percentil correspondiente dividido en 100
    """
    
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

def intercuartil(valores):
    
    """
     Función intercuartil():
         input: lista de datos(list), output: rango intercuartil de los datos(float)
         Devuelve el rango intercuartílico de una lista de datos, siendo este la diferencia entre su respectivo cuartil 3 y 1
         Ya que los cuartiles son equivalentes a los percentiles 25, 50 y 75, se utiliza la función percentil para ello

     Variables:
         -percentiles(list): Lista con los percentiles de la lista de números ingresada, obtenida con la función percentil()
         -rangoInter(list): Valor equivalente al rango intercuartílico, resto entre el cuartil 3 y el 1
             Utilizando percentiles: cuartil 3 = percentil 75, cuartil 1 = percentil 25
    """
    
    percentiles = percentil(valores)    #Se llama a la función percentiles()
    
    rangoInter = percentiles[74]-percentiles[24]
    
    return rangoInter   #Retorna el rango Intercuartílico
    
def MAD(valores):
    
    """
     Función MAD():
         input: lista de datos(list), output: mad de los datos(float)
         Calcula la desviación mediana absoluta de una lista de números ingresada
         Se calcula la mediana mediante la misma lógica usada en la función de mediana()
         Genera una lista donde se incluye cada el valor absoluto de la diferencia entre cada valor de la lista ingresada y su mediana
         Ordena la lista y, retorna la desviación mediana absoluta correspondiente en caso de si:
             Es impar, retorna el valor ubicado al medio de la lista
             Es par, retorna el promedio de la suma de los 2 valores ubicados al medio de la lista

     Variables:
         -n(int): Cantidad de datos en la lista
         -med(float): Mediana de la lista ingresada, calculada con la función mediana()
         -datosMinusMed(list): Lista que contiene el valor absoluto de la diferencia entre cada valor de la lista y su mediana
         -medio(int): Posición media de la lista, calculada con división entera
         -determinante(int): Variable que define mediante el módulo de n y 2 si la lista es par o no
         -MAD(int): Valor de la desviación mediana absoluta de la lista ingresada
    """
    
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
    
def coef(x, y):
    
    """
    Función coef():
        input: 2 lista de datos(list), output: coeficiente de relación entre ambas listas datos(float)
        Calcula el coeficiente de relación de Pearson entre 2 conjuntos de datos de igual longitud
        Esto mediante el cálculo de la fórmula del mismo
    
    Variables:
        -x_promx(float): promedio del conjunto en x
        -y_promy(float): promedio del conjunto en y
        -multixy(list): lista con el producto entre cada valor de ambas listas restado a su respectivo promedio
        -x_promx2(list): lista con el cuadrado de cada diferencia entre los valores de x y su promedio
        -y_promy2(list): lista con el cuadrado de cada diferencia entre los valores de y y su promedio
        -num(float): numerador de la fórmula del coeficiente de relación
        -den(float): denominador de la fórmula del coeficiente de relación
    """
    
    promx = mediaAritmetica(x)
    promy = mediaAritmetica(y)
    
    x_promx = []
    y_promy = []
    
    for i in range(len(x)):     #for para añadir los valores respectivos a x_promx e y_promx
        x_promx.append(x[i]-promx)
        y_promy.append(y[i]-promy)
    
    multixy = []
    x_promx2 = []
    y_promy2 = []
    
    for i in range(len(x)):     #for para añadir sus valores respectivos a x_promx2, y_promy2 y multixy
        x_promx2.append(x_promx[i]**2)
        y_promy2.append(y_promy[i]**2)
        multixy.append(x_promx[i]*y_promy[i])
        
    num = sum(multixy)
    den = ((sum(x_promx2))**0.5)*((sum(y_promy2))**0.5)
    
    return num/den  #Se retorna el cociente entre num y den con tal de obtener el coeficiente de relación
    
    
    
    
    
    
    
