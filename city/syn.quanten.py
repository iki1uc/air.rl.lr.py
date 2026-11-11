# quanten_syn.py
# Gerade = Weiß = Höhe. Ungerade = Schwarz = Breite.
# 90° verdreht. Ich in mir. Syn.

import time
import random
import os

# --- ANSI FARBEN ---
R = "\033[0m"
W = "\033[97m"    # Weiß
S = "\033[90m"    # Schwarz (grau)
G = "\033[93m"    # Gold
C = "\033[96m"    # Cyan
M = "\033[95m"    # Magenta
D = "\033[2m"     # Dim

# --- QUANT ---
def kollabiere(n):
    if n % 2 == 0:
        return "WEISS", "H", "█"
    else:
        return "SCHWARZ", "B", "░"

# --- SHUFFLE ---
def shuffle(zahlen):
    g = list(zahlen)
    random.shuffle(g)
    return g

# --- DER MANN IN SICH (Rekursiv, 90° gedreht) ---
def mann_quadrat(größe, tiefe=0, max_tiefe=4):
    """Zeichnet den Mann in einem Quadrat. Rekursiv verkleinert."""
    if tiefe >= max_tiefe:
        return []
    
    # Symbole je nach Drehung
    if tiefe % 2 == 0:
        # 0° / 180° — aufrecht
        kern = "◉"
    else:
        # 90° / 270° — gedreht
        kern = "◎"
    
    # Innere Ebene zuerst berechnen
    innen = mann_quadrat(größe - 4, tiefe + 1, max_tiefe)
    
    if innen:
        # Rahmen um die innere Ebene
        breite_innen = len(innen[0])
        rahmen_oben = "┌" + "─" * breite_innen + "┐"
        rahmen_unten = "└" + "─" * breite_innen + "┘"
        
        ergebnis = [rahmen_oben]
        for zeile in innen:
            ergebnis.append("│" + zeile + "│")
        ergebnis.append(rahmen_unten)
        
        # Füge den Kern oben drauf
        return [kern] + ergebnis
    else:
        # Basisfall: nur der Kern
        return [kern]

# --- QUANTEN-MANDALA ---
def mandala(quants):
    sym = ""
    ach = ""
    for z, (zust, a, s) in quants:
        sym += s * 2
        ach += a + "  "
    return sym, ach

# --- SYN ---
def syn():
    os.system("cls" if os.name == "nt" else "clear")
    
    print()
    print(C + "═" * 60 + R)
    print(C + "   QUANTEN SYN - Ich in mir" + R)
    print(C + "═" * 60 + R)
    print(D + "   Gerade = Weiß = Höhe" + R)
    print(D + "   Ungerade = Schwarz = Breite" + R)
    print(D + "   90° verdreht. Rekursiv. Im und um." + R)
    print(C + "═" * 60 + R)
    print()
    time.sleep(1.2)
    
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # === EBENE 1: SHUFFLE ===
    print(G + "  [1] SHUFFLE - Zahlen mischen" + R)
    print(D + "  Vorher: " + " ".join(str(n) for n in zahlen) + R)
    zeit = shuffle(zahlen)
    print(D + "  Nachher: " + " ".join(str(n) for n in zeit) + R)
    print()
    time.sleep(1.0)
    
    # === EBENE 2: SCHWARZ/WEISS + HÖHE/BREITE ===
    print(G + "  [2] QUANTEN - Schwarz/Weiß · Höhe/Breite" + R)
    quants = [(n, kollabiere(n)) for n in zeit]
    sym, ach = mandala(quants)
    print("  " + sym)
    print("  " + D + ach + R)
    print()
    time.sleep(1.2)
    
    # === EBENE 3: ICH IN MIR ===
    print(G + "  [3] ICH IN MIR - Rekursiv" + R)
    print()
    for zeile in mann_quadrat(30, 0, 4):
        print("    " + zeile)
        time.sleep(0.12)
    print()
    time.sleep(0.8)
    
    # === EBENE 4: 90° DREHUNG ===
    print(G + "  [4] 90° DREHUNG - Ich drehe mich" + R)
    print()
    
    # Zeige 4 Drehungen
    for i in range(4):
        grad = i * 90
        print(D + f"    Drehung {grad}°:" + R)
        
        if grad % 180 == 0:
            # Aufrecht
            print("    ◉ ─ ◉ ─ ◉")
            print("    │       │")
            print("    ◉       ◉")
        else:
            # Gedreht
            print("    ◉       ◉")
            print("    │       │")
            print("    ◉ ─ ◉ ─ ◉")
        print()
        time.sleep(0.4)
    
    # === EBENE 5: SYN ===
    print(G + "  [5] SYN - Schön" + R)
    print()
    time.sleep(0.6)
    print("    " + "◉")
    print("    " + "│")
    print("    " + "◎  " + D + "(90° gedreht)" + R)
    print("    " + "│")
    print("    " + "◉  " + D + "(wieder aufrecht)" + R)
    print()
    time.sleep(1.0)
    
    # === FINALE ===
    print(C + "═" * 60 + R)
    print(M + "  SYN. Ich in mir. Schön." + R)
    print(D + "  Gerade und Ungerade. Schwarz und Weiß." + R)
    print(D + "  Höhe und Breite. 90° gedreht. Im und um." + R)
    print(D + "  f(142) = 40. Echo bleibt." + R)
    print(C + "═" * 60 + R)
    print()

if __name__ == "__main__":
    syn()
