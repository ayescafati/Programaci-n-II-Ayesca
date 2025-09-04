
#### BLOQUE DE IMPORTACIONES ####
from typing import Iterable, Callable, Dict, List
from .beverage import Beverage, Size
from . import beverages as B
from . import condiments as C
#### FIN BLOQUE DE IMPORTACIONES ####

# Mapeos de nombres a clases concretas
BASES: Dict[str, Callable[[], Beverage]] = {
    "espresso": B.Expresso,
    "expresso": B.Expresso,   
    "darkroast": B.DarkRoast,
    "houseblend": B.HouseBlend,
    "decaf": B.Decaf,
}

CONDIMENTS: Dict[str, Callable[[Beverage], Beverage]] = {
    "milk": C.Milk,
    "soy": C.Soy,
    "whip": C.WhippedCream,
    "crema": C.WhippedCream,
    "chocolate": C.Chocolate,
    "mocha": C.Mocha,
    "caramel": C.Caramel,
    "caramelo": C.Caramel,
}

def build_beverage(base: str, size: Size, condiments: Iterable[str]) -> Beverage:
    """
    Construye una bebida decorada a partir de nombres de base y condimentos.
    """
    key = base.lower().replace(" ", "")
    if key not in BASES:
        raise ValueError(f"Base desconocida: {base}")
    drink = BASES[key]()
    drink.set_size(size)
    for c in condiments:
        ck = c.lower().replace(" ", "")
        if ck not in CONDIMENTS:
            raise ValueError(f"Condimento desconocido: {c}")
        drink = CONDIMENTS[ck](drink)
    # Asegurar tamaño propagado a toda la cadena!!!
    drink.set_size(size)
    return drink

# Decorador para que la salida sea más bonita, modifica la descripción para compactar repeticiones
class PrettyDescription(Beverage):
    _MULTIPLIERS = {2: "Double", 3: "Triple"}

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def set_size(self, size: Size) -> None:
        self._beverage.set_size(size)

    def get_size(self) -> Size:
        return self._beverage.get_size()

    def get_cost(self) -> float:
        return self._beverage.get_cost()

    def get_description(self) -> str:
        # Agrupamos términos iguales consecutivos. P.e.: "Mocha, Mocha, Whip" se transforma en "Double Mocha, Whip"
        parts: List[str] = [p.strip() for p in self._beverage.get_description().split(",")]
        if not parts:
            return ""

        base = parts[0]  
        rest = parts[1:]

        pretty: List[str] = [base]
        i = 0
        while i < len(rest):
            j = i + 1
            while j < len(rest) and rest[j] == rest[i]:
                j += 1
            count = j - i
            word = rest[i]
            if count in self._MULTIPLIERS:
                pretty.append(f"{self._MULTIPLIERS[count]} {word}")
            elif count > 3:
                pretty.append(f"{count}x {word}")
            else:
                pretty.extend([word] * count)
            i = j
        return ", ".join([p.strip() for p in pretty if p.strip()])
