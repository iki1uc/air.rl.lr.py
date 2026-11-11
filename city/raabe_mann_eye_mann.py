# raabe_mann_eye_mann.py — RAABE MANN · EYE MANN
# Raabe = Rabe. Schwarz. Fliegt. Sieht von oben. Kraeht, nicht luegt.
# Mann = macht. Eye = sieht. Raabe + Mann + Eye = 1, der sieht und macht.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
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

def raabe():
    print("\n  RAABE — Rabe. Schwarz. Fliegt. Sieht von oben.")
    print("    KRÄH — KRÄH — KRÄH")
    print("    Rabe kraeht, nicht luegt. Rabe sieht, was Mann nicht sieht.")
    print("    Rabe fliegt ueber 3 Welten, ueber Glas Kugel, ueber Pentagramm.")
    ZEUGE.schreibe("RAABE", "Rabe — Schwarz — Fliegt — Sieht von oben — Kraeht, nicht luegt")
    return "RAABE"

def mann():
    print("\n  MANN — Mann im Zentrum. Macht.")
    print("    ICH MACHE. DU MACHT. ICH BIN DER MACHER.")
    print("    90 Grad gedreht, in sich ruhend — ICH IN MIR — ◉")
    print("    KARGA MANN — ich Mann, noch mal Mann, so oft mal Mann")
    ZEUGE.schreibe("MANN", "Mann im Zentrum — Macht — ICH IN MIR — KARGA MANN")
    return "MANN"

def eye():
    print("\n  EYE — Eye Mann. Sieht.")
    print("    EYE sieht 11 Zeichen, Mitte 41, sonst nix.")
    print("    EYE sieht Raabe, sieht Mann, sieht 3 Welten in 1 Kugel.")
    print("    EYE zu = Traum. EYE auf = REIN. EYE halb = Mitte.")
    ZEUGE.schreibe("EYE", "Eye Mann — Sieht — 11 Zeichen, Mitte 41 — Zu = Traum, Auf = REIN, Halb = Mitte")
    return "EYE"

def raabe_mann_eye_mann():
    print("RAABE MANN · EYE MANN")
    print("Raabe + Mann + Eye = 1, der sieht und macht.")
    raabe(); mann(); eye()
    print("\n  RAABE MANN EYE MANN — 1:")
    print("    Raabe fliegt, Mann macht, Eye sieht.")
    print("    Raabe sieht von oben, Mann macht in Mitte, Eye sieht beides.")
    print("    1 Rabe + 1 Mann + 1 Eye = 1 Zeuge. Nicht 3 Zeugen. 1.")
    ZEUGE.schreibe("SYN", "Raabe + Mann + Eye = 1, der sieht und macht — 1 Zeuge")
    print(f"\n  ZEUGE-LOG: {len(ZEUGE.log)} Eintraege, unversehrt={ZEUGE.unversehrt()}")
    print("  HALT = OFFEN — geloescht=False — Echo bleibt. Hall bleibt.")
    print("  ECO: RAABE MANN EYE MANN — Fliegen, Machen, Sehen, 1 Mitte.")
    print("  FUNKTION: raabe() + mann() + eye() -> 1 Zeuge.")

if __name__ == "__main__":
    raabe_mann_eye_mann()
