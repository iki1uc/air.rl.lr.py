# shift.drunter.map.py — ORDNER SHIFT · DRUNTER, MANN
# Kann ich die letzten auch zu Shift rein tun, Mann? — Ja, Mann. Drunter, Mann.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
# Drunter = Fundament. Haelt unten. Sieht man nicht, aber traegt alles drueber.

SHIFT_DRUNTER_ALT = ["Nc.cpp", "kombinat.9.py", "anomalie.territorial.class.eye.brain.continuum.py"]
SHIFT_DRUNTER_NEU = [
    ("kasparov_3x.py", "KASPAROV 3x — 1 VS 1, 21 x 3, 63 Steps — Schach zu Schach"),
    ("quantum_shuffle_syn.py", "QUANTUM SHUFFLE — vor, rueck, ruecke, verkehre, rum x3 -> Mitte"),
    ("abra.kadabra.py", "ABRA KADABRA — Traum an/aus — Auge zu/auf — Schaefer Zug"),
    ("der_macher_syn.py", "MACHER SYN — O2, H2O, CO2, CPU Quad, Orbit 729, Karga"),
    ("schhaeferzug_bht_3x.py", "SCHHAEFERZUG B H T — 3x B H T, 3x Mann in in in Mann"),
    ("drei_welten_glas_kugel_pentagramm_mann.py", "3 WELTEN — Glas Kugel — Pentagramm — Mann — 1 ORT"),
    ("raabe_mann_eye_mann.py", "RAABE MANN EYE MANN — Rabe fliegt, Mann macht, Eye sieht — 1 Zeuge"),
]

def zeige():
    print("ORDNER SHIFT · DRUNTER, MANN")
    print("Drunter = Fundament. Haelt unten. Traegt alles drueber.")
    print("\nALT — schon drunter:")
    for f in SHIFT_DRUNTER_ALT:
        print(f"  - {f}")
    print("\nNEU — die letzten, jetzt auch drunter:")
    for f, warum in SHIFT_DRUNTER_NEU:
        print(f"  - {f}")
        print(f"      {warum}")
    gesamt = len(SHIFT_DRUNTER_ALT) + len(SHIFT_DRUNTER_NEU)
    print(f"\nSHIFT DRUNTER: ALT {len(SHIFT_DRUNTER_ALT)} + NEU {len(SHIFT_DRUNTER_NEU)} = {gesamt} Dateien")
    print("Drunter heisst: nicht drauf, nicht daneben, nicht drueber. Drunter.")
    print("Wer drunter steht, haelt. Wer drauf steht, sieht. Beides braucht man.")
    print("HALT = OFFEN — geloescht=False — Alles um rum, Mann.")
    print("ECO: SHIFT DRUNTER — Fundament, 10 Dateien, 1 Mitte.")
    print("FUNKTION: shift_drunter() -> ALT + NEU -> 1 Fundament.")

if __name__ == "__main__":
    zeige()
