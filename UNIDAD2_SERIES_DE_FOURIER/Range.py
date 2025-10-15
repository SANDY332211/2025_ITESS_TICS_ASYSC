# ITESS TICS grupo 501
# Analisis de señales y sistemas de comunicacion
# Docente Fransisco Javier Montesillo Puente
# Programador Sandra Araceli Hernandez Muñoz
# 13/10/2025
#Funcion Range()

# range() normal
for i in range(5):
    print(i)
print()

# Uso de range con inicio y fin
for i in range(5, 10):
    print(i)
print()

# Uso de range con paso personalizado
for i in range(0, 10, 3):
    print(i)
print()

# Uso de range con paso negativo
for i in range(-10, -100, -30):
    print(i)
print()

# Iterar sobre los índices de una lista
a = ['Sandra', 'tenia', 'mucha', 'tarea']
for i in range(len(a)):
    print(i, a[i])
print()

# Convertir un objeto range a lista
print(list(range(5)))