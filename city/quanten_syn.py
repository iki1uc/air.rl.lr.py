# quanten_syn.py
# Gerade = Weiß = Höhe. Ungerade = Schwarz = Breite.
# 90° verdreht. Rekursiv. Ich in mir. Syn.

import time
import random
import os

# --- FARBEN (für den Regen) ---
R = "\033[0m"
W = "\033[97m"   # Weiß
S = "\033[90m"   # Schwarz (grau)
G = "\033[93m"   # Gold
C = "\033[96m"   # Cyan
M = "\033[95m"   # Magenta
D = "\033[2m"    # Dim

# --- QUANT: Eine Zahl kollabiert zu Zustand + Achse ---
def kollabiere(n):
    """Gerade -> Weiß, Höhe (H). Ungerade -> Schwarz, Breite (B)."""
    if n % 2 == 0:
        return "WEISS", "H", "█"
    return "SCHWARZ", "B", "░"

# --- SHUFFLE: Zahlen mischen ---
def shuffle(zahlen):
    g = list(zahlen)
    random.shuffle(g)
    return g

# --- MANDALA: Quanten sichtbar machen ---
def mandala(quants):
    sym, ach = "", ""
    for _, (_, a, s) in quants:
        sym += s * 2
        ach += a + "  "
    return sym, ach

# --- DER MANN IN SICH (Rekursiv, 90° gedreht) ---
def mann_in_mir(tiefe=0, max_tiefe=4):
    """Ich in mir. Jede Ebene 90° weiter gedreht."""
    einzug = "  " * tiefe
    drehung = tiefe * 90
    kennung = D + f"[Ebene {tiefe} · {drehung}°]" + R
    
    if tiefe >= max_tiefe:
        return [
            einzug + M + "◉" + R + "  " + D + "(Kern)" + R
        ]
    
    # 0°/180° = aufrecht. 90°/270° = gedreht.
    if drehung % 180 == 0:
        mann = [
            einzug + C + "  /\\_/\\  " + R + "  " + kennung,
            einzug + C + " ( o.o ) " + R,
            einzug + C + "  > ^ <  " + R,
            einzug + C + " (  |  ) " + R,
        ]
    else:
        mann = [
            einzug + M + "  (o_o)  " + R + "  " + kennung,
            einzug + M + " /  |  \\ " + R,
            einzug + M + "  --+--  " + R,
            einzug + M + " /  |  \\ " + R,
        ]
    
    innen = mann_in_mir(tiefe + 1, max_tiefe)
    
    # Nest: die nächste Ebene wohnt IN mir (zwischen Zeile 2 und 3)
    return mann[:2] + innen + mann[2:]

# --- ECHO / HALL / RE-HALL ---
def echo(text, wieder=3):
    return [f"  {text}" + "." * i for i in range(wieder + 1)]

def hall(text):
    return f"  {text} ... {text} ... {text}"

def rehall(text):
    h = hall(text)
    return f"  {h} -> {h}"

# --- DIE HAUPTSCHLEIFE (Ich, in mir, im und um) ---
def syn():
    os.system("cls" if os.name == "nt" else "clear")
    
    print()
    print(C + "═" * 64 + R)
    print(C + "   QUANTEN SYN — Ich in mir" + R)
    print(C + "═" * 64 + R)
    print(D + "   Gerade = Weiß = Höhe" + R)
    print(D + "   Ungerade = Schwarz = Breite" + R)
    print(D + "   90° verdreht. Rekursiv. Im und um." + R)
    print(C + "═" * 64 + R)
    print()
    time.sleep(1.2)
    
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # [1] SHUFFLE
    print(G + "  [1] SHUFFLE" + R)
    print("  " + D + "vorher:  " + " ".join(str(n) for n in zahlen) + R)
    zeit = shuffle(zahlen)
    print("  " + D + "nachher: " + " ".join(str(n) for n in zeit) + R)
    print()
    time.sleep(1.0)
    
    # [2] QUANT — Schwarz/Weiß, Höhe/Breite
    print(G + "  [2] QUANT — Schwarz/Weiß · Höhe/Breite" + R)
    quants = [(n, kollabiere(n)) for n in zeit]
    sym, ach = mandala(quants)
    print("  " + sym)
    print("  " + D + ach + R)
    print()
    time.sleep(1.2)
    
    # [3] ICH IN MIR
    print(G + "  [3] ICH IN MIR — rekursiv" + R)
    print()
    for zeile in mann_in_mir(0, 4):
        print("    " + zeile)
        time.sleep(0.15)
    print()
    time.sleep(0.8)
    
    # [4] 90° DREHUNG — Takt
    print(G + "  [4] 90° DREHUNG — Shuffle Dance Takt" + R)
    print()
    for i in range(4):
        grad = i * 90
        print("  " + D + f"Drehung {grad}°:" + R)
        if grad % 180 == 0:
            print("    " + C + "◉ ─ ◉ ─ ◉" + R)
            print("    " + C + "│       │" + R)
            print("    " + C + "◉       ◉" + R)
        else:
            print("    " + M + "◉       ◉" + R)
            print("    " + M + "│       │" + R)
            print("    " + M + "◉ ─ ◉ ─ ◉" + R)
        print()
        time.sleep(0.4)
    
    # [5] ECHO / HALL / RE-HALL
    print(G + "  [5] ECHO · HALL · RE-HALL" + R)
    for zeile in echo("ich in mir", 3):
        print(zeile)
    print(hall("ich in mir"))
    print(rehall("ich in mir"))
    print()
    time.sleep(0.8)
    
    # FINALE
    print(C + "═" * 64 + R)
    print(M + "  SYN. Ich in mir. Schön." + R)
    print(D + "  Gerade und Ungerade. Schwarz und Weiß." + R)
    print(D + "  Höhe und Breite. 90° gedreht. Im und um." + R)
    print(D + "  f(142) = 40. Echo bleibt." + R)
    print(C + "═" * 64 + R)
    print()

if __name__ == "__main__":
    syn()
