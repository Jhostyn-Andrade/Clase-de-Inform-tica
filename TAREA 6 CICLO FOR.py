#EJERCICIO LISTA
notas=[8.5, 6.0, 9.0, 7.0, 5.5]
suma=0
aprobaron=0
reprobaron=0
for i in notas:
    suma=suma+i
    if i>=7:
        aprobaron=aprobaron+1
    else:
        reprobaron=reprobaron+1
promedio=suma/len(notas)
print(f"La suma total de las notas es: {suma}")
print(f"El promedio del curso es: {promedio}")
print(f"Aprobaron: {aprobaron} estudiantes")
print(f"Reprobaron {reprobaron} estudiantes")


