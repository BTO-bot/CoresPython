#Funciones intermedias (Core)


#1. Actualizar valores en diccionarios y listas.

# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
# En ciudades, cambia “Cancún” por “Monterrey”
# En las coordenadas, cambia el valor de “latitud” por 9.9355431

matriz = [ [10, 15, 20], [6, 7, 14] ]

cantantes = [

   {"nombre": "Enrique Martin Morales", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Monterrey"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

   {"latitud": 8.2588997, "longitud": -9.9355431}

]

#2. Iterar a través de una lista de diccionarios.

# Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios
# y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente.
# Por ejemplo:

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

#Creacion de la funcion:
def iterarDiccionario(lista):
    for diccionario in lista:
        resultado = ', '.join([f"{llave} - {valor}" for llave, valor in diccionario.items()])
        print(resultado)

# Lista de cantantes:
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]


#Imprime "nombre": "Ricky Martin", "pais": "Puerto Rico" (está bien si lo imprime en líneas separadas)

#BONUS: Que aparezcan en este formato:

#nombre - Ricky Martin, pais - Puerto Rico

#nombre - Chayanne, pais - Puerto Rico

#nombre - José José, pais - México

#nombre - Juan Luis Guerra, pais - República Dominicana

print() #Espacio

print("Iterar a través de una lista de diccionarios: ") #Titulo

print() #Espacio

#Llamada de la funcion:
iterarDiccionario(cantantes)

#3. Obtener valores de una lista de diccionarios.

# Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios.
# La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. 
# Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:

#Ricky Martin

#Chayanne

#José José

#Juan Luis Guerra


#Otro ejemplo: iterarDiccionario2(“pais”, cantantes) debe de imprimir:

#Puerto Rico

#Puerto Rico

#México

#República Dominicana

#Funcion IterarDiccionario2:
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# La lista de los diccionarios de cantantes:
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

print() #Espacio 

print("Obtener valores de una lista de diccionarios: ") #Titulo

print() #Espacio

print("Nombre de los cantantes:")
iterarDiccionario2("nombre", cantantes)

print("\nPais de los cantantes:")
iterarDiccionario2("pais", cantantes)


#4. Iterar a través de un diccionario con valores de lista

# Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. 
# La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.
# Por ejemplo:

# costa_rica = {

#    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

#    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

# }

# #imprime:

# 4 CIUDADES

# San José

# Limón

# Cartago

# Puntarenas

# 5 COMIDAS

# gallo pinto

# casado

# tamales

# chifrijo

# olla de carne

print() #Espacio

#Creacion de funcion:
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        
        print(f"{len(lista)} {clave.upper()}")
        
        for valor in lista:
            print(valor)
        
        print() #Espacio

# Emulando el ejemplo:
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print() #Espacio

print("Iterar a través de un diccionario con valores de lista: ") #Titulo

print() #Espacio

#Llamado de la funcion:
imprimirInformacion(costa_rica)
