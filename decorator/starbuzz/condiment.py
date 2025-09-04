# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod
from .beverage import Beverage
from typing import Literal

Size = Literal["tall", "grande", "venti"]

# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    # Encadenar tamaño a la bebida envuelta (no duplicamos estado)
    def set_size(self, size: Size) -> None:
        self._beverage.set_size(size)

    def get_size(self) -> Size:
        return self._beverage.get_size()

    def get_description(self) -> str:
        # Por defecto, delega la descripción
        return self._beverage.get_description()

    @abstractmethod
    def get_cost(self) -> float:
        ...

# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"
    def get_cost(self) -> float:
        return self._beverage.get_cost() + 0.10

class Mocha(CondimentDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"
    def get_cost(self) -> float:
        return self._beverage.get_cost() + 0.20

class Soy(CondimentDecorator):
    PRICES = {"tall": 0.10, "grande": 0.15, "venti": 0.20}
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"
    def get_cost(self) -> float:
        return self._beverage.get_cost() + self.PRICES[self.get_size()]

class WhippedCream(CondimentDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"
    def get_cost(self) -> float:
        return self._beverage.get_cost() + 0.10

# Alias como pide el TP
Whip = WhippedCream

class Caramel(CondimentDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramelo"
    def get_cost(self) -> float:
        return self._beverage.get_cost() + 0.20

class Chocolate(CondimentDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Chocolate"
    def get_cost(self) -> float:
        return self._beverage.get_cost() + 0.20
