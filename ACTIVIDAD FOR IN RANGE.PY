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
numero=int(input("Ingrese un número: "))
limiteinferior=int(input("Ingrese el limite inferior: "))
limitesuperior=int(input("Ingrese el limite superior: "))
for number in range(limiteinferior, limitesuperior+1):
    resultado=numero*number
    print(f"{numero} x {number} = {resultado}")