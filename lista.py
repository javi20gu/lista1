preguntar = "no".lower()
while preguntar == "no":
        nombre = input("Introduce tu nombre: ")
        for i in nombre:
                print(i.upper())
        preguntar = input("¿Quieres salirte del programa? si/no \n>>>").lower()
input("Pulse cualquier tecla para salir...")
