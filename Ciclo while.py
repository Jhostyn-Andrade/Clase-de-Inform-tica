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

opcion=""
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
        print("funcion invalida")