from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles

class Autokolcsonzo:
    """
    Az autókölcsönző fő osztálya.
    Kezeli az autók listáját, a bérléseket és a műveleteket.
    """

    def __init__(self):
        self._autok = []
        self._berlesek = []

    @property
    def autok(self):
        """Az autók listája."""
        return self._autok

    @property
    def berlesek(self):
        """A bérlések listája."""
        return self._berlesek

    def auto_hozzaadas(self, auto):
        """Új autó hozzáadása a listához."""
        self._autok.append(auto)

    def berles(self, rendszam: str, datum: str, berlo_neve: str):
        """Új bérlés rögzítése rendszám alapján."""
        auto = next((a for a in self._autok if a.rendszam == rendszam), None)
        if auto is None:
            return False, "Nincs ilyen rendszámú autó."

        berles = Berles(auto, datum, berlo_neve)
        self._berlesek.append(berles)
        return True, "Bérlés sikeresen rögzítve."

    def berles_lemondas(self, rendszam: str):
        """Bérlés törlése rendszám alapján."""
        for b in self._berlesek:
            if b.auto.rendszam == rendszam:
                self._berlesek.remove(b)
                return True, "Bérlés lemondva."
        return False, "Ehhez a rendszámhoz nincs bérlés."

    def listaz_autok(self):
        """Az autók listáját adja vissza szövegként."""
        return [a.info() for a in self._autok]

    def listaz_berlesek(self):
        """A bérlések listáját adja vissza szövegként."""
        return [b.info() for b in self._berlesek]

    def elore_feltoltes(self):
        """Példaadatok betöltése a program indulásakor."""
        self.auto_hozzaadas(Szemelyauto("ABC-123", "Opel Astra", 12000, 5))
        self.auto_hozzaadas(Szemelyauto("XYZ-555", "Suzuki Swift", 10000, 3))
        self.auto_hozzaadas(Teherauto("TTT-999", "Ford Transit", 18000, 1200))