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
