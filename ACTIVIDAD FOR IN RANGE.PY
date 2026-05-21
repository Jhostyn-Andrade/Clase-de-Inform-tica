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
numero = int(input("Ingrese un número: "))
for x in range(2,11,2):
    print(f"{numero}x{x} = {numero*2} ")
