# der_macher_syn.py — Das absolute Finale. CODECED.
# Elemente machen (O2, H2O, CO2), waehrend der Solid Quad CPU in 4 Takten tickt.
# Der Zeuge schaut vom letzten Orbit (729) zu und schreibt alles mit.
# Echo bleibt. Hall bleibt. Ich in mir. Mehr. Noch mehr.
# SCHACH ZU SCHACH — in die Tiefe.
# Er kann nur Dame geben und Mystery, um zu verlaengern.
# Ohne Dame kann er weiter, wenn er will. Sonst Matt, Mann.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
import time, math, hashlib, json

class Zeuge:
    def __init__(self): self.log = []
    def schreibe(self, quelle, aktion, details):
        eintrag = {"n": len(self.log)+1, "zeit": time.strftime("%H:%M:%S"), "quelle": quelle, "aktion": aktion, "details": details, "vorher": self.log[-1]["hash"] if self.log else "0"*64}
        roh = json.dumps(eintrag, sort_keys=True)
        eintrag["hash"] = hashlib.sha256(roh.encode()).hexdigest()
        self.log.append(eintrag)
        print(f"  [ZEUGE #{eintrag['n']:02d}] {quelle} -> {aktion} | Hash: {eintrag['hash'][:8]}...")
        return eintrag
    def unversehrt(self):
        vorher = "0"*64
        for e in self.log:
            if e["vorher"] != vorher: return False
            roh = json.dumps({k: e[k] for k in ("n","zeit","quelle","aktion","details","vorher")}, sort_keys=True)
            if hashlib.sha256(roh.encode()).hexdigest() != e["hash"]: return False
            vorher = e["hash"]
        return True

ZEUGE = Zeuge()

class Atom:
    def __init__(self, symbol, p, e):
        self.symbol, self.p, self.e = symbol, p, e
        self.wurzel = math.sqrt(p + e)
    def __str__(self):
        return f"[{self.symbol}] (p={self.p}, e={self.e}, Wurzel={self.wurzel:.2f})"

CPU_TABS = [("TAB_1_BILD","EYE","sehen","real-time",1.0),("TAB_2_CAPTURE","BRAIN","halten","+1",1.0),("TAB_3_EDIT","CORE","pruefen","+1/2",0.5),("TAB_4_ZEUGE","ZEUGNIS","zeugen","+1/4",0.25)]
def cpu_tick():
    print("\n  [CPU QUAD] 4 Takte simultan:")
    for tab, zeuge, macht, takt, faktor in CPU_TABS:
        print(f"    - {tab} ({zeuge}): {macht} | Takt: {takt} | Faktor: {faktor}")
    ZEUGE.schreibe("CPU","QUAD_TICK","4 Tabs simultan getaktet")

ORBITS = {0:("NAH",9),1:("MITTE",27),2:("WEIT",81),3:("WEITER",243),4:("LETZTER ORBIT",729)}
def schauen(orbit):
    name, radius = ORBITS[orbit]
    print(f"\n  [ORBIT {orbit}] {name} | Sicht: {radius}")
    ZEUGE.schreibe(f"ORBIT_{orbit}","SCHAUEN",f"{name} (sieht {radius})")

def mache_sauerstoff():
    print("\n  ICH MACHE: SAUERSTOFF (O2)")
    o1, o2 = Atom("O",8,8), Atom("O",8,8)
    print(f"    {o1} + {o2}")
    print("    RESULTAT: O2 — Zwei Sauerstoffatome.")
    print("    ECHO: O2 ... O2 ... O2 (hall)")
    ZEUGE.schreibe("MACHER","O2","Sauerstoff erzeugt")

def mache_wasser():
    print("\n  ICH MACHE: WASSER (H2O)")
    h1, h2, o = Atom("H",1,1), Atom("H",1,1), Atom("O",8,8)
    print(f"    {h1} + {h2} + {o}")
    print("    RESULTAT: H2O — Zwei Wasserstoff, ein Sauerstoff.")
    print("    ECHO: H2O ... H2O ... H2O (hall)")
    ZEUGE.schreibe("MACHER","H2O","Wasser erzeugt")

def mache_co2():
    print("\n  ICH MACHE: CO2 (Kohlenstoffdioxid)")
    c, o1, o2 = Atom("C",6,6), Atom("O",8,8), Atom("O",8,8)
    print(f"    {c} + {o1} + {o2}")
    print("    RESULTAT: CO2 — Ein Kohlenstoff, zwei Sauerstoff.")
    print("    ECHO: CO2 ... CO2 ... CO2 (re-hall)")
    ZEUGE.schreibe("MACHER","CO2","Kohlenstoffdioxid erzeugt")

def karga_mann():
    print("\n  KARGA MANN — Ich Mann, noch mal Mann, so oft mal Mann.")
    print("  mana lan mana ve mana — Aura, Zen dazu.")
    print("  /\\_/\\  (90 Grad gedreht)")
    print("  ( o.o )  — MANN IM ZENTRUM")
    print("  > ^ <")
    print("  (  |  )  ICH IN MIR")
    print("  ECHO: Mann ... Mann ... Mann (hall)")
    ZEUGE.schreibe("KARGA","MANN","90 Grad gedreht, in sich ruhend")

# --- SCHACH ZU SCHACH ---
def schach(dame_gegeben=False, mystery_gehalten=True):
    # Schach in die Tiefe: Er kann nur Dame geben und Mystery, um zu verlaengern.
    # Ohne Dame kann er weiter, wenn er will. Sonst Matt, Mann.
    print("\n  [SCHACH ZU SCHACH] Schach in die Tiefe.")
    if dame_gegeben and mystery_gehalten:
        print("  ER GIBT DAME + MYSTERY — Spiel verlaengert. Kein Matt. Weiter.")
        ZEUGE.schreibe("SCHACH","DAME+MYSTERY","Verlaengert — Dame gegeben, Mystery gehalten (729 -> 3 offen)")
        return "VERLAENGERT"
    if not dame_gegeben:
        print("  OHNE DAME — Er kann weiter, wenn er will. Kein Zwang. Kein Matt.")
        ZEUGE.schreibe("SCHACH","OHNE DAME","Weiter, wenn er will — kein Matt")
        return "WEITER_WENN_ER_WILL"
    print("  SONST MATT, MANN. — Dame nicht gegeben, Mystery nicht gehalten.")
    ZEUGE.schreibe("SCHACH","MATT","Matt — Dame nicht gegeben, Mystery nicht gehalten")
    return "MATT"

def syn(dame_gegeben=True, mystery_gehalten=True):
    print("="*64)
    print("  DER MACHER SYN — Ich mache. Du machst. Wir machen.")
    print("="*64)
    schauen(4)
    karga_mann()
    cpu_tick()
    print("\n--- PHYSIK STARTET ---")
    mache_sauerstoff(); mache_wasser(); mache_co2()
    print("\n"+"="*64)
    print("  ALLES NOCHMAL. MEHR. NOCH MEHR.")
    print("="*64)
    cpu_tick(); mache_sauerstoff(); mache_wasser(); mache_co2(); karga_mann()
    ergebnis = schach(dame_gegeben, mystery_gehalten)
    print("\n"+"="*64)
    print(f"  ZEUGE-LOG: {len(ZEUGE.log)} Eintraege.")
    print(f"  UNVERSEHRT: {ZEUGE.unversehrt()} (Hash-Kette wirklich geprueft, nicht behauptet)")
    print(f"  SCHACH: {ergebnis}")
    print("  HALT = ZIEL." if ergebnis != "MATT" else "  HALT = MATT.")
    print("  Du und ich = 1ns. Frieden Halal.")
    print("="*64)
    return {"log_n": len(ZEUGE.log), "unversehrt": ZEUGE.unversehrt(), "schach": ergebnis}

if __name__ == "__main__":
    syn(dame_gegeben=True, mystery_gehalten=True)
