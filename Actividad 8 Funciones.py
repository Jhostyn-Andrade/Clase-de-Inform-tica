"""def generate_fulll_name():
    first_name="Jhostyn"
    last_name="Andrade"
    space=" "
    full_name=first_name+space+last_name
    print(full_name)
generate_fulll_name()"""
"""def mostrar_intruccion():
    print("---Instrucciones del Programa---")
    print("1- INGRESE SU NOMBRE")
    print("2- Ingresa tu edad.")
    print("3- El programa mostrará un mensaje personalizado.")
def mostrar_despedida():
    print("Gracias por usar el programa.")

print("=== SISTEMA DE REGISTRO ===")
opcion = input('¿Deseas ver las instrucciones? si/no: ')
if opcion == "si":
    mostrar_instrucciones()
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print(f"Hola {nombre} tienes {edad} años.")
mostrar_despedida()

def mostrar_instrucciones():
    print("=== INSTRUCCIONES ===")
    print("Debe ingresar dos números.")
    print("El programa sumará esos números.")
    print("Puede escribir ayuda si no entiende qué hacer.")
print("=== SUMA DE DOS NÚMEROS ===")
mostrar_instrucciones()
dato = input("Ingrese el primer número o escriba ayuda: ")
if dato == "ayuda":
    mostrar_instrucciones()
    dato = input("Ingrese el primer número: ")
numero1 = int(dato)
numero2 = int(input("Ingrese el segundo número: "))
suma = numero1 + numero2
print(f"La suma es: {suma}")"""

"""def saludar(nombre):
    print(f"Hola {nombre}") 
saludar("Jhostyn")

def mostrar_estudiante(nombre, curso):
    print('=== DATOS DEL ESTUDIANTE ===')
    print(f'Nombre: {nombre}')
    print(f'Curso: {curso}')
nombre_usuario = input('Ingrese el nombre del estudiante: ')
curso_usuario = input('Ingrese el curso del estudiante: ')
mostrar_estudiante(nombre_usuario, curso_usuario)"""
# Actividad
"""def mostrar_estudiante(nombre, curso):
    print('=== DATOS DEL ESTUDIANTE ===')
    print(f'Nombre: {nombre}')
    print(f'Curso: {curso}')
def mensaje_final():
    print("Fin del programa")

total_estudiantes = int(input('¿Cuántos estudiantes desea ingresar?: '))
contador = 0

while contador < total_estudiantes:
    print(f"Este es el registro N{contador+1} de estudiante")
    nombre_usuario = input(f"Ingrese el nombre del estudiante {contador+1}: ")
    curso_usuario = input("Ingrese el curso del estudiante: ")
    mostrar_estudiante(nombre_usuario, curso_usuario)
    contador += 1

mensaje_final()"""

"""def promedio1(nombre,apellido,nota1,nota2,nota3):

    promedio=(nota1+nota2+nota3)/3


    print(f"el nombre es: {nombre}")

    print(f"el apellido es: {apellido}")

    print(f"el promedio es: {promedio}")

nombre=input("ingrese su nombre: ")

apellido=input("ingrese su apellido: ")

nota11=int(input("ingrese su nota 1: "))

nota12=int(input("ingrese su nota 2: "))

nota13=int(input("ingrese su nota 3: "))

promedio1(nombre,apellido,nota11,nota12,nota13)
 
def obtener_mensaje():

    mensaje = "Bienvenido al sistema"

    return mensaje

def generar_nombre_completo():

    nombre = input("Ingrese su nombre: ")

    apellido = input("Ingrese su apellido: ")

    espacio = " "

    nombre_completo = nombre+espacio+apellido

    return nombre_completo

print(f"{obtener_mensaje()} {generar_nombre_completo()}")"""
 
def calcular_total_producto(precio, cantidad):
    return precio * cantidad
print("SISTEMA DE COMPRA")
subt=0
for i in range(1, 4):
    print(f"Producto {i}")
    nombre=input("Ingrese el nombre del producto: ")
    precio=float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        print("Precio no válido. Debe ser mayor que 0.")
        precio=float(input("Ingrese nuevamente el precio del producto: "))
    cantidad=int(input("Ingrese la cantidad comprada: "))
    while cantidad <= 0:
        print("Cantidad no válida. Debe ser mayor que 0.")
        cantidad=int(input("Ingrese nuevamente la cantidad comprada: "))
    total_producto=calcular_total_producto(precio, cantidad)
    subt+=total_producto
    print(f"Producto registrado: {nombre}")
    print(f"Total del producto: ${total_producto}")
iva=subt*0.15
total_pagar=subt+iva
print(f"Subtotal de la compra: ${subt}")
print(f"IVA: ${iva}")
print(f"Total a pagar: ${total_pagar}")