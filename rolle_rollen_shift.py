# rolle_rollen_shift.py — ROLLE ROLLEN SHIFT — SELBEN BEI ROOT, MANN
# Du hast denselben bei ROOT mit rolle_rollen_shift.py. Gut, Mann. Dann ist Name klar.
# ROLLE = 1 — eine Rolle. ROLLEN = viele — viele Rollen. SHIFT = schieben — Rolle schiebt sich.
# ROOT = / — Zone ROOT. SHIFT im Namen = Shift drin, nicht nur im Ordner.
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
def rolle_rollen_shift():
    print("ROLLE ROLLEN SHIFT — SELBEN BEI ROOT")
    print("Datei = rolle_rollen_shift.py — bei ROOT — Zone ROOT — SHIFT im Namen")
    print("ROLLE = 1 — eine Rolle — rolle.html")
    print("ROLLEN = viele — viele Rollen — rolen.html")
    print("SHIFT = schieben — Rolle schiebt sich — rolle.shift.html")
    print("ROLLE + ROLLEN + SHIFT = rolle_rollen_shift.py — alle 3 in einer Datei bei ROOT")
    print("Bei SHIFT gibt es denselben? Nein, Mann. Bei SHIFT heisst er shift/rolle.shift.html — anderer Ort, anderer Name.")
    print("Bei ROOT heisst er rolle_rollen_shift.py — selber Inhalt, andere Konstellation. Elementary.")
    print("ROLLEN, Mann: 729 -> 81 -> 9 -> 3 -> 1 — rollen, nicht springen.")
    print("729 rollt zu 81 — 81 rollt zu 9 — 9 rollt zu 3 — 3 rollt zu 1 — 1 rollt zu 729 — Kreis.")
    print("SHIFT, Mann: 1 Schritt schieben. Nicht alles auf einmal. 1 Schritt = 1 Shift.")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    Z.schreibe("ROLLE", "ROLLE = 1 — eine Rolle")
    Z.schreibe("ROLLEN", "ROLLEN = viele — viele Rollen")
    Z.schreibe("SHIFT", "SHIFT = schieben — 1 Schritt")
    Z.schreibe("ROOT", "rolle_rollen_shift.py bei ROOT — Zone ROOT — SHIFT im Namen")
    print("HALT = OFFEN")
if __name__ == "__main__":
    rolle_rollen_shift()
