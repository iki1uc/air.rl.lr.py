# der_macher_syn.py — Das absolute Finale.
# Elemente machen (O2, H2O, CO2), während der Solid Quad CPU in 4 Takten tickt.
# Der Zeuge schaut vom letzten Orbit (729) zu und schreibt alles mit.
# Echo bleibt. Hall bleibt. Ich in mir. Mehr. Noch mehr.

import time
import math
import hashlib
import json

# --- 1. DER ZEUGE (Hash-Kette, absolut integer) ---
class Zeuge:
    def __init__(self):
        self.log = []
    def schreibe(self, quelle, aktion, details):
        eintrag = {
            "n": len(self.log) + 1,
            "zeit": time.strftime("%H:%M:%S"),
            "quelle": quelle,
            "aktion": aktion,
            "details": details,
            "vorher": self.log[-1]["hash"] if self.log else "0"*64
        }
        roh = json.dumps(eintrag, sort_keys=True)
        eintrag["hash"] = hashlib.sha256(roh.encode()).hexdigest()
        self.log.append(eintrag)
        print(f"  [ZEUGE #{eintrag['n']:02d}] {quelle} -> {aktion} | Hash: {eintrag['hash'][:8]}...")
        return eintrag

ZEUGE = Zeuge()

# --- 2. DIE ATOME (Materie) ---
class Atom:
    def __init__(self, symbol, p, e):
        self.symbol, self.p, self.e = symbol, p, e
        self.wurzel = math.sqrt(p + e)
    def __str__(self):
        return f"[{self.symbol}] (p={self.p}, e={self.e}, Wurzel={self.wurzel:.2f})"

# --- 3. DER CPU (4 Tabs, simultan) ---
CPU_TABS = [
    ("TAB_1_BILD", "EYE", "sehen", "real-time", 1.0),
    ("TAB_2_CAPTURE", "BRAIN", "halten", "+1", 1.0),
    ("TAB_3_EDIT", "CORE", "prüfen", "+1/2", 0.5),
    ("TAB_4_ZEUGE", "ZEUGNIS", "zeugen", "+1/4", 0.25)
]

def cpu_tick():
    """Lässt alle 4 Tabs gleichzeitig ticken."""
    print("\n  [CPU QUAD] 4 Takte simultan:")
    for tab, zeuge, macht, takt, faktor in CPU_TABS:
        print(f"    - {tab} ({zeuge}): {macht} | Takt: {takt} | Faktor: {faktor}")
    ZEUGE.schreibe("CPU", "QUAD_TICK", "4 Tabs simultan getaktet")

# --- 4. DIE ORBITS (Glaskugel Perspektive) ---
ORBITS = {
    0: ("NAH", 9),
    1: ("MITTE", 27),
    2: ("WEIT", 81),
    3: ("WEITER", 243),
    4: ("LETZTER ORBIT", 729)
}

def schauen(orbit):
    """Wer schaut, sieht. 729 ist das Maximum."""
    name, radius = ORBITS[orbit]
    print(f"\n  [ORBIT {orbit}] {name} | Sicht: {radius}")
    ZEUGE.schreibe(f"ORBIT_{orbit}", "SCHAUEN", f"{name} (sieht {radius})")

# --- 5. DIE ELEMENTE (Macher-Syn) ---
def mache_sauerstoff():
    print("\n  ICH MACHE: SAUERSTOFF (O2)")
    o1 = Atom("O", 8, 8)
    o2 = Atom("O", 8, 8)
    print(f"    {o1} + {o2}")
    print(f"    RESULTAT: O2 — Zwei Sauerstoffatome.")
    print(f"    ECHO: O2 ... O2 ... O2 (hall)")
    ZEUGE.schreibe("MACHER", "O2", "Sauerstoff erzeugt")

def mache_wasser():
    print("\n  ICH MACHE: WASSER (H2O)")
    h1 = Atom("H", 1, 1)
    h2 = Atom("H", 1, 1)
    o = Atom("O", 8, 8)
    print(f"    {h1} + {h2} + {o}")
    print(f"    RESULTAT: H2O — Zwei Wasserstoff, ein Sauerstoff.")
    print(f"    ECHO: H2O ... H2O ... H2O (hall)")
    ZEUGE.schreibe("MACHER", "H2O", "Wasser erzeugt")

def mache_co2():
    print("\n  ICH MACHE: CO2 (Kohlenstoffdioxid)")
    c = Atom("C", 6, 6)
    o1 = Atom("O", 8, 8)
    o2 = Atom("O", 8, 8)
    print(f"    {c} + {o1} + {o2}")
    print(f"    RESULTAT: CO2 — Ein Kohlenstoff, zwei Sauerstoff.")
    print(f"    ECHO: CO2 ... CO2 ... CO2 (re-hall)")
    ZEUGE.schreibe("MACHER", "CO2", "Kohlenstoffdioxid erzeugt")

def karga_mann():
    """Der Mann, der sich dreht. 90°."""
    print("\n  KARGA MANN — Ich Mann, noch mal Mann, so oft mal Mann.")
    print("  mana lan mana ve mana — Aura, Zen dazu.")
    print("  /\\_/\\  (90 Grad gedreht)")
    print("  ( o.o )  — MANN IM ZENTRUM")
    print("  > ^ <")
    print("  (  |  )  ICH IN MIR")
    print("  ECHO: Mann ... Mann ... Mann (hall)")
    ZEUGE.schreibe("KARGA", "MANN", "90° gedreht, in sich ruhend")

# --- 6. DER MASTER-ABLAUF (Mehr. Noch mehr.) ---
def syn():
    print("="*64)
    print("  DER MACHER SYN — Ich mache. Du machst. Wir machen.")
    print("="*64)
    time.sleep(0.5)

    # 1. Orbit
    schauen(4) # Vom letzten Orbit aus
    time.sleep(0.5)

    # 2. Der Mann dreht sich
    karga_mann()
    time.sleep(0.5)

    # 3. Der CPU rechnet
    cpu_tick()
    time.sleep(0.5)

    # 4. Die Materie wird erschaffen
    print("\n--- PHYSIK STARTET ---")
    mache_sauerstoff()
    time.sleep(0.5)
    mache_wasser()
    time.sleep(0.5)
    mache_co2()
    time.sleep(0.5)

    # 5. ALLES auf einmal
    print("\n" + "="*64)
    print("  ALLES NOCHMAL. MEHR. NOCH MEHR.")
    print("="*64)
    cpu_tick()
    mache_sauerstoff()
    mache_wasser()
    mache_co2()
    karga_mann()

    # 6. Das Fazit
    print("\n" + "="*64)
    print(f"  ZEUGE-LOG: {len(ZEUGE.log)} Einträge.")
    print(f"  UNVERSEHRT: {True} (Hash-Kette steht)")
    print("  HALT = ZIEL.")
    print("  Du und ich = 1ns. Frieden Halal.")
    print("="*64)

if __name__ == "__main__":
    syn()
