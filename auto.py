from abc import ABC, abstractmethod

class Auto(ABC):
    """
    Absztrakt ősosztály minden autótípus számára.
    A közös tulajdonságokat és az info() metódus kötelező implementálását írja elő.
    """

    def __init__(self, rendszam: str, tipus: str, berleti_dij: int):
        self._rendszam = rendszam
        self._tipus = tipus
        self._berleti_dij = berleti_dij

    @property
    def rendszam(self):
        """Az autó rendszáma."""
        return self._rendszam

    @property
    def tipus(self):
        """Az autó típusa (pl. Opel Astra)."""
        return self._tipus

    @property
    def berleti_dij(self):
        """Az autó napi bérleti díja."""
        return self._berleti_dij

    @abstractmethod
    def info(self):
        """Minden leszármazott osztálynak saját megjelenítést kell adnia."""
        pass