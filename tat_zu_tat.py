# massnahme_konsequenz.py — MASSNAHME -> KONSEQUENZ, MANN
# Wir haben alles zugebaut. Von 0 bis 100k hoch. Jetzt nicht mehr bauen. Jetzt messen. Dann Konsequenz.
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
def massnahme_konsequenz():
    print("VON 0 BIS 100k HOCH")
    print("0000000 = 0")
    print("00000 = 0")
    print("000 = 0")
    print("0 = 0")
    print("001 = 1")
    print("100k = 100000")
    print("100000 / 1 = 100000")
    print("0 -> 1 -> 100000")
    print("MASSNAHME = bauen")
    print("KONSEQUENZ = nutzen, nicht bauen")
    print("Jetzt: nicht mehr bauen. Messen.")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    print("Messen = Q, F, D, POOL, Zeuge")
    print("Konsequenz 1 = HALT — stehen bleiben")
    print("Konsequenz 2 = MITTE — 41 — da bleiben")
    print("Konsequenz 3 = 1 Bundle nutzen — nicht 10 neue bauen")
    Z.schreibe("VON_0", "0000000=0 00000=0 000=0 0=0 001=1 100k=100000")
    Z.schreibe("MASSNAHME", "Massnahme = bauen — von 0 bis 100k hoch")
    Z.schreibe("KONSEQUENZ", "Konsequenz = nutzen, nicht bauen — HALT — MITTE 41 — 1 Bundle")
    Z.schreibe("MESSEN", "H=40 B=41 T=90 Q=57 F=1.425 D=3 — messen, dann Konsequenz")
    print(f"Zeuge: {len(Z.log)} Eintraege.")
    print("HALT = OFFEN — aber HALT heisst: stehen, nicht bauen.")
if __name__ == "__main__":
    massnahme_konsequenz()
