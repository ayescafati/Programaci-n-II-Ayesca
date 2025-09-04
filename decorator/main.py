# main.py
# Script principal para probar el patrón Decorator.
# Incluye los pedidos requeridos por el TP (niveles 1-3).

from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy, Caramel
from starbuzz.builder import build_beverage, PrettyDescription

def money(x: float) -> str:
    return f"${x:.2f}"

def main():
    """
    Función principal que simula la preparación de cafés en Starbuzz.
    """
    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1 (Nivel 1): Un Espresso simple, sin condimentos.
    beverage1 = Espresso()
    print(f"Pedido 1: {beverage1.get_description()} {money(beverage1.cost())}")

    # Pedido 2 (Nivel 1 dobles): Un DarkRoast con doble Mocha y Crema.
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)  # Envolvemos con el primer Mocha
    beverage2 = Mocha(beverage2)  # Envolvemos con el segundo Mocha
    beverage2 = Whip(beverage2)   # Envolvemos con Crema
    print(f"Pedido 2: {beverage2.get_description()} {money(beverage2.cost())}")

    # Pedido 3 (Nivel 1 + 2 ejemplo sin tamaño): Un HouseBlend con Soja, Mocha y Crema.
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Pedido 3: {beverage3.get_description()} {money(beverage3.cost())}")

    # Pedido 4 (Nivel 1 Caramel): Espresso con Caramelo.
    beverage4 = Caramel(Espresso())
    print(f"Pedido 4: {beverage4.get_description()} {money(beverage4.cost())}")

    # Pedido 5 (Nivel 1 triples): DarkRoast con triple Mocha.
    beverage5 = DarkRoast()
    beverage5 = Mocha(Mocha(Mocha(beverage5)))
    print(f"Pedido 5: {beverage5.get_description()} {money(beverage5.cost())}")

    # Pedido 6 (Nivel 2 tamaños): HouseBlend Venti con Soy dependiente del tamaño.
    beverage6 = HouseBlend()
    beverage6.set_size("venti")
    beverage6 = Soy(beverage6)
    print(f"Pedido 6: {beverage6.get_description()} {money(beverage6.cost())}  (size={beverage6.get_size()})")



    # Pedido 7 (builder): HouseBlend grande con Soja, Mocha y Whip
    # Demostramos el builder; no hay condimentos repetidos, por ello pretty no comprime nada.
    beverage7 = build_beverage(base="houseblend", size="grande", condiments=["soy", "mocha", "whip"])
    pretty7 = PrettyDescription(beverage7)  # sólo cambia el texto (presentación); el costo es el mismo
    print(f"Pedido 7 (builder): {pretty7.get_description()} ${pretty7.get_cost():.2f}")


    # Pedido 8 (pretty print): DarkRoast con mocha X2 + whip
    # Armado manual para mostrar que PrettyDescription comprime duplicados a 'Double Mocha' (no cambia el costo).
    raw8 = DarkRoast()
    raw8 = Mocha(Mocha(raw8))  # Mocha duplicado
    raw8 = Whip(raw8)
    print(f"Pedido 8 (raw): {raw8.get_description()} ${raw8.cost():.2f} (antes)")
    pretty8 = PrettyDescription(raw8)  # afecta la descripción solamente, no al cálculo
    print(f"Pedido 8 (pretty): {pretty8.get_description()} ${pretty8.get_cost():.2f} (después :D)")


if __name__ == "__main__":
    main()
