"""
creamos un archivo 
guardamos en la carpeta del reposistorio 
con la extencion .py
uso de numeros aleatorios
"""

"""
#importamos la libreria randint
from random import randint           
aleatorio=randint(1,20)            #creamos una variable y generamos un numero aleatorios entro 0, 20
print(aleatorio)                   #imprimimos el numero generando 
"""
"""
ejercicio 
escribir una funcion sorteo() que reciba una lista de 
participantes, y elejir a uno de los participantes
 aleatoriamente, y retornar esa persona elejida
 desafio: no volver a retornar una persona ya sorteada 
 """




from random import randint          #importamos la funcion de la libreria randint
def sorteo(ganadores):              #definimos una funcion
    participantes=len(lista)        #utilizamos len para saber la cantidad de personas que haz en la lista y guardamos en una variable 
    sorteo=randint(0, participantes-1)      #seleccionamos un elemnto de la lista y guardamos en la variable  
    return lista[sorteo]                    #retornamos la lista 

lista=["Lucas", "Sara", "Paula", "Kami"]   #creamos una lista con los participantes 
ganar=sorteo("ganadores")                        #llamamos a la funcion y lo guardamos en una vairable 
print(ganar)

""""
from random import randint
def sorteo(ganadores):
    participantes=len(lista)
    sorteo=randint(0, participantes-1)
    return lista[sorteo]
    print(lista[sorteo]) 
lista=["Lucas", "Sara", "Paula", "Kami"]
sorteo(lista)
"""