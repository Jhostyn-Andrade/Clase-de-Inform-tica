# ======== PARTE A ============
# Respuesta 1:
# a) Los tipos de dato de la variable nombre: cadena (str)
# edad: entero (int)
# promedio: decimal (float)
# cursos: lista (list)
# b) Lo que mostraria la pantalla al ejecutar el programa es: <class "str">, 
# <class "int">, 
# <class "float">, 
# <class "list"> 
# y el número 5.
# c) len(nombre) cuenta la cantidad de caracteres que tiene la cadena, en este caso "Lucía" se mostraría el número 5

#Respuesta 2:
# a) La diferencia es que print() muestra datos, refleja el código impreso e input() el cual solicita datos al usuario para guardarlos en una variable.
# b) Puede darle error al no convertirlo a número float, porque input() siempre recibe texto str, y si se usa directamente para un cálculo es necesario la conversión a número.
# c) / es división decimal, // es división entera (sin decimales) y % es el residuo de la división.
# d) import sys; print(sys.version).
# e) help("keywords").

#======== PARTE B ============
#Respuestas 3:
ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * largo
costo = area * precio
print(f"Área total: {area}")
print(f"Costo estimado: {costo}")
# Respuestas Parte B:
# a) Los errores principales eran la falta de conversión de tipos ya que input da string y necesitabamos que sea un numero float, además el error al momento de imprimir con f-strings
# b) Porque convierte las entradas a números (float) y utiliza f-strings para imprimir resultados correctamente.

#Respuestas 4:
frase="Tecnología para todos"
print(frase.upper())
print(len(frase))
print("Python" in frase)
frase_nueva=frase.replace("Tecnología", "Programación")
print(frase_nueva.split())
