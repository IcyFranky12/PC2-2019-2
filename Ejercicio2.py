letra = 0

a = input("Coloque texto: ")
b = input("Coloque letra a copiar: ")

def contarletra(a, b):
    contador = 0
    for algo in a.lower():
        if algo == b.lower():
            contador = contador + 1
    return contador

contadorMas = contarletra(a,b)
print(contadorMas)

    
    
    