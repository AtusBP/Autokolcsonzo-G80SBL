from auto import Auto

class Szemelyauto(Auto):
    """
    Személyautó osztály.
    Az Auto ősosztályból származik, plusz tartalmazza az ajtók számát.
    """

    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, ajtok_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._ajtok_szama = ajtok_szama

    @property
    def ajtok_szama(self):
        """A személyautó ajtóinak száma."""
        return self._ajtok_szama

    def info(self):
        """A személyautó adatait formázott szövegként adja vissza."""
        return f"Személyautó | Rendszám: {self.rendszam}, Típus: {self.tipus}, Ajtók: {self.ajtok_szama}, Díj: {self.berleti_dij} Ft/nap"