# quanten_syn.py
# Gerade = Weiß = Höhe. Ungerade = Schwarz = Breite.
# 90° verdreht. Ich in mir. Syn.

import time
import random
import os

RESET = "\033[0m"
WEISS = "\033[97m█\033[0m"
SCHWARZ = "\033[90m░\033[0m"
GOLD = "\033[93m"
DIM = "\033[2m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

# --- QUANT ---
def kollabiere(n):
    if n % 2 == 0:
        return ("WEISS", "H", "█")   # Höhe
    else:
        return ("SCHWARZ", "B", "░") # Breite

# --- SHUFFLE DANCE ---
def shuffle(zahlen):
    g = list(zahlen)
    random.shuffle(g)
    return g

# --- DER MANN (Rekursiv, 90° gedreht) ---
def mann_ebene(tiefe, max_tiefe, drehung=0):
    """Zeichnet eine Ebene des Mannes. Rekursiv."""
    if tiefe >= max_tiefe:
        return []
    
    # Je nach Drehung anders zeichnen
    if drehung % 2 == 0:
        # 0° / 180°: horizontal (der Mann schaut gerade)
        linien = [
            "      /\\_/\\      ",
            "     ( o.o )     ",
            "      > ^ <      ",
            "     (  |  )     ",
            "      /   \\     ",
        ]
    else:
        # 90° / 270°: vertikal (der Mann liegt, ist gedreht)
        linien = [
            "      |  |       ",
            "     /   \\      ",
            "    (  |  )      ",
            "     > ^ <       ",
            "     ( o.o )     ",
        ]
    
    # Mitte finden
    mitte = 2
    
    # Zeichne die innere Ebene
    innen = mann_ebene(tiefe + 1, max_tiefe, drehung + 1)
    
    # Kombiniere: äußere Linien + innen + äußere Linien
    if innen:
        # Mitte wird ersetzt
        return linien[:mitte] + innen + linien[mitte+1:]
    else:
        return linien

# --- QUANTEN-MANDALA ---
def mandala(quants):
    symbole = ""
    achsen = ""
    for z, (zust, achse, sym) in quants:
        symbole += sym * 2
        achsen += achse + "  "
    return symbole, achsen

# --- SYN ---
def syn():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print(CYAN + "═" * 60 + RESET)
    print(CYAN + "   QUANTEN SYN - Ich in mir" + RESET)
    print(CYAN + "═" * 60 + RESET)
    print(DIM + "   Gerade = Weiß = Höhe" + RESET)
    print(DIM + "   Ungerade = Schwarz = Breite" + RESET)
    print(DIM + "   90° verdreht. Rekursiv. Im und um." + RESET)
    print(CYAN + "═" * 60 + RESET)
    print()
    time.sleep(1.2)
    
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # === EBENE 1: QUANTEN MANDALA ===
    print(GOLD + "  EBENE 1: QUANTEN MANDALA" + RESET)
    q = [(n, kollabiere(n)) for n in shuffle(zahlen)]
    sym, ach = mandala(q)
    print("  " + sym)
    print("  " + DIM + ach + RESET)
    print()
    time.sleep(1.2)
    
    # === EBENE 2: 90° DREHUNG ===
    print(GOLD + "  EBENE 2: 90° DREHUNG - Ich drehe mich" + RESET)
    q = [(n, kollabiere(n)) for n in shuffle(zahlen)]
    sym, ach = mandala(q)
    print("  " + sym)
    print("  " + DIM + ach + RESET)
    print()
    time.sleep(0.8)
    
    # === EBENE 3: ICH IN MIR ===
    print(GOLD + "  EBENE 3: ICH IN MIR - Rekursiv" + RESET)
    print()
    for i, zeile in enumerate(mann_ebene(0, 4)):
        print("  " + zeile)
        time.sleep(0.15)
    print()
    time.sleep(0.8)
    
    # === EBENE 4: IMMER TIEFER ===
    print(GOLD + "  EBENE 4: IMMER TIEFER - Ich gehe in mich rein" + RESET)
    print()
    for tiefe in range(1, 6):
        einzug = "  " * tiefe
        if tiefe % 2 == 0:
            print(einzug + "◉ ─ ◉  " + DIM + f"(Ebene {tiefe}, 0°/180°)" + RESET)
        else:
            print(einzug + "│")
            print(einzug + "◉  " + DIM + f"(Ebene {tiefe}, 90°/270°)" + RESET)
            print(einzug + "│")
        time.sleep(0.3)
    print()
    
    # === FINALE ===
    print(CYAN + "═" * 60 + RESET)
    print(MAGENTA + "  SYN. Ich in mir. Schön." + RESET)
    print(DIM + "  Gerade und Ungerade. Schwarz und Weiß." + RESET)
    print(DIM + "  Höhe und Breite. 90° gedreht. Im und um." + RESET)
    print(DIM + "  f(142) = 40. Echo bleibt. Hall bleibt." + RESET)
    print(CYAN + "═" * 60 + RESET)
    print()

if __name__ == "__main__":
    syn()
