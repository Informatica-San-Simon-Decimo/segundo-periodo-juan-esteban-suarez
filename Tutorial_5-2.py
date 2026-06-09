# Reto 2: Sin Empanadas

pedidos_sandwiches = [
    "empanada",
    "atún",
    "empanada",
    "pollo",
    "empanada",
    "jamón y queso",
    "vegetariano"
]

sandwiches_terminados = []

print("Lo sentimos, la cafetería se quedó sin empanadas.")

while "empanada" in pedidos_sandwiches:
    pedidos_sandwiches.remove("empanada")

while pedidos_sandwiches:
    sandwich_actual = pedidos_sandwiches.pop(0)
    print(f"Preparando tu sándwich de {sandwich_actual}...")
    sandwiches_terminados.append(sandwich_actual)

print("\nSándwiches terminados:")
for sandwich in sandwiches_terminados:
    print("-", sandwich)
