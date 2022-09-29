Bandera = ""
number = 1
contadorFallos = 0

while (number !=0):
    user = input("digitar usuario")
    password = input("digitar contra")
    if(user == "admin" and password == "123"):
        Bandera = True
        print("autenticacion exitosa")
        break
    if(Bandera != True):
        contadorFallos += 1
        if(contadorFallos == 1):
            print(f"Has fallado {contadorFallos} veces la autenticacion")
            print(f"Fallo autenticacion")
        else:
            print(f"Has fallado {contadorFallos} veces la autenticacion")
            print(f"Fallo autenticacion")
