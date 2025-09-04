
#### BLOQUE DE IMPORTACIONES ####
from typing import TextIO
#### FIN BLOQUE DE IMPORTACIONES ####

class TextoMinusculas:
    """
    Wrapper de lectura que convierte a minúsculas todo lo que se lee
    """
    def __init__(self, wrapped: TextIO) -> None:
        self._wrapped = wrapped

    def read(self, *args, **kwargs) -> str:
        return self._wrapped.read(*args, **kwargs).lower()

    def readline(self, *args, **kwargs) -> str:
        return self._wrapped.readline(*args, **kwargs).lower()

    def __iter__(self):
        for line in self._wrapped:
            yield line.lower()

    def close(self) -> None:
        return self._wrapped.close()
