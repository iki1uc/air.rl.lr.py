# quanten_syn.py
# Gerade = Weiß = Höhe. Ungerade = Schwarz = Breite.
# 90° verdreht. Ich in mir. Syn.

import time
import random
import os

# --- ZAHLEN (quanten) ---
# Gerade = Weiß, Höhe
# Ungerade = Schwarz, Breite

def kollabiere(n):
    """Nimmt eine Zahl in Superposition und gibt ihren Zustand."""
    if n % 2 == 0:
        return {"zahl": n, "zustand": "WEISS", "achse": "H", "symbol": "█"}
    else:
        return {"zahl": n, "zustand": "SCHWARZ", "achse": "B", "symbol": "░"}

# --- SHUFFLE MIT SCHWARZ/WEISS UND HÖHE/BREITE ---
def shuffle_quanten(zahlen):
    """Mischt die Zahlen und kollabiert sie zu Quanten."""
    gemischt = list(zahlen)
    random.shuffle(gemischt)
    return [kollabiere(n) for n in gemischt]

# --- DER MANN IN SICH (Rekursiv, 90° gedreht) ---
def mann_in_mir(tiefe, max_tiefe=4, oben=True):
    """Zeichnet den Mann, der in sich selbst schaut.
    Jede Ebene ist 90° weiter gedreht."""
    if tiefe >= max_tiefe:
        return []
    
    einzug = "  " * tiefe
    # Drehung: 90° bedeutet, die Linien werden anders gezeichnet
    if tiefe % 2 == 0:
        # 0° oder 180°
        linien = [
            "  /\\_/\\  ",
            " ( o.o ) ",
            "  > ^ <  ",
            " (  |  ) ",
        ]
    else:
        # 90° oder 270°
        linien = [
            "  __|__  ",
            " / o o \\ ",
            " \\  ^  / ",
            "  |   |  ",
        ]
    
    # Jede Linie mit Einzug
    ausgabe = [einzug + l for l in linien]
    
    # Die nächste Ebene in sich selbst
    if oben:
        naechste = mann_in_mir(tiefe + 1, max_tiefe, not oben)
        # Verschachteln: nächste Ebene kommt IN die Mitte des Mannes
        if naechste:
            # Mitte: die 3. Zeile wird ersetzt durch die nächste Ebene
            ausgabe = ausgabe[:2] + naechste + ausgabe[3:]
    
    return ausgabe

# --- QUANTEN-MANDALA ---
def quanten_mandala(quants, größe=24):
    """Zeichnet das Mandala aus den kollabierten Quanten."""
    # Erste Zeile: Symbole
    symbole = "".join(q["symbol"] * 2 for q in quants)
    
    # Zweite Zeile: Achsen
    achsen = " ".join(q["achse"] for q in quants)
    
    return symbole, achsen

# --- HAUPTFUNKTION ---
def syn():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" + "="*70)
    print("  QUANTEN SYN - Ich in mir")
    print("="*70)
    print("  Gerade = Weiß = Höhe")
    print("  Ungerade = Schwarz = Breite")
    print("  90° verdreht. Rekursiv. Im und um.")
    print("="*70 + "\n")
    
    time.sleep(1)
    
    # Die Zahlensammlung
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 40]
    
    # Shuffle
    quants = shuffle_quanten(zahlen)
    
    # Mandala zeigen
    symbole, achsen = quanten_mandala(quants)
    print("  QUANTEN-MANDALA:")
    print("  " + symbole)
    print("  " + achsen + "\n")
    
    time.sleep(1)
    
    # Der Mann in sich
    print("  DER MANN IN SICH (rekursiv, 90° gedreht):\n")
    for zeile in mann_in_mir(0, max_tiefe=5):
        print("  " + zeile)
    
    time.sleep(1)
    
    # Die Rekursion (90° gedreht)
    print("\n  90° DREHUNG - Ich gehe in mich rein:\n")
    
    for drehung in range(4):
        print(f"  Ebene {drehung+1} ({drehung * 90}°):")
        if drehung % 2 == 0:
            print("    ◉ ─ ◉  (horizontal)")
        else:
            print("    │   (vertikal)")
            print("    ◉")
        
        # Shuffle das Mandala neu
        quants = shuffle_quanten(zahlen)
        symbole, achsen = quanten_mandala(quants)
        print("    " + symbole)
        print()
        time.sleep(0.5)
    
    # Abschluss
    print("="*70)
    print("  SYN. Ich in mir. Schön.")
    print("  f(142) = 40. Echo bleibt.")
    print("="*70 + "\n")

if __name__ == "__main__":
    syn()
