import random
b = random
a = int(input("Ingrese un grado de la matriz entre 2 y 5"))
while True:
    if a < 2 or a > 5:
        print("Error, colocar numero correcto")
        a = int(input("Ingrese un grado de la matriz entre 2 y 5"))
    else:
        break
    
b.random(0,100)
if a == 3:
    print("|", b, b, b, "|")
    print("|", b, b, b, "|")
    print("|", b, b, b, "|")