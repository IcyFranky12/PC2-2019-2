import random
random.seed(100)

a = int(input("Ingrese un grado de la matriz entre 2 y 5: "))
while True:
    if a < 2 or a > 5:
        print("Error, colocar numero correcto")
        a = int(input("Ingrese un grado de la matriz entre 2 y 5: "))
    else:
        break
    

if a == 3:
    print("|", random.randint(1,100), random.randint(1,100), random.randint(1,100), "|")
    print("|", random.randint(1,100), random.randint(1,100), random.randint(1,100), "|")
    print("|", random.randint(1,100), random.randint(1,100), random.randint(1,100), "|")
