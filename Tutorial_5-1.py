pedidos_sandwiches = [
    "atún",
    "pollo",
    "jamón y queso",
    "vegetariano",
    "pastrami"
]

sandwiches_terminados = []

while pedidos_sandwiches:
    sandwich_actual = pedidos_sandwiches.pop(0)
    print(f"Preparando tu sándwich de {sandwich_actual}...")
    sandwiches_terminados.append(sandwich_actual)

print("\nSándwiches terminados:")
for sandwich in sandwiches_terminados:
    print("-", sandwich)
