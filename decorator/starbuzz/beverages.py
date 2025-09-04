
from .beverage import Beverage

# --- Componentes Concretos ---

class HouseBlend(Beverage):
    """
    Café de la casa, un tipo específico de bebida.
    """
    def __init__(self) -> None:
        super().__init__("Café de la Casa")
    def get_cost(self) -> float:
        return 0.89
    
class DarkRoast(Beverage):
    """
    Café Dark Roast, un tipo específico de bebida.
    """
    def __init__(self) -> None:
        super().__init__("Café Dark Roast")
    def get_cost(self) -> float:
        return 0.99
    
class Decaf(Beverage):
    """
    Café Descafeinado, un tipo específico de bebida.
    """
    def __init__(self) -> None:
        super().__init__("Café Descafeinado")
    def get_cost(self) -> float:
        return 1.05

class Expresso(Beverage):
    """
    Café Espresso, un tipo específico de bebida.
    """
    def __init__(self) -> None:
        super().__init__("Espresso")
    def get_cost(self) -> float:
        return 1.99

# --- FIN Componentes Concretos ---