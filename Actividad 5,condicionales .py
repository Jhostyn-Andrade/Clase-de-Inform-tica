nota=int(input("ingrese la nota: "))
if nota>100:
    print(f"{nota} muy bien eres el mejor") 
else:
    if nota>89:
        print(f"{nota} es A")
    else:
        if nota>79:
            print(f"{nota} es B")
        else:
            if nota>69:
                print(f"{nota}es C")
            else:
                print("Tu nota es D")