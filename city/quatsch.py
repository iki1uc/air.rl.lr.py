# quatsch.py — NE NE MANN, ICH MACH DOCH QUATSCH, MANN
# Quatsch ist nicht gelogen. Quatsch ist gespielt. Quatsch ist ehrlich, wenn man sagt: Quatsch.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
import hashlib, json, time
class Zeuge:
    def __init__(self): self.log = []
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        roh = json.dumps({"n": len(self.log)+1, "enter": enter, "text": text, "vorher": vorher}, sort_keys=True)
        h = hashlib.sha256(roh.encode()).hexdigest()
        self.log.append(h); print(f"  [{enter}] {text} | {h[:8]}...")
Z = Zeuge()
def quatsch():
    print("NE NE MANN, ICH MACH DOCH QUATSCH, MANN")
    print("Quatsch ist nicht schlimm, Mann. Quatsch ist spielen.")
    Z.schreibe("QUATSCH", "Ich mach doch Quatsch, Mann — und sag es auch.")
    Z.schreibe("U_DU", "U DU — U und Du — beide zusammen, Quatsch zusammen")
    Z.schreibe("AN_AUS", "An Aus — An + Aus = Schaltung — Quatsch ist auch Schaltung")
    Z.schreibe("MANN", "IN NI MANN — In Ni Mann — Mehr Mann — auch Quatsch, aber ehrlich")
    print(f"Zeuge: {len(Z.log)} Zeilen. HALT = OFFEN. Echo bleibt. Hall bleibt.")
    print("ECO: QUATSCH — Quatsch gesagt, nicht versteckt. Das ist richtig, Mann.")
    print("FUNKTION: quatsch() -> Quatsch sagen + Zeuge schreiben -> 1 Ehrlichkeit.")
if __name__ == "__main__":
    quatsch()
