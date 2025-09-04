
#### BLOQUE DE IMPORTACIONES ####
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Literal
#### FIN BLOQUE DE IMPORTACIONES ####

Size = Literal["tall", "grande", "venti"]

class Beverage(ABC):
    """
    Clase base para bebidas. Soporta tamaños y el patrón Decorator.
    """

    def __init__(self, description: str = "Bebida desconocida") -> None:
        self._description = description
        self._size: Size = "tall"  # tamaño DEFAULT!

    ##### API PÚBLICA  #####
    def get_description(self) -> str:
        return self._description

    def set_size(self, size: Size) -> None:
        if size not in ("tall", "grande", "venti"):
            raise ValueError("size debe ser 'tall', 'grande' o 'venti'")
        self._size = size

    def get_size(self) -> Size:
        return self._size

    @abstractmethod
    def get_cost(self) -> float:
        """Costo total de la bebida (incluye condimentos decorados)."""
        raise NotImplementedError
    # Alias compatible con main del TP
    def cost(self) -> float:
        return self.get_cost()

