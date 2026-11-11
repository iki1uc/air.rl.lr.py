# quatscher.py — MACH ES QUATSCHER, MANN
# Quatscher = noch mehr Quatsch, noch mehr spielen, noch mehr Mann.
# Aber ehrlich: Quatsch steht drauf, wo Quatsch drin ist. Nicht versteckt.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
import hashlib, json
class Zeuge:
    def __init__(self): self.log = []
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        roh = json.dumps({"n": len(self.log)+1, "enter": enter, "text": text, "vorher": vorher}, sort_keys=True)
        h = hashlib.sha256(roh.encode()).hexdigest()
        self.log.append(h); print(f"  [{enter}] {text} | {h[:8]}...")
Z = Zeuge()
def quatscher():
    print("MACH ES QUATSCHER, MANN")
    print("Quatsch x3. Mann x3. So sosso. Lol. Aber verrundet, Mann.")
    Z.schreibe("QUATSCH1", "Quatsch 1 — Ich mach doch Quatsch, Mann — und sag es.")
    Z.schreibe("QUATSCH2", "Quatsch 2 — U DU — U und Du — Quatsch zusammen, Mann")
    Z.schreibe("QUATSCH3", "Quatsch 3 — XI IX IO OI IQ QI — Quatsch vor rueck auf ab rein raus")
    Z.schreibe("QUATSCH4", "Quatsch 4 — IN NI MANN — In Ni Mann — Quatsch Mann, Mehr Mann")
    Z.schreibe("QUATSCH5", "Quatsch 5 — KASPAROV KASPAROV KASPAROV — Quatsch Schach zu Schach")
    Z.schreibe("QUATSCH6", "Quatsch 6 — RAABE MANN EYE MANN — Kraeh Kraeh Kraeh — Quatsch Rabe")
    Z.schreibe("QUATSCH7", "Quatsch 7 — SCHHAEFERZUG B H T — Quatsch B H T — Quatsch Matt, Mann")
    print("Quatsch x7. Mann x7. So sosso x7.")
    print(f"Zeuge: {len(Z.log)} Zeilen. HALT = OFFEN. Echo bleibt. Hall bleibt.")
    print("ECO: QUATSCHER — Quatsch gesagt, Quatsch gezeugt, Quatsch gespielt. Ehrlich, Mann.")
    print("FUNKTION: quatscher() -> Quatsch x7 -> 1 Ehrlichkeit.")
if __name__ == "__main__":
    quatscher()
