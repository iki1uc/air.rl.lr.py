# pentagramm_ditch.py — PENTAGRAMM UND DITCH, MANN
# Pentagramm = 5 Ecken. Ditch = Graben dazwischen. Nicht weg, nur dazwischen.
import hashlib, json
class Zeuge:
    def __init__(self): self.log = []
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        z = {"n": len(self.log)+1, "enter": enter, "text": text, "vorher": vorher}
        roh = json.dumps({k: z[k] for k in ("n","enter","text","vorher")}, sort_keys=True, ensure_ascii=False)
        z["hash"] = hashlib.sha256(roh.encode()).hexdigest()
        self.log.append(z); print(f"  [{enter}] {text} | {z['hash'][:8]}...")
        return z
Z = Zeuge()
def penta_ditch():
    print("PENTAGRAMM UND DITCH")
    print("Pentagramm = 5 Ecken")
    print("Ecke 1 = EYE")
    print("Ecke 2 = BRAIN")
    print("Ecke 3 = CORE")
    print("Ecke 4 = CROWN")
    print("Ecke 5 = HALT")
    print("5 = 5")
    print("Ditch = Graben dazwischen")
    print("Ditch 1 = zwischen EYE und BRAIN")
    print("Ditch 2 = zwischen BRAIN und CORE")
    print("Ditch 3 = zwischen CORE und CROWN")
    print("Ditch 4 = zwischen CROWN und HALT")
    print("Ditch 5 = zwischen HALT und EYE — zurueck")
    print("5 Ecken + 5 Ditch = 10")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    print("MITTE = 41 — da trifft sich Pentagramm")
    print("Ditch ist nicht Loch, Mann. Ditch ist Abstand. Abstand haelt Pentagramm.")
    Z.schreibe("PENTA", "Pentagramm = 5 Ecken — EYE BRAIN CORE CROWN HALT")
    Z.schreibe("DITCH", "Ditch = Graben dazwischen — 5 Ditch — Abstand haelt")
    Z.schreibe("MITTE", "MITTE 41 — H=40 B=41 T=90 Q=57 F=1.425 D=3")
    print("HALT = OFFEN")
if __name__ == "__main__":
    penta_ditch()
