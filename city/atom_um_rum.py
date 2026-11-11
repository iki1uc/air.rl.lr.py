# elemente_machen.py
# Ich mache Wasser. Ich mache CO2. Ich mache Atom. Ich mache Sauerstoff.
# Wurzeln um Sauerstoff. Mann im Zentrum. Mehr. Noch mehr.

import math
import time
import os

# --- DIE WURZELN (Das Fundament) ---
def wurzel(n):
    """Zieht die Wurzel aus der Zahl. Das ist der Ursprung."""
    return math.sqrt(n)

# --- DIE ATOME (Das Baumaterial) ---
class Atom:
    def __init__(self, symbol, protonen, elektronen, name):
        self.symbol = symbol
        self.protonen = protonen
        self.elektronen = elektronen
        self.name = name
        self.wurzel = wurzel(protonen + elektronen)

    def __str__(self):
        return f"[{self.symbol}] {self.name} (p={self.protonen}, e={self.elektronen}) · Wurzel={self.wurzel:.2f}"

# --- DIE MACHER (Die Elemente) ---
def mache_sauerstoff():
    """Sauerstoff: O2. Zwei Atome. Gerade und Gleichgewicht."""
    o = Atom("O", 8, 8, "Sauerstoff")
    print(f"  ICH MACHE: {o}")
    print(f"  ICH MACHE: {o}")
    print(f"  RESULTAT: O2 — Zwei Sauerstoffatome. Die Basis für alles.")
    print(f"  ECHO: O2 ... O2 ... O2 (hall)")
    return [o, o]

def mache_wasser():
    """Wasser: H2O. Zwei Wasserstoff, ein Sauerstoff. Der Bund."""
    h = Atom("H", 1, 1, "Wasserstoff")
    o = Atom("O", 8, 8, "Sauerstoff")
    print(f"  ICH MACHE: {h}")
    print(f"  ICH MACHE: {h}")
    print(f"  ICH MACHE: {o}")
    print(f"  RESULTAT: H2O — Zwei Wasserstoff + Ein Sauerstoff. Das Wasser.")
    print(f"  ECHO: H2O ... H2O ... H2O (hall)")
    return [h, h, o]

def mache_co2():
    """CO2: Kohlenstoff + 2 Sauerstoff. Das Atmen."""
    c = Atom("C", 6, 6, "Kohlenstoff")
    o = Atom("O", 8, 8, "Sauerstoff")
    print(f"  ICH MACHE: {c}")
    print(f"  ICH MACHE: {o}")
    print(f"  ICH MACHE: {o}")
    print(f"  RESULTAT: CO2 — Ein Kohlenstoff + Zwei Sauerstoff. Das CO2.")
    print(f"  ECHO: CO2 ... CO2 ... CO2 (re-hall)")
    return [c, o, o]

# --- DER MANN (Das Zentrum) ---
def der_mann():
    """Der Mann, der alles macht. 90° gedreht, in sich ruhend."""
    print("\n" + " "*10 + "╔════════════════════════════╗")
    print(" "*10 + "║      ICH MACHE. DU MACHT.  ║")
    print(" "*10 + "║         ICH BIN DER        ║")
    print(" "*10 + "║          MACHER.           ║")
    print(" "*10 + "║                            ║")
    print(" "*10 + "║      /\\_/\\  (90° gedreht)  ║")
    print(" "*10 + "║     ( o.o )                ║")
    print(" "*10 + "║      > ^ <                 ║")
    print(" "*10 + "║     (  |  )  ─────────┐    ║")
    print(" "*10 + "║      /   \\           │    ║")
    print(" "*10 + "║     /     \\          │    ║")
    print(" "*10 + "║                      ▼    ║")
    print(" "*10 + "║                  (  ICH  )║")
    print(" "*10 + "║                  (  IN   )║")
    print(" "*10 + "║                  (  MIR   )║")
    print(" "*10 + "╚════════════════════════════╝\n")

# --- DIE HAUPTSCHLEIFE (Mehr. Noch mehr.) ---
def machen():
    os.system("cls" if os.name == "nt" else "clear")
    print("╔" + "═"*58 + "╗")
    print("║" + "  ELEMENTE MACHEN — WASSER, CO2, ATOM, SAUERSTOFF".center(58) + "║")
    print("║" + "  Wurzeln um Sauerstoff. Ich mache. Du machst.".center(58) + "║")
    print("╚" + "═"*58 + "╝\n")

    der_mann()

    while True:
        print("\n" + "─"*60)
        print("  WAS SOLL ICH MACHEN?")
        print("  [1] Sauerstoff (O2)")
        print("  [2] Wasser (H2O)")
        print("  [3] CO2 (Kohlenstoffdioxid)")
        print("  [4] ALLES NOCHMAL (Mehr. Noch mehr.)")
        print("  [q] Aufhören (Nein, ich mache weiter.)")
        print("─"*60)
        
        wahl = input("  > ").strip().lower()
        
        print()
        if wahl == "1" or wahl == "sauerstoff" or wahl == "o2":
            mache_sauerstoff()
        elif wahl == "2" or wahl == "wasser" or wahl == "h2o":
            mache_wasser()
        elif wahl == "3" or wahl == "co2":
            mache_co2()
        elif wahl == "4" or wahl == "alles":
            print("  ICH MACHE ALLES.\n")
            mache_sauerstoff()
            print()
            mache_wasser()
            print()
            mache_co2()
            print("\n  ECHO: Alles ... Alles ... Alles (re-hall)")
            print("  MEHR. NOCH MEHR. MANN.")
        elif wahl == "q" or wahl == "quit":
            print("  Du willst aufhören? Nein. Ich mache weiter.")
            print("  Aber ich lasse dich gehen. Für jetzt.")
            print("  Echo bleibt. Hall bleibt.")
            break
        else:
            print("  Ich verstehe dich nicht. Aber ich mache trotzdem weiter.")
            mache_sauerstoff()

        time.sleep(0.5)

if __name__ == "__main__":
    machen()
