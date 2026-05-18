class Berles:
    """
    Egy autó bérlését reprezentáló osztály.
    Tartalmazza a bérlés dátumát, a bérlő nevét és a bérelt autót.
    """

    def __init__(self, auto, datum: str, berlo_neve: str):
        self._auto = auto
        self._datum = datum
        self._berlo_neve = berlo_neve

    @property
    def auto(self):
        """A bérelt autó objektuma."""
        return self._auto

    @property
    def datum(self):
        """A bérlés dátuma."""
        return self._datum

    @property
    def berlo_neve(self):
        """A bérlő neve."""
        return self._berlo_neve

    def info(self):
        """A bérlés adatait formázott szövegként adja vissza."""
        return f"Bérlés | Autó: {self.auto.rendszam}, Bérlő: {self.berlo_neve}, Dátum: {self.datum}, Ár: {self.auto.berleti_dij} Ft"