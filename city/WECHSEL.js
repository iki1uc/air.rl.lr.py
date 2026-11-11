# WECHSEL, axiomisch korrekt: w(w(x)) = x, kein Verlust
WECHSEL = {
    "H": "B",  # Höhe <-> Breite = links / rechts
    "B": "T",  # Breite <-> Tiefe = um Biege
    "T": "H",  # Tiefe <-> Höhe = zurück zur Mitte
}

def wechsel(ebene):
    return WECHSEL[ebene]

def wechsel_zurueck(ebene):
    # 2x wechseln = zurück
    return WECHSEL[WECHSEL[ebene]]  # muss wieder Start sein, sonst Laber
