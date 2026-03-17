"""Definition der Funktion laengen_rechner"""


def laengen_rechner(wert, von, zu):
    """Rechnet die eingegebenen Einheiten um"""
    # Umrechnungsfaktoren basierend auf 1 Meter
    einheiten = {
        "m": 1.0,
        "ft": 0.3048,
        "in": 0.0254,
    }

    # Überprüfung, ob Einheiten existieren
    if von not in einheiten or zu not in einheiten:
        return None

    # Umrechnung: Startwert -> Meter -> Zielwert
    meter = wert * einheiten[von]
    ergebnis = meter / einheiten[zu]
    return ergebnis
