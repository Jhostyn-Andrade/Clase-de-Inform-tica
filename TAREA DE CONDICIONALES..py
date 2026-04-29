#Ejercicio 1
edad=int(input("ingrese su edad: "))
if edad>=18:
    print("Eres mayor de edad")
else:
    edadFaltante=18-edad
    print(f"Te faltan {edadFaltante} años para ser mayor de edad")


my_age = 25
your_age = int(input("Ingrese su edad: "))

if my_age > your_age:
    diferencia = my_age - your_age
    print(f"Yo soy {diferencia} {"año" if diferencia == 1 else "años"} mayor que tú.")
elif your_age > my_age:
    diferencia = your_age - my_age
    print(f"Eres {diferencia} {"año" if diferencia == 1 else "años"} mayor que yo.")
else:
    print("Tenemos la misma edad.")


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")


puntaje = int(input("Ingrese el puntaje (0-100): "))
if 90 <= puntaje <= 100:
    print("Calificación: A")
elif 80 <= puntaje <= 89:
    print("Calificación: B")
elif 70 <= puntaje <= 79:
    print("Calificación: C")
elif 60 <= puntaje <= 69:
    print("Calificación: D")
else:
    print("Calificación: F")


mes = input("Ingrese el mes: ").capitalize()
if mes in ["Septiembre", "Octubre", "Noviembre"]:
    print("La estación es Otoño")
elif mes in ["Diciembre", "Enero", "Febrero"]:
    print("La estación es Invierno")
elif mes in ["Marzo", "Abril", "Mayo"]:
    print("La estación es Primavera")
elif mes in ["Junio", "Julio", "Agosto"]:
    print("La estación es Verano")
else:
    print("Mes no reconocido.")


fruits = ['banana', 'orange', 'mango', 'lemon']
nueva_fruta = input("Ingrese una fruta: ").lower()
if nueva_fruta in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(nueva_fruta)
    print("Nueva lista:", fruits)

edad = int(input("Ingrese la edad del estudiante: "))
promedio = float(input("Ingrese el promedio académico: "))
tiene_permiso = input("¿Cuenta con permiso de sus padres? (si/no): ").lower() == "si"
if edad < 12:
    if tiene_permiso:
        print("Puede ingresar con supervisión")
    else:
        print("No puede ingresar a la plataforma")
elif 12 <= edad <= 17:
    if promedio >= 8.5:
        print("Acceso completo a cursos avanzados")
    elif 7 <= promedio < 8.5:
        print("Acceso a cursos intermedios")
    else:
        print("Acceso solo a cursos básicos")
else: # 18 años o más
    print("Acceso libre a la plataforma")
