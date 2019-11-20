lista_nombres=[]
lista_sexo=[]
cantSe = 0
cantSo = 0
lista_edad=[]
personas = 0

while True :
        nombre = input("Ingrese su nombre: ")
        if nombre == "":
            print("Error")
            nombre = input("Ingrese su nombre: ")
        else:
            lista_nombres.append(nombre)

        sexo = input("Ingrese su sexo: ")
        if sexo == "femenino":
            lista_sexo.append(sexo)
            cantSe = cantSe + 1
        elif sexo == "masculino":
            lista_sexo.append(sexo)
            cantSo = cantSo + 1
            
        edad = int(input("Ingrese su edad: "))
        if edad < 4 or edad > 17:
            print("No puede ingresar")
        else:
            lista_edad.append(edad)
            break

print("-----DATOS-----")
print("Ingresado: ", nombre)
print("Edad: ", edad)
print("Sexo: ", sexo)

print("-----Cantidad-----")
print("Personas Hombres: ",cantSo)
print("Personas Mujeres: ",cantSe)

print("-----Promedio de Edad-----")
print("Promedio es: ", lista_edad)