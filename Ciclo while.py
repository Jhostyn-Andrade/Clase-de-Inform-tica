"""variabledecontrol= 8
while variabledecontrol<5:
    print(f"Esta es la vuelta {variabledecontrol}")
    variabledecontrol += 1
else:
    print("No se cumplió el ciclo")
print("Fin del programa") """

"""clave=""
while clave != "python123":
    clave=input("Ingrese la clave:")
print("Clave correcta. Acceso concedido.") """

"""opcion=""
while opcion!="c":
    print("a=Saludar")
    print("b=mostrar mensaje")
    print("c=salir")
    opcion=input("seleccione una opción: ")
    if opcion=="a":
        print("Hola, BIENVENIDO")
    elif opcion=="b":
        print("Estamos aprendiendo ciclo while")
    elif opcion=="c":
        print("programa terminado")
    else:
        print("funcion invalida")"""  

#CICLO FOR
"""numers=[0,1,2,3,4,5]
for iterador in numers:
    print(f"Su itererador es {iterador}")"""

"""notas=[8,7,9,10]
suma=0
for nota in notas:
    suma=suma+nota
promedio=suma/len(notas)
print(promedio)"""

"""notas=[8,7,9,10]
suma=0
contador=0
for nota in notas:
    suma=suma+nota
    contador+=1
promedio=suma/contador
print(f"el promedio de las notas es: {promedio}")

palabra="P y t h o n"
for iterador in palabra:
    print(iterador)


palabra=input("Ingrese una palabra:").lower()
vocales=0
for letra in palabra:
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        vocales=vocales+1
print(f"la cantidad de vocales es{vocales}")
print(f"El total de letras es: {len(palabra)}")
print(f"La cantidad de consonantes es: {len(palabra)-vocales}")"""

#FOR EN UN SET
"""it_companies={"Facebook","Google","Apple","Amazon","Facebook"}
for companies in it_companies:
    print(companies)"""

numbers=[5,2,5,6,7,8,2,3]
for number in numbers:
    if number==3:
        print("Numero encontrado")
        break
else:
    print("Numero no encontrado")

list=[5,2,5,6,7,8,2,3]
numbers=float(input("Ingrese un numero: "))
for i in list:
    if i==numbers:
        print("Numero encontrado")
        break  
print("Numero no encontrado")