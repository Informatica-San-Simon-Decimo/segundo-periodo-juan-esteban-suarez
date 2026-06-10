print("=== SISTEMA DE ENTRADAS DE CINE ===")

while True:
    edad = input("Ingresa tu edad (o escribe 'salir'): ").lower()

    if edad == "salir":
        print("Gracias por visitarnos.")
        break

    edad = int(edad)

    if edad < 3:
        print("Tu entrada es GRATIS.")
    elif edad <= 12:
        print("Tu entrada cuesta $10.000.")
    else:
        print("Tu entrada cuesta $15.000.")
