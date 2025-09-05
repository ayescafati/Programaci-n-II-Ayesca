# Starbuzz — Patrón Decorator (Python)

Trabajo práctico de programación orientada a objetos . El repositorio implementa el ejemplo **Starbuzz Coffee** para ejercitar el patrón **Decorator** en Python, con foco en composición, delegación y extensión sin modificar clases existentes.

## Alcance del trabajo

### Nivel 1

* **Condimento nuevo: `Caramel` (Caramelo)** con costo fijo `0.20`.
* **Dobles / triples**: se puede encadenar el mismo decorador (p. ej., `Mocha(Mocha(...))`).
* Se muestra en `main.py` (Pedidos 4 y 5).

### Nivel 2 — Tamaños

* `Beverage` define `set_size(size)` / `get_size()` con tamaños `tall | grande | venti`.
* `Soy` cobra según tamaño: `0.10`, `0.15`, `0.20`.
* Los decoradores **no duplican estado**: consultan y propagan el tamaño del componente envuelto (composición + delegación).
* Demo en `main.py`: *HouseBlend venti + Soy* (Pedido 6).

### Nivel 3 — Usabilidad y pruebas

* **Builder** (`builder.py`): permite armar bebidas por nombre y lista de condimentos.
* **PrettyDescription**: transforma `"Mocha, Mocha, Whip"` en **"Double Mocha, Whip"** únicamente a nivel de **texto** (el costo no cambia).
* **Pruebas** (`tests/test_tp.py`, con `pytest`): validan costos y descripciones (Caramel, dobles, triple, tamaños).

## Decisiones de diseño

* **Propagación de tamaño**: los decoradores heredan de `Beverage` y **delegan** `get_size()` / `set_size()` al componente interno. Evitamos estados duplicados y posibles inconsistencias.
* **OCP (Open/Closed Principle)**: para agregar un condimento, definimos **un nuevo decorador**; no se tocan `Beverage` ni las bebidas base.
* **Programar contra la abstracción**: el cliente interactúa con `Beverage` (y no con tipos concretos), preservando el polimorfismo cuando se encadenan decoradores.

## Extensión I/O (bonus)

* En `starbuzz/io_decorator.py` se incluye  TextoMinusculas, que convierte a minúsculas al leer de un stream de texto.

## UML

Diagrama:
[https://drive.google.com/file/d/11wZz4W07LpIPLPk9xc-LduBVV8-GcXQM/view?usp=sharing](https://drive.google.com/file/d/11wZz4W07LpIPLPk9xc-LduBVV8-GcXQM/view?usp=sharing)

## Cómo correr

```bash
python main.py
pytest -q
```

> Probado con Python 3.x. El builder y PrettyDescription se demuestran en los pedidos 7 y 8 del `main.py`.

