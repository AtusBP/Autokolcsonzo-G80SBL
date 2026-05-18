from auto import Auto

class Teherauto(Auto):
    """
    Teherautó osztály.
    Az Auto ősosztályból származik, plusz tartalmazza a teherbírást.
    """

    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._teherbiras = teherbiras

    @property
    def teherbiras(self):
        """A teherautó maximális teherbírása kilogrammban."""
        return self._teherbiras

    def info(self):
        """A teherautó adatait formázott szövegként adja vissza."""
        return f"Teherautó | Rendszám: {self.rendszam}, Típus: {self.tipus}, Teherbírás: {self.teherbiras} kg, Díj: {self.berleti_dij} Ft/nap"