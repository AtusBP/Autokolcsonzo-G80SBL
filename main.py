from autokolcsonzo import Autokolcsonzo

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

        valasztas = input("Válassz egy menüpontot: ")

        if valasztas == "1":
            autok = kolcsonzo.listaz_autok()
            if not autok:
                print("Nincs egyetlen autó sem.")
            else:
                print("\n--- Autók ---")
                for a in autok:
                    print(a)

        elif valasztas == "2":
            berlesek = kolcsonzo.listaz_berlesek()
            if not berlesek:
                print("Nincs egyetlen bérlés sem.")
            else:
                print("\n--- Bérlések ---")
                for b in berlesek:
                    print(b)

        elif valasztas == "3":
            rendszam = input("Add meg a rendszámot: ")
            datum = input("Add meg a dátumot (pl. 2024-05-12): ")
            berlo = input("Add meg a bérlő nevét: ")

            siker, uzenet = kolcsonzo.berles(rendszam, datum, berlo)
            print(uzenet)

        elif valasztas == "4":
            rendszam = input("Add meg a rendszámot: ")
            siker, uzenet = kolcsonzo.berles_lemondas(rendszam)
            print(uzenet)

        elif valasztas == "5":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()