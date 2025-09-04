# Re-exporta condimentos a nivel tope para usar: from condiments import ...

from starbuzz.condiment import (
    CondimentDecorator,
    Milk,
    Mocha,
    Soy,
    WhippedCream,
    Caramel,
    Chocolate,
)
Whip = WhippedCream
__all__ = ["Mocha", "Whip", "Soy", "Milk", "Caramel", "Chocolate"]
