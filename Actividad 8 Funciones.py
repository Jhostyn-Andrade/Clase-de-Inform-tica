"""def generate_fulll_name():
    first_name="Jhostyn"
    last_name="Andrade"
    space=" "
    full_name=first_name+space+last_name
    print(full_name)
generate_fulll_name()"""
def mostrar_intruccion():
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
