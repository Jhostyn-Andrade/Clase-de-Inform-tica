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
numers=[0,1,2,3,4,5]
for iterador in numers:
    print(f"Su itererador es {iterador}")

notas=[8,7,9,10]
suma=0
for nota in notas:
    suma=suma+nota
promedio=suma/len(notas)
print(promedio)
