from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles

class Autokolcsonzo:
    def __init__(self):
        self._autok = []
        self._berlesek = []

    @property
    def autok(self):
        return self._autok

    @property
    def berlesek(self):
        return self._berlesek

    def auto_hozzaadas(self, auto):
        self._autok.append(auto)

    def berles(self, rendszam: str, datum: str, berlo_neve: str):
        auto = next((a for a in self._autok if a.rendszam == rendszam), None)
        if auto is None:
            return False, "Nincs ilyen rendszámú autó."

        berles = Berles(auto, datum, berlo_neve)
        self._berlesek.append(berles)
        return True, "Bérlés sikeresen rögzítve."

    def berles_lemondas(self, rendszam: str):
        for b in self._berlesek:
            if b.auto.rendszam == rendszam:
                self._berlesek.remove(b)
                return True, "Bérlés lemondva."
        return False, "Ehhez a rendszámhoz nincs bérlés."

    def listaz_autok(self):
        return [a.info() for a in self._autok]

    def listaz_berlesek(self):
        return [b.info() for b in self._berlesek]

    def elore_feltoltes(self):
        self.auto_hozzaadas(Szemelyauto("ABC-123", "Opel Astra", 12000, 5))
        self.auto_hozzaadas(Szemelyauto("XYZ-555", "Suzuki Swift", 10000, 3))
        self.auto_hozzaadas(Teherauto("TTT-999", "Ford Transit", 18000, 1200))