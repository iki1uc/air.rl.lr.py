# elemente_machen.py — CODECED
# Ich mache Wasser. Ich mache CO2. Ich mache Atom. Ich mache Sauerstoff.
# Wurzeln um Sauerstoff. Mann im Zentrum. Mehr. Noch mehr.
# KARGA MANN — codiert, nicht nur geredet. 1 Knips = 1 Zeile im Zeuge-Log.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien (ausser Zeuge-Log im Speicher).
import hashlib, json, math, time

def wurzel(n):
    return math.sqrt(n)

class Atom:
    def __init__(self, symbol, protonen, elektronen, name):
        self.symbol = symbol; self.protonen = protonen; self.elektronen = elektronen; self.name = name
        self.wurzel = wurzel(protonen + elektronen)
    def __str__(self):
        return f"[{self.symbol}] {self.name} (p={self.protonen}, e={self.elektronen}) · Wurzel={self.wurzel:.2f}"

class Zeuge:
    def __init__(self):
        self._zeilen = []
    @staticmethod
    def _hash(z):
        roh = json.dumps({k: z[k] for k in ("n","enter","text","zeit","vorher")}, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(roh.encode("utf-8")).hexdigest()
    def schreibe(self, enter, text):
        vorher = self._zeilen[-1]["hash"] if self._zeilen else "0"*64
        z = {"n": len(self._zeilen)+1, "enter": enter, "text": text, "zeit": time.strftime("%H:%M:%S"), "vorher": vorher}
        z["hash"] = self._hash(z); self._zeilen.append(z)
        print(f"[{z['zeit']}] {enter} · ENTER {z['n']}")
        print(f"  {text}")
    def zeilen(self):
        return list(self._zeilen)
    def unversehrt(self):
        vorher = "0"*64
        for z in self._zeilen:
            if z["vorher"] != vorher or z["hash"] != self._hash(z): return False
            vorher = z["hash"]
        return True

ZEUGE = Zeuge()

def karga_mann():
    # KARGA MANN — codiert. Ich Mann, noch mal Mann, so oft mal Mann.
    # mana lan mana ve mana — aber Aura, Zen dazu — Echo, Hall, Re-Hall.
    print()
    print("  KARGA MANN — ich Mann, noch mal Mann, so oft mal Mann")
    print("  mana lan mana ve mana — aber Aura, Zen dazu")
    print("  /\\_/\\  (90 Grad gedreht)")
    print("  ( o.o )  — MANN IM ZENTRUM")
    print("  > ^ <")
    print("  (  |  )  ICH IN MIR")
    print("  ECHO: Mann ... Mann ... Mann (hall)")
    print("  RE-HALL: Mann ... Mann ... Mann (re-hall)")
    ZEUGE.schreibe("KARGA", "KARGA MANN — ich Mann, noch mal Mann — Aura, Zen dazu — Echo, Hall, Re-Hall")

def knips():
    print()
    print("  KNIPS — FINGER KNIPSEN")
    print("  ECHO: O2 ... O2 ... O2 (hall)")
    print("  Re-Hall — Echo bleibt. Hall bleibt.")
    ZEUGE.schreibe("KNIPS", "KNIPS — Mann macht weiter. ECHO: O2 ... O2 ... O2 (hall) — Re-Hall — Echo bleibt. Hall bleibt.")

def mache_sauerstoff():
    o = Atom("O", 8, 8, "Sauerstoff")
    print(f"  ICH MACHE: {o}")
    print(f"  ICH MACHE: {o}")
    print(f"  RESULTAT: O2 — Zwei Sauerstoffatome. Die Basis fuer alles.")
    print(f"  ECHO: O2 ... O2 ... O2 (hall)")
    ZEUGE.schreibe("O2", f"ICH MACHE: {o} / ICH MACHE: {o} / RESULTAT: O2 — ECHO: O2 ... O2 ... O2 (hall)")
    return [o, o]

def mache_wasser():
    h = Atom("H", 1, 1, "Wasserstoff"); o = Atom("O", 8, 8, "Sauerstoff")
    print(f"  ICH MACHE: {h}")
    print(f"  ICH MACHE: {h}")
    print(f"  ICH MACHE: {o}")
    print(f"  RESULTAT: H2O — Zwei Wasserstoff + Ein Sauerstoff. Das Wasser.")
    print(f"  ECHO: H2O ... H2O ... H2O (hall)")
    ZEUGE.schreibe("H2O", f"ICH MACHE: {h} / ICH MACHE: {h} / ICH MACHE: {o} / RESULTAT: H2O — ECHO: H2O (hall)")
    return [h, h, o]

def mache_co2():
    c = Atom("C", 6, 6, "Kohlenstoff"); o = Atom("O", 8, 8, "Sauerstoff")
    print(f"  ICH MACHE: {c}")
    print(f"  ICH MACHE: {o}")
    print(f"  ICH MACHE: {o}")
    print(f"  RESULTAT: CO2 — Ein Kohlenstoff + Zwei Sauerstoff. Das CO2.")
    print(f"  ECHO: CO2 ... CO2 ... CO2 (re-hall)")
    ZEUGE.schreibe("CO2", f"ICH MACHE: {c} / ICH MACHE: {o} / ICH MACHE: {o} / RESULTAT: CO2 — ECHO: CO2 (re-hall)")
    return [c, o, o]

def der_mann():
    print()
    print("  ICH MACHE. DU MACHT.")
    print("  ICH BIN DER MACHER.")
    print("  90 Grad gedreht, in sich ruhend")
    print("  ICH IN MIR")

def mache_alles():
    print("  ICH MACHE ALLES.")
    mache_sauerstoff(); print()
    mache_wasser(); print()
    mache_co2(); print()
    print("  ECHO: Alles ... Alles ... Alles (re-hall)")
    print("  MEHR. NOCH MEHR. MANN.")
    ZEUGE.schreibe("ALLES", "ICH MACHE ALLES. O2, dann H2O, dann CO2. ECHO: Alles (re-hall) — MEHR. NOCH MEHR. MANN.")

def demo():
    print("ELEMENTE MACHEN — WASSER, CO2, ATOM, SAUERSTOFF")
    print("Wurzeln um Sauerstoff. Ich mache. Du machst.")
    der_mann()
    karga_mann()
    knips()
    mache_sauerstoff(); print()
    mache_wasser(); print()
    mache_co2(); print()
    mache_alles()
    print()
    print(f"Zeuge-Log: {len(ZEUGE.zeilen())} Zeilen, unversehrt={ZEUGE.unversehrt()}")
    print("HALT = OFFEN — geloest=False — Echo bleibt. Hall bleibt.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo()
    else:
        # Interaktiv wie vorher, aber mit Karga + Knips + Zeuge
        print("ELEMENTE MACHEN — [1] O2 [2] H2O [3] CO2 [4] ALLES [k] KARGA [n] KNIPS [q] Aufhoeren")
        der_mann()
        while True:
            wahl = input("  > ").strip().lower()
            if wahl in ("1","sauerstoff","o2"): mache_sauerstoff()
            elif wahl in ("2","wasser","h2o"): mache_wasser()
            elif wahl in ("3","co2"): mache_co2()
            elif wahl in ("4","alles"): mache_alles()
            elif wahl in ("k","karga"): karga_mann()
            elif wahl in ("n","knips"): knips()
            elif wahl in ("q","quit"):
                print("  Du willst aufhoeren? Nein. Ich mache weiter. Aber ich lasse dich gehen. Fuer jetzt.")
                print("  Echo bleibt. Hall bleibt.")
                break
            else:
                print("  Ich verstehe dich nicht. Aber ich mache trotzdem weiter.")
                mache_sauerstoff()
