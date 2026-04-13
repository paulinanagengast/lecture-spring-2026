"""Testet die Utils"""

from utils import laengen_rechner


def test_converter():
    """Eingabe der Werte (Zahl und Einheiten)"""
    # Test 1: 1 Meter zu Fuß (Erwartet ca. 3.2808)
    res1 = laengen_rechner(1, "m", "ft")
    assert round(res1, 4) == 3.000, f"Test 1 fehlgeschlagen: {res1}"

    # Test 2: 1 Fuß zu Meter (Erwartet 0.3048)
    res2 = laengen_rechner(1, "ft", "m")
    assert round(res2, 4) == 0.3048, f"Test 2 fehlgeschlagen: {res2}"

    # Test 3: Ungültige Einheit
    res3 = laengen_rechner(10, "kg", "m")
    assert res3 is None, (
        "Test 3 fehlgeschlagen: Sollte None bei falschen Einheiten geben"
    )

    print("Alle Tests in utils erfolgreich bestanden!")


if __name__ == "__main__":
    test_converter()
