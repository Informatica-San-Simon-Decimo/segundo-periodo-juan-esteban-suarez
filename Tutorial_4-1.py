print("=== CREADOR DE PIZZA ===")

while True:
    ingrediente = input("Ingresa un ingrediente (o escribe 'salir'): ").lower()

    if ingrediente == "salir":
        print("Tu pizza está lista. ¡Buen provecho!")
        break

    print(f"Añadiré {ingrediente} a tu pizza.")
