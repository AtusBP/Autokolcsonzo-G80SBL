import datetime
from autokolcsonzo import Autokolcsonzo

def datum_valid(datum: str):
    try:
        datetime.datetime.strptime(datum, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    kolcsonzo = Autokolcsonzo()
    kolcsonzo.elore_feltoltes()

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ ---")
        print("1. Autók listázása")
        print("2. Bérlések listázása")
        print("3. Autó bérlése")
        print("4. Bérlés lemondása")
        print("5. Kilépés")

        valasztas = input("Válassz egy menüpontot (1-5): ").strip()

        if valasztas not in ["1", "2", "3", "4", "5"]:
            print("Érvénytelen választás, próbáld újra.")
            continue

        if valasztas == "1":
            autok = kolcsonzo.listaz_autok()
            if not autok:
                print("Nincs egyetlen autó sem.")
            else:
                print("\n--- Autók listája ---")
                for i, a in enumerate(autok, start=1):
                    print(f"{i}. {a}")

        elif valasztas == "2":
            berlesek = kolcsonzo.listaz_berlesek()
            if not berlesek:
                print("Nincs egyetlen bérlés sem.")
            else:
                print("\n--- Bérlések listája ---")
                for i, b in enumerate(berlesek, start=1):
                    print(f"{i}. {b}")

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

        elif valasztas == "4":
            rendszam = input("Add meg a rendszámot: ").strip().upper()
            if not rendszam:
                print("A rendszám nem lehet üres.")
                continue

            siker, uzenet = kolcsonzo.berles_lemondas(rendszam)
            print(uzenet)

        elif valasztas == "5":
            print("Kilépés...")
            break

if __name__ == "__main__":
    main()