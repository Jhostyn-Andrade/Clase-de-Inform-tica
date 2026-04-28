"""nota=int(input("ingrese la nota: "))
if nota>89:
        print(f"{nota} es A")
else:
    if nota>79:
            print(f"{nota} es B")
    else:
        if nota>69:
                print(f"{nota}es C")
        else:
                print("Tu nota es D")"""

"""numero=int(input("ingrese un numero: "))
if numero ==0:
     print("el numero es cero")
else:
    if numero>0:
        if numero%2==0:
            print("el numero es par positivo")
        else:
            print("el numero es impar positivo")
    else:
        if numero%2==0:
            print("el numero es par negativo")
        else:
            print("el numero es impar negativo")"""

numero=int(input("ingrese un numero: "))
if numero>0 and numero%2==0:
     print("el numero es par positivio")
elif numero>0 and numero%2==1:
     print("el numero es impart positivo")
elif numero<0 and numero%2==0:
     print("el numero es par negativo")
elif numero<0 and numero%2==1:
     print("el numero es impar negativo")
else: print("el numero es cero")
