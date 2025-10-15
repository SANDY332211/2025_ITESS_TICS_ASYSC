# ITESS TICS grupo 501
# Analisis de señales y sistemas de comunicacion
# Docente Fransisco Javier Montesillo Puente
# Programador Sandra Araceli Hernandez Muñoz
# 13/10/2025

# Listas 
#Una lista en Python se define usando corchetes [ ]  
cuadrados = [1, 4, 9, 16, 25]
print(cuadrados)
print()

# Acceder a elementos por índice
print(cuadrados[0]) #índice 0 es el primer elemento
print(cuadrados[-1]) # índice -1 es el último elemento
print(cuadrados[-3:]) #rebanada que retorna los ultimos 3 elementos 
print()

# Crear una copia de la lista, devuleve una copia superfisial de toda la lista 
nueva_lista = cuadrados[:]
print(nueva_lista)
print()

#Unir o concatenar dos listas 
nueva_lista = cuadrados + [36, 49, 64, 81, 100]
print(nueva_lista)
print()

#modificar elementos de una lista 
# Lista con un error
cubos = [1, 8, 27, 65, 125]
print("Antes:", cubos)
# Corregir el valor erróneo en el elemento 3
cubos[3] = 64
print("Después:", cubos)
print()


#Agregar elementos al final (append)
cubos.append(216)    
cubos.append(7 ** 3) 
print(cubos)
print()


#Reemplazar y eliminar elementos con slices
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original:", letras)
# Reemplazar algunos valores
letras[2:5] = ['C', 'D', 'E']
print("Reemplazado:", letras)
# Eliminar esos valores
letras[2:5] = []
print("Eliminado:", letras)
# Vaciar toda la lista
letras[:] = []
print("Lista vacía:", letras)
print()


#Calcular la longitud de una lista con len
letras = ['a', 'b', 'c', 'd']
print(len(letras))
print()


#Listas anidadas
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)        # muestra la lista anidada
print(x[0])     # muestra la primera sublista
print(x[0][1])  # muestra el segundo elemento de la primera sublista


