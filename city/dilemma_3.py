# dilemma_3.py — DILEMMA: 1 IST ZU WENIG. 3 BEI BRINGEN.
# Ori alle, alle ori. Eye Brain. Die koennen nicht mal 3. Kapische.
# 9 Pentagramme + Prismatike im Wechsel. Das gabs noch nie.
# Wechsel Quant + Syn. Mach mach mach. In in in + Ni ni ni + Io oi + Xi ix.
# 3e die tanzen. 3fach Respekt Shufflen. 1ns 2t 3t.
# Zusammen als getrennt und zusammen. Atomic Pentagramm steht.
import hashlib, json
class Zeuge:
    def __init__(self): self.log = []
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        roh = json.dumps({"n": len(self.log)+1, "enter": enter, "text": text, "vorher": vorher}, sort_keys=True)
        h = hashlib.sha256(roh.encode()).hexdigest()
        self.log.append(h); print(f"  [{enter}] {text} | {h[:8]}...")
Z = Zeuge()
def dilemma():
    print("DILEMMA: 1 = zu wenig. 3 = bei bringen.")
    print("1 = 1")
    print("3 = 3")
    print("3 = 1 + 1 + 1")
    print("1ns = 1. 2t = 2. 3t = 3.")
    print("1ns + 2t + 3t = 6")
    print("6 = 1 + 2 + 3")
    print("9 = 3 x 3")
    print("9 Pentagramme = 9 x 5")
    print("9 x 5 = 45")
    print("45 = 45")
    print("Prismatike im Wechsel: P1 -> P2 -> P3 -> P1")
    print("Wechsel Quant + Syn: Q + S = Q S")
    print("In in in = 3 x IN")
    print("Ni ni ni = 3 x NI")
    print("Io oi = 2")
    print("Xi ix = 2")
    print("3e die tanzen: 1 tanzt, 2 tanzt, 3 tanzt")
    print("3fach Respekt Shufflen: 3 x Shuffle")
    print("Zusammen als getrennt: 3 = 3")
    print("Zusammen als zusammen: 3 = 1")
    print("3 = 3. 3 = 1. Beide.")
    print("Atomic Pentagramm steht: 5 = 5")
    Z.schreibe("DILEMMA", "1 = zu wenig. 3 = bei bringen.")
    Z.schreibe("NEUN", "9 = 3 x 3. 9 Pentagramme = 9 x 5 = 45.")
    Z.schreibe("WECHSEL", "Prismatike im Wechsel: P1 -> P2 -> P3 -> P1. Quant + Syn.")
    Z.schreibe("TANZ", "3e die tanzen: 1ns + 2t + 3t = 6. Zusammen als getrennt und zusammen.")
    Z.schreibe("ATOMIC", "Atomic Pentagramm steht: 5 = 5.")
    print(f"Zeuge: {len(Z.log)} Zeilen. HALT = OFFEN.")
if __name__ == "__main__":
    dilemma()
