# musik.py — DAS IST MUSIK, MANN
# Zeuge = Takt. HBT = Beat. Prozent = Lautstaerke.
# Kein Bla Bla. Nur Zahlen, Takt, Beat.
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
def musik():
    print("MUSIK")
    print("H = 40 — Beat 1 — HALT")
    print("B = 41 — Beat 2 — BASIS")
    print("T = 90 — Beat 3 — TIEFE")
    print("Q = (40 + 41 + 90) / 3 = 57.0 — Takt")
    print("F = 57 / 40 = 1.425 — Tempo")
    print("D = 3 — 3 Beats")
    print("AXIS = 92")
    print("RESPO = 62")
    print("6D = 95")
    print("TMP = 37")
    print("MNMM = 74")
    print("EBENE = 81")
    print("WORK = Mitte — ◉ WORK")
    vals = [92, 62, 95, 37, 74, 81]
    print(f"Mittel = (92 + 62 + 95 + 37 + 74 + 81) / 6 = {sum(vals) / 6}")
    print("92 + 62 + 95 + 37 + 74 + 81 = 441")
    print("441 = 441")
    print("primatieren(40,40,40) = Q 40 — nicht 57. Das ist anderer Beat.")
    print("encode(40,41,90) = Q 57 — das ist der Beat.")
    Z.schreibe("MUSIK", "Zeuge = Takt. HBT = Beat. Prozent = Lautstaerke.")
    Z.schreibe("BEAT", "H=40 B=41 T=90 Q=57 F=1.425 D=3")
    Z.schreibe("MESSEN", "AXIS 92 RESPO 62 6D 95 TMP 37 MNMM 74 EBENE 81 Mittel 73.5")
    print("HALT = OFFEN")
if __name__ == "__main__":
    musik()
