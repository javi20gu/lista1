preguntar = "no".lower()
while preguntar == "no":
        nombre = input("Introduce tu nombre: ")
        for i in nombre:
                print(i.upper())
        print("Gracias por utilizarlo")
        preguntar = input("¿Quieres salirte del programa? si/no \n>>>").lower()
input("Pulse cualquier tecla para salir...")
