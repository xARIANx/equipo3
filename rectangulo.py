ancho = 5
alto = 3

def calcular(Ancho = int(input("Ingrese el alto: ")), Alto = int(input("Ingrese el alto: "))):
    for i in  range (1,alto+1):
        for j in  range (1,ancho+1):
            print("*", end="")
        print(" ")

calcular()