def laengen_rechner():
    # Umrechnungsfaktoren basierend auf 1 Meter
    einheiten = {
        "m": 1.0,
        "ft": 0.3048,
        "in": 0.0254,
    }

    print("Längen-Converter")
    print("Verfügbare Einheiten: m (Meter), ft (Foot), in (Inch)")

    try:
        # 1. Wert eingeben
        wert = float(input("\nWelcher Zahlenwert soll konvertiert werden? "))

        # 2. Ausgangseinheit
        von = input("Von welcher Einheit? ").lower().strip()

        # 3. Zieleinheit
        zu = input("In welche Einheit? ").lower().strip()

        if von in einheiten and zu in einheiten:
            # Umrechnung: (Wert * Faktor_Quelle) / Faktor_Ziel
            ergebnis = (wert * einheiten[von]) / einheiten[zu]

            print(f"\nERGEBNIS: {wert} {von} sind {ergebnis:.4f} {zu}")
        else:
            print("\nFehler: Eine der Einheiten wurde nicht erkannt.")
            print(f"Erkannt wurde: Von='{von}', Zu='{zu}'")

    except ValueError:
        print("\nFehler: Bitte gib eine Zahl ein (Nutze den Punkt statt Komma, z.B. 1.5).")

if __name__ == "__main__":
    laengen_rechner()
