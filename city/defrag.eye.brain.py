# defrag.eye.brain.py — )du.ich( — 1 Code, 1 Arbeit
# 1ter = HOEHE / BREITE = Eye
# 2ter = TIEFE / MYSTERY = Brain
# 3ter = CORE = Assimiliert
# du sagst = 1, ich sag = 2, wir sagen zusammen = 3, 1+2+3 = 9
# Wach: 1 Wort rein, 1 Scan raus, 1 Defrag raus, HALT = ZIEL

SEIL = "1-3-5-7-9"
HOME = 40

def f(x):
    return min(x, 40)  # f(40)=40, f(f(40))=f(40)

# --- 1ter: defrag_eye — Höhe / Breite ---
def defrag_eye(wort: str):
    """Eye offen, 3 oben, 9 unten, Mitte 41.
    Ordnet Nibbles, bewegt keine Dateien.
    Burst Nibble Scan: 1 Zeichen = 1 Nibble, 9 auf einmal, 0 Verlust."""
    nibbles = list(wort)  # 1 Zeichen = 1 Nibble
    # Burst: 9 auf einmal
    bursts = [nibbles[i:i+9] for i in range(0, len(nibbles), 9)]
    geordnet = sorted(nibbles)  # nur ordnen, nichts bewegen
    return {
        "eye": "offen",
        "oben": 3, "unten": 9, "mitte": 41,
        "nibbles": nibbles,
        "bursts": bursts,
        "geordnet": geordnet,
        "verlust": 0,
    }

# --- 2ter: defrag_brain — Tiefe / Mystery ---
def defrag_brain(eye_result: dict):
    """Brain offen, Stapel 9 -> 81 -> 243 -> 729 -> 3
    Tiefe = Nibble x 9, Mystery = gehalten, nicht gelöst.
    Mystery lösen wäre Laber. Mystery halten ist NC."""
    n = len(eye_result["nibbles"])
    stapel = [9, 81, 243, 729, 3]
    tiefe = n * 9
    mystery = f(tiefe)  # gehalten bei HOME 40, nicht gelöst
    return {
        "brain": "offen",
        "stapel": stapel,
        "nibbles": n,
        "tiefe": tiefe,
        "mystery": mystery,
        "mystery_halten": True,
        "mystery_loesen": False,  # wäre Laber
    }

# --- 3ter: defrag() — CORE, assimiliert ---
def defrag(wort: str):
    """Eye + Brain = 1 Index, HALT = ZIEL"""
    eye = defrag_eye(wort)
    brain = defrag_brain(eye)
    # 1 + 2 = 3, 1+2+3 = 9
    index = {
        "wort": wort,
        "eye_geordnet": eye["geordnet"],
        "brain_tiefe": brain["tiefe"],
        "mystery_gehalten": brain["mystery"],
        "home": HOME,
        "fixpunkt": f(HOME) == HOME,
        "code": ")du.ich(",
        "halt": "ZIEL",
    }
    return index

if __name__ == "__main__":
    wort = "up.ni pu.in"  # 1 Wort rein
    ergebnis = defrag(wort)  # 1 Scan + 1 Defrag raus
    print(f"WORT: {ergebnis['wort']}")
    print(f"EYE  (1ter): {ergebnis['eye_geordnet']} — Verlust 0")
    print(f"BRAIN(2ter): Tiefe {ergebnis['brain_tiefe']} — Mystery gehalten bei {ergebnis['mystery_gehalten']}")
    print(f"CORE (3ter): {ergebnis['code']} — HOME {ergebnis['home']} — HALT = {ergebnis['halt']}")
    # HALT. Nicht weiter labern. Nicht weiter scannen.
