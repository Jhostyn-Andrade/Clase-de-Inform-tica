#  Nivel 1: Operaciones básicas

texto = "Programación Para Todos"  
print(f"Contenido: {texto}")        
print(f"Longitud: {len(texto)}")   


# Nivel 2: Transformación de texto

print(f"Mayúsculas: {texto.upper()}")      # 4. Mayúsculas
print(f"Minúsculas: {texto.lower()}")      # 5. Minúsculas
print(f"Formato Título: {texto.title()}")  # 6. Cada palabra inicia en mayúscula
print(f"Capitalize: {texto.capitalize()}") # 7. Solo la primera letra de la frase


#  Nivel 3: Búsqueda y verificación

print(f"¿Empieza con Programación?: {texto.startswith("Programación")}")
print(texto[0:12]) 
print(f"¿Termina con Todos?: {texto.endswith("Todos")}")
print(texto[-5:])                 
print(f"Posición de Para: {texto.find("Para")}")                         
print(f"¿Contiene Python?: {'Python' in texto}")                        


#  Nivel 4: Manipulación

nuevo_texto = texto.replace("Programación", "Python") # 12. Reemplazar
print(f"Reemplazo: {nuevo_texto}")
gg=texto.replace("Todos","Elian")
print(gg)

palabras = texto.split() # 13. Dividir en una lista
print(f"Split: {palabras}")

union = " - ".join(palabras) # 14. Unir con guiones
print(f"Unión: {union}")


#  Nivel 5: Índices

print(f"Primer carácter: {texto[0]}")  # 15. Índice 0
print(f"Último carácter: {texto[-1]}") # 16. Índice -1
print(f"Carácter posición 5: {texto[5]}") # 17. (Letra 'a')


#  Nivel 6: Aplicación simple

nombre_completo = "Jhostyn Andrade"
print(f"Hola, mi nombre es {nombre_completo}")

nombre="Jhostyn"
apellido="Andrade"
primera_n=nombre[0]
primera_a=apellido[0]
print(f"Mi Acrónimo: {primera_n+primera_a}")

#===== PARTE A =====
# Respuesta 1:
# a) nombre: str (cadena), edad: int (entero), promedio: float (decimal), cursos: list (lista)[cite: 30, 31, 32, 33, 40].
# b) Mostraría: <class 'str'>, <class 'int'>, <class 'float'>, <class 'list'> y el número 5[cite: 34, 35, 36, 37, 38, 41].
# c) len(nombre) cuenta la cantidad de caracteres que tiene la cadena "Lucía" (en este caso, 5)[cite: 42].

# Respuesta 2:
# a) print() muestra datos en consola; input() solicita datos al usuario para guardarlos en una variable[cite: 45].
# b) Porque input() siempre recibe texto (str). Si se usa en cálculos sin convertirlo a número (int/float), da error[cite: 46].
# c) / es división decimal, // es división entera (sin decimales) y % es el residuo de la división[cite: 47].
# d) import sys; print(sys.version)[cite: 48].
# e) help("keywords")[cite: 49].

# ===== PARTE B =====
# Código corregido [cite: 12, 52]
ancho = float(input("Ingrese el ancho del terreno: ")) [cite: 53]
largo = float(input("Ingrese el largo del terreno: ")) [cite: 54]
precio = float(input("Ingrese el precio por metro cuadrado: ")) [cite: 56]

area = ancho * largo [cite: 57]
costo = area * precio [cite: 58]

print(f"Área total: {area}") [cite: 59]
print(f"Costo estimado: {costo}") [cite: 60]

# Respuestas adicionales Parte B:
# a) Errores: Falta de conversión de tipos (input da str), error de sintaxis en 'costo', e intentar concatenar str con float[cite: 62].
# b) Porque convierte las entradas a números (float) y utiliza f-strings para imprimir resultados correctamente[cite: 63].

# 4. Construcción breve [cite: 64]
frase = "Tecnología para todos" [cite: 66]
print(frase.upper()) [cite: 67]
print(len(frase)) [cite: 68]
print("Python" in frase) [cite: 69]
frase_modificada = frase.replace("Tecnología", "Programación") [cite: 70]
print(frase_modificada.split()) [cite: 71]

#===== PARTE C =====
# Programa integrador [cite: 15, 72]

# 1. Solicitud de datos [cite: 75, 76]
nombre = input("Nombre: ")
apellido = input("Apellido: ")
pais = input("País: ")
ancho_p = float(input("Ancho de la pared: "))
alto_p = float(input("Alto de la pared: "))
precio_m2 = float(input("Precio por metro cuadrado: "))

# Cálculos [cite: 78]
area_pared = ancho_p * alto_p
costo_total = area_pared * precio_m2
nombre_completo = f"{nombre} {apellido}" [cite: 79]

# 2. Reporte final con f-strings [cite: 80, 83]
print("\n--- REPORTE FINAL ---")
print(f"Nombre completo: {nombre_completo}") [cite: 82]
print(f"País: {pais}") [cite: 82]
print(f"Área calculada: {area_pared} m2") [cite: 82]
print(f"Costo total estimado: ${costo_total}") [cite: 82]

# 3. Información adicional [cite: 84]
print(f"Nombre en mayúsculas: {nombre_completo.upper()}") [cite: 87]
print(f"Longitud del nombre: {len(nombre_completo)}") [cite: 88]
print(f"¿Contiene la letra 'a'?: {'a' in nombre_completo.lower()}") [cite: 89]
print(f"¿El costo es mayor a 100?: {costo_total > 100}") [cite: 90]

