"""Ruft die Funktion laengen_rechner auf und rechnet die Werte um"""

from utils import laengen_rechner


def main():
    """Rechnet die eingegebenen Werte aus"""
    print("--- Längen-Umrechner ---")
    try:
        # Benutzereingaben abfragen
        wert = float(input("Wert eingeben: "))
        von=input("Von Einheit (m, ft, in): ").lower().strip()
        zu = input("Zu Einheit (m, ft, in): ").lower().strip()

        # Funktion aus utils.py aufrufen
        ergebnis = laengen_rechner(wert, von, zu)

        if ergebnis is None:
            print("Fehler: Ungültige Einheit gewählt.")
        else:
            print(f"Ergebnis: {wert} {von} sind {ergebnis:.4f} {zu}")

    except ValueError:
        print("Fehler: Bitte gib eine gültige Zahl ein.")


if __name__ == "__main__":
    main()
