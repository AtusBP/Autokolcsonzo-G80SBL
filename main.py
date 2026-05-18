import datetime
from autokolcsonzo import Autokolcsonzo

# ---------------------------------------------------------
# Segédfüggvény: dátum validálása (YYYY-MM-DD formátum)
# ---------------------------------------------------------
def datum_valid(datum: str):
    """
    Ellenőrzi, hogy a megadott dátum helyes-e.
    A helyes formátum: YYYY-MM-DD
    """
    try:
        datetime.datetime.strptime(datum, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ---------------------------------------------------------
# A program belépési pontja
# ---------------------------------------------------------
def main():
    """
    A főmenü működését vezérlő függvény.
    Itt történik:
    - az autókölcsönző példányosítása
    - az előre feltöltött adatok betöltése
    - a menü megjelenítése
    - a felhasználói műveletek kezelése
    """
    kolcsonzo = Autokolcsonzo()
    kolcsonzo.elore_feltoltes()  # Példaadatok betöltése

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ ---")
        print("1. Autók listázása")
        print("2. Bérlések listázása")
        print("3. Autó bérlése")
        print("4. Bérlés lemondása")
        print("5. Kilépés")

        # -----------------------------
        # Menüválasztás validálása
        # -----------------------------
        valasztas = input("Válassz egy menüpontot (1-5): ").strip()

        if valasztas not in ["1", "2", "3", "4", "5"]:
            print("Érvénytelen választás, próbáld újra.")
            continue

        # -----------------------------
        # 1. Autók listázása
        # -----------------------------
        if valasztas == "1":
            autok = kolcsonzo.listaz_autok()
            if not autok:
                print("Nincs egyetlen autó sem.")
            else:
                print("\n--- Autók listája ---")
                for i, a in enumerate(autok, start=1):
                    print(f"{i}. {a}")

        # -----------------------------
        # 2. Bérlések listázása
        # -----------------------------
        elif valasztas == "2":
            berlesek = kolcsonzo.listaz_berlesek()
            if not berlesek:
                print("Nincs egyetlen bérlés sem.")
            else:
                print("\n--- Bérlések listája ---")
                for i, b in enumerate(berlesek, start=1):
                    print(f"{i}. {b}")

        # -----------------------------
        # 3. Autó bérlése
        # -----------------------------
        elif valasztas == "3":
            rendszam = input("Add meg a rendszámot: ").strip().upper()
            if not rendszam:
                print("A rendszám nem lehet üres.")
                continue

            datum = input("Add meg a dátumot (YYYY-MM-DD): ").strip()
            if not datum_valid(datum):
                print("Hibás dátumformátum. Példa: 2024-05-12")
                continue

            berlo = input("Add meg a bérlő nevét: ").strip()
            if not berlo:
                print("A bérlő neve nem lehet üres.")
                continue

            siker, uzenet = kolcsonzo.berles(rendszam, datum, berlo)
            print(uzenet)

        # -----------------------------
        # 4. Bérlés lemondása
        # -----------------------------
        elif valasztas == "4":
            rendszam = input("Add meg a rendszámot: ").strip().upper()
            if not rendszam:
                print("A rendszám nem lehet üres.")
                continue

            siker, uzenet = kolcsonzo.berles_lemondas(rendszam)
            print(uzenet)

        # -----------------------------
        # 5. Kilépés
        # -----------------------------
        elif valasztas == "5":
            print("Kilépés...")
            break


# ---------------------------------------------------------
# Program indítása
# ---------------------------------------------------------
if __name__ == "__main__":
    main()