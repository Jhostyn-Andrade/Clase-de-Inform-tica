""" Nombre: Jhostyn Andrade
Fecha: 15/4/2026
Titulo: Variables de python"""

#texto(str) en comillas para no cálculos
nombre = "Stefany"
apellido ="Ruano"
nombreCompleto="Noam Zukrberg"
pais="Estados Unidos"
ciudad="New York"

#numeros(int) no llevan comillas
edad=18
año=2000

#booleanos(bool)
estaCasado= False  
esVerdadero= True
luzEncendida= False
 
goat, colegio, color="Beto", "Ism", "blanco"
# %%
print(type(nombre))
print(type(apellido))
print(type(nombreCompleto))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(estaCasado))
print(type(esVerdadero))
print(type(luzEncendida))

# len():calcula la longitud
print(len(nombre))
print(len(nombre)>len(apellido))

numeroUno = 5
numeroDos = 4

total = numeroUno + numeroDos
print(total)

diferencia = numeroUno - numeroDos
print(diferencia)

producto=numeroUno*numeroDos
print(producto)

division=numeroUno/numeroDos
print(division)

#El residuo es lo que sobra después de una división.
residuo= numeroDos%numeroUno
print(residuo)

potencia=numeroUno**numeroDos
print(potencia)

# // es para diviones enteras
divisionEntera=numeroUno//numeroDos
print(divisionEntera)

ratio=30
areaCirculo=3.14*30**2
print(areaCirculo)

circunferenciaCirculo=2*3.14*ratio
print(circunferenciaCirculo)

# input() sirve para pedir datos al usuario
#float() convierte un valor a número con decimales

radio= float(input("ingrese el valor del ratio: "))
areaCirculo=3.14*radio**2
print(areaCirculo)

#int() sirve para convertir algo en número entero
nombre=input("ingrese su nombre: ")
apellido=input("inrgese su apellido: ")
pais= input("ingrese pais de nacimiento: ")
edad= int(input("ingrese su edad: "))

#palabras resevadas:Tú NO puedes usarlas como nombres de variables
help('keywords')