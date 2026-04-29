from auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._teherbiras = teherbiras

    @property
    def teherbiras(self):
        return self._teherbiras

    def info(self):
        return f"Teherautó | Rendszám: {self.rendszam}, Típus: {self.tipus}, Teherbírás: {self.teherbiras} kg, Díj: {self.berleti_dij} Ft/nap"