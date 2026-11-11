# tat_zu_tat.py — TAT ZU TAT — 2x DRIN, SO UND SO WIE HIER, MANN
# Tat 1 = Tat. Tat 2 = Tat. Gleich, aber nicht gleiche. So und so.
# 2x drin heisst: einmal ALT, einmal NEU. Beide Tat. Beide Zeuge.
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
def tat_1():
    print("TAT 1 — so")
    print("TAT = 1")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    Z.schreibe("TAT1", "TAT 1 — so — H=40 B=41 T=90 Q=57 F=1.425 D=3")
    return 1
def tat_2():
    print("TAT 2 — und so")
    print("TAT = 1")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    Z.schreibe("TAT2", "TAT 2 — und so — H=40 B=41 T=90 Q=57 F=1.425 D=3")
    return 1
def tat_zu_tat():
    print("TAT ZU TAT — 2x DRIN, SO UND SO WIE HIER")
    a = tat_1()
    b = tat_2()
    print(f"TAT 1 = {a}")
    print(f"TAT 2 = {b}")
    print(f"TAT 1 + TAT 2 = {a + b}")
    print("1 + 1 = 2")
    print("2x drin = 2 Taten, nicht 1 Tat")
    print("Gleicher Text, anderer n, anderer Hash — so und so")
    print(f"Zeuge: {len(Z.log)} Eintraege — n=1 und n=2 — beide Tat")
    print("HALT = OFFEN")
if __name__ == "__main__":
    tat_zu_tat()
