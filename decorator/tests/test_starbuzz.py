import sys
from pathlib import Path

from starbuzz.beverages import Expresso, DarkRoast, HouseBlend
from starbuzz.condiments import Mocha, WhippedCream, Soy, Caramel
from starbuzz.builder import build_beverage, PrettyDescription


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def test_simple_espresso_cost():
    p = Expresso()
    assert round(p.get_cost(), 2) == 1.99
    assert "Espresso" in p.get_description()

def test_double_mocha_whip_darkroast():
    p = WhippedCream(Mocha(Mocha(DarkRoast())))
   
    assert round(p.get_cost(), 2) == 1.49 # 0.99 + 0.20 + 0.20 + 0.10 = 1.49
    assert p.get_description().startswith("Café Dark Roast")

def test_size_affects_soy():
    p = HouseBlend()
    p.set_size("venti")
    p = Soy(p)  # Soy depende del tamaño del envuelto
   
    assert round(p.get_cost(), 2) == 1.09 # 0.89 + 0.20 = 1.09

def test_builder_and_pretty():
    p = build_beverage("houseblend", "grande", ["mocha", "mocha", "whip"])
    pp = PrettyDescription(p)
    assert "Double Mocha" in pp.get_description()

    assert round(pp.get_cost(), 2) == 1.39 # 0.89 + 0.20 + 0.20 + 0.10 = 1.39 

def test_caramel_fixed_price():
    p = Caramel(Expresso())
    
    assert round(p.get_cost(), 2) == 2.19 # 1.99 + 0.20 = 2.19





