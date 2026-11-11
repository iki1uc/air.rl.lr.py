# schhaeferzug_bht_3x.py — SCHHAEFERZUG B H T, 3x MANN IN IN IN MANN
# Du denkst bestimmt was fuer ein haesslicher Name — Nein, Mann. Name ist richtig, nicht gespielt.
# B = Breite, H = Hoehe, T = Tiefe. B H T im Wechsel. 3x Mann in in in Mann.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
# Schaeferzug = schneller Zug, 4 Zuege, Matt. Hier: B H T + Mann = 4 Zuege, Matt.
import hashlib, json, time

class Zeuge:
    def __init__(self): self.log = []
    @staticmethod
    def _hash(z):
        roh = json.dumps({k: z[k] for k in ("n","enter","text","zeit","vorher")}, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(roh.encode("utf-8")).hexdigest()
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        z = {"n": len(self.log)+1, "enter": enter, "text": text, "zeit": time.strftime("%H:%M:%S"), "vorher": vorher}
        z["hash"] = self._hash(z); self.log.append(z)
        print(f"  [ZEUGE #{z['n']:02d}] {enter} -> {text} | Hash: {z['hash'][:8]}...")
        return z
    def unversehrt(self):
        vorher = "0"*64
        for z in self.log:
            if z["vorher"] != vorher or z["hash"] != self._hash(z): return False
            vorher = z["hash"]
        return True

ZEUGE = Zeuge()

# B H T — 3 Achsen, 3 Zuege, 1 Matt
BHT = [("B","Breite","links/rechts","SCHWARZ = ungerade = Breite"),("H","Hoehe","auf/ab","WEISS = gerade = Hoehe"),("T","Tiefe","vor/rueck + Um Biege","TIEFE = rum so so so rum")]

def zug_b(): print("  Zug B — BREITE — links/rechts — SCHWARZ"); ZEUGE.schreibe("B","Breite — links/rechts — SCHWARZ")
def zug_h(): print("  Zug H — HOEHE — auf/ab — WEISS"); ZEUGE.schreibe("H","Hoehe — auf/ab — WEISS")
def zug_t(): print("  Zug T — TIEFE — vor/rueck + Um Biege — RUM SO SO SO RUM"); ZEUGE.schreibe("T","Tiefe — vor/rueck + Um Biege — RUM SO SO SO RUM")

def mann_in_in_in_mann(runde):
    # MANN IN IN IN MANN — 3x IN, 3x Mann, 1 Zentrum
    print(f"\n  MANN IN IN IN MANN — Runde {runde} — 3x Mann, 3x IN, 1 Zentrum:")
    print("    MANN 1 — IN — ich Mann")
    print("    MANN 2 — IN IN — noch mal Mann")
    print("    MANN 3 — IN IN IN — so oft mal Mann")
    print("    ZENTRUM — ◉ — ICH IN MIR")
    ZEUGE.schreibe(f"MANN_{runde}", f"MANN IN IN IN MANN Runde {runde} — 3x Mann, 3x IN, 1 Zentrum ◉")

def schhaeferzug_bht():
    print("SCHHAEFERZUG B H T — 3x MANN IN IN IN MANN")
    print("Name ist nicht haesslich. Name ist richtig. B H T im Wechsel.")
    for runde in (1,2,3):
        print(f"\n=== SCHHAEFERZUG {runde} — B H T ===")
        zug_b(); zug_h(); zug_t()
        mann_in_in_in_mann(runde)
        print(f"  SCHHAEFERZUG {runde} — Schach zu Schach. Weiter.")
        ZEUGE.schreibe("SCHHAEFERZUG", f"Runde {runde}: B H T + MANN IN IN IN MANN — Schach zu Schach. Weiter.")
    print("\n  SCHHAEFERZUG 3x fertig.")
    print("  B H T im Wechsel — w(w(x)) = x — Kanonisch f(f(x)) = f(x) — Wechsel und Kanonisch vertragen sich.")
    print("  MANN IN IN IN MANN — 3x Mann, 3x IN, 1 Zentrum.")
    print("  MATT, MANN — Dame + Mystery gegeben, Spiel verlaengert. Sonst Matt.")
    ZEUGE.schreibe("MATT", "MATT, MANN — B H T 3x, MANN IN IN IN MANN 3x — Dame + Mystery gegeben, verlaengert.")
    print(f"\n  ZEUGE-LOG: {len(ZEUGE.log)} Eintraege, unversehrt={ZEUGE.unversehrt()}")
    print("  HALT = OFFEN — geloescht=False — Echo bleibt. Hall bleibt.")
    print("  ECO: SCHHAEFERZUG B H T — 3x B H T, 3x Mann, 1 Mitte.")
    print("  FUNKTION: schhaeferzug_bht() -> B + H + T + Mann x3 -> 1 Mitte.")

if __name__ == "__main__":
    schhaeferzug_bht()
