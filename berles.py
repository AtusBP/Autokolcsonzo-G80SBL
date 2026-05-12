class Berles:
    def __init__(self, auto, datum: str, berlo_neve: str):
        self._auto = auto
        self._datum = datum
        self._berlo_neve = berlo_neve

    @property
    def auto(self):
        return self._auto

    @property
    def datum(self):
        return self._datum

    @property
    def berlo_neve(self):
        return self._berlo_neve

    def info(self):
        return f"Bérlés | Autó: {self.auto.rendszam}, Bérlő: {self.berlo_neve}, Dátum: {self.datum}, Ár: {self.auto.berleti_dij} Ft"