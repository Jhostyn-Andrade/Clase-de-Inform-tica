#FOR CON INICIO
"""suma=0
while True:
    i=int(input("Ingrese cuantas notas quere:"))
    if i>=2:
            for x in range(i):
                    nota=int(input(f"Ingrese la nota {x+1} : "))
                    suma=suma+nota
            break
    else:
            print(f"No se puede sacar el promedio de {i} nota")
promedio=suma/i
print(promedio) """
#fOR IN RANGE INICIO Y FIN
"""numero=int(input("Ingrese un número: "))
limiteinferior=int(input("Ingrese el limite inferior: "))
limitesuperior=int(input("Ingrese el limite superior: "))
for number in range(limiteinferior, limitesuperior+1):
    resultado=numero*number
    print(f"{numero} x {number} = {resultado}")"""
"""suma=0
cantidad=0
notas=[5,8,9,7,10]
for i in range(1,4):
    suma=suma+notas[i]
    cantidad=cantidad+1
promedio=suma/cantidad
print(f"El promedio de las notas es: {promedio}") """
# Programa para generar una tabla de multiplicar
# usando solo los factores pares: 2, 4, 6, 8 y 10
"""numero = int(input("Ingrese un número: "))
for x in range(2,11,2):
    print(f"{numero}x{x} = {numero*2} ")"""
#For anidado
# Asignar estudiantes a los puestos de un laboratorio
# El laboratorio tiene 3 filas y 4 computadoras por cada fila
# Ciclo externo: recorre las filas del laboratorio
# range(1, 4) genera los valores 1, 2 y 3
for fila in range(1, 4):
    # Ciclo interno: recorre las computadoras de cada fila
    # range(1, 5) genera los valores 1, 2, 3 y 4
    for computadora in range(1, 5):
        # Solicita el nombre del estudiante que será asignado al puesto actual
        nombre = input("Ingrese el nombre del estudiante: ")
        # Muestra el nombre del estudiante y el puesto asignado
        print(f"{nombre} ud esta asignado a FILA {fila}, computadora {computadora}")
    # Este mensaje se muestra cuando termina la asignación de una fila completa
    print(f"Fin de la fila{fila}")
