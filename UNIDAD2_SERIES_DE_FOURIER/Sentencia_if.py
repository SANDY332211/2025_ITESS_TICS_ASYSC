# ITESS TICS grupo 501
# Analisis de señales y sistemas de comunicacion
# Docente Fransisco Javier Montesillo Puente
# Programador Sandra Araceli Hernandez Muñoz
# 13/10/2025
#sentencia if

# Solicita al usuario ingresar un número entero
x = int(input("Ingresa un entero: "))

# Estructura condicional if, elif y else
if x < 0:
    x = 0
    print("Numero negativo cambiado a cero")
elif x == 0:
    print("Es igual a cero")
elif x == 1:
    print("Simple")
else:
    print("Es mayor a 1")
