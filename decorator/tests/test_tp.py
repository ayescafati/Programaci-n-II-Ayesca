# tests/test_tp.py
import pytest

from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy, Caramel

def money(x: float) -> str:
    return f"${x:.2f}"

def test_caramel_on_espresso_cost_and_description():
    b = Caramel(Espresso())
    assert b.get_description().endswith("Caramelo")
    assert pytest.approx(b.cost(), rel=1e-9) == 1.99 + 0.20

def test_double_mocha_whip_on_darkroast():
    b = DarkRoast()
    b = Mocha(Mocha(Whip(b)))  # order doesn't matter for cost
    # base 0.99 + mocha 0.20 + mocha 0.20 + whip 0.10 = 1.49
    assert pytest.approx(b.cost(), rel=1e-9) == 0.99 + 0.20 + 0.20 + 0.10
    assert "Mocha" in b.get_description() and "Crema" in b.get_description()

def test_soy_depends_on_size_venti():
    b = HouseBlend()
    b.set_size("venti")
    b = Soy(b)
    # base 0.89 + soy(venti 0.20)
    assert pytest.approx(b.cost(), rel=1e-9) == 0.89 + 0.20
    assert b.get_size() == "venti"

def test_triple_mocha_increases_cost():
    b = DarkRoast()
    b = Mocha(Mocha(Mocha(b)))
    assert pytest.approx(b.cost(), rel=1e-9) == 0.99 + 0.20*3

