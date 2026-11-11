# root_router.py — HOME NICHT BEI ROOT, MANN. DAS GIBT AERGER.
# ROOT = / — nur Wegweiser. HOME = /home — ein Ort. Nicht dasselbe.
# Wenn HOME bei ROOT ist, dann: / = HOME = INDEX = ROOT. Alles eins. Dann kann INDEX nicht mehr zu ORT und HOME und PQ routen, weil HOME schon ROOT ist. Kollision. Aerger.
# Richtig: INDEX steht bei ROOT und ROUTET zu ORT, HOME, PQ.
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
ROUTEN = {
    "/": "index.html — ROOT — Wegweiser, kein Ort",
    "/home": "home.html — HOME — Ort",
    "/ort": "ort.html — ORT — Ort",
    "/pq": "pq.html — PQ — Ort",
    "/tal": "tal.html — TAL — Ort",
    "/city": "city.html — CITY — Ort",
    "/shift": "shift/index.html — SHIFT — Ort",
}
def routen(weg):
    # INDEX soll zu ORT und HOME und PQ rein rooten — heisst: INDEX zeigt Weg, nicht INDEX ist HOME
    ziel = ROUTEN.get(weg)
    print(f"{weg} -> {ziel}")
    return ziel
def zeige():
    print("HOME NICHT BEI ROOT — DAS GIBT AERGER")
    print("ROOT = / — Wegweiser")
    print("HOME = /home — Ort, HOME = 40")
    print("ORT = /ort — Ort")
    print("PQ = /pq — Ort")
    print("Falsch: / = /home — dann ist HOME = ROOT = INDEX. Alles eins. Kollision.")
    print("Richtig: / = index.html — index routet zu /ort, /home, /pq")
    for w in ROUTEN:
        routen(w)
    print("INDEX soll zu ORT und HOME und PQ rein rooten — heisst:")
    print("INDEX -> ORT")
    print("INDEX -> HOME")
    print("INDEX -> PQ")
    print("INDEX ist nicht HOME. INDEX zeigt zu HOME.")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    Z.schreibe("ROOT", "ROOT = / — Wegweiser, kein Ort")
    Z.schreibe("HOME", "HOME = /home — Ort, nicht ROOT")
    Z.schreibe("ROUTEN", "INDEX -> ORT, INDEX -> HOME, INDEX -> PQ")
    print("HALT = OFFEN")
if __name__ == "__main__":
    zeige()
