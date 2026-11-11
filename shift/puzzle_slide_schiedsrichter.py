# puzzle_slide_schiedsrichter.py — PUZZLE, SLIDE, SCHIEDSRICHTER DAUMEN, MANN
# Kein Wette, kein Shill. Nur: Puzzle, Slide, Daumen.
# Puzzle = 9 Teile. Slide = 1 Teil schieben. Zerreissen = 1 Teil raus = Puzzle nicht mehr ganz.
# Schiedsrichter = Daumen hoch = 1, Daumen runter = 0. Daumen entscheidet, nicht Wette.
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
def spiel():
    print("PUZZLE, SLIDE, SCHIEDSRICHTER DAUMEN")
    print("Puzzle = 9 Teile — 9 = 9")
    print("Slide = 1 Teil schieben — 9 bleibt 9, nur anderer Ort")
    print("Zerreissen = 1 Teil raus — 9 - 1 = 8 — Puzzle nicht mehr ganz")
    print("8 != 9 — Puzzle kaputt, Mann")
    print("Soccer = Spiel — 2 Teams — Ball — Tor")
    print("Wette = nicht spielen, Mann. Wette ist raten auf Geld. Raten ist nicht messen.")
    print("Shill = nicht ehrlich, Mann. Shill tut so, als ob er spielt, aber er wirbt nur. Nicht machen.")
    print("Schiedsrichter Daumen = entscheidet")
    print("Daumen hoch = 1 — weiter")
    print("Daumen runter = 0 — halt")
    print("Daumen = 1 oder 0 — kein Dazwischen")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    Z.schreibe("PUZZLE", "Puzzle = 9 Teile")
    Z.schreibe("SLIDE", "Slide = 1 Teil schieben — 9 bleibt 9")
    Z.schreibe("ZERREISSEN", "Zerreissen = 9 - 1 = 8 — Puzzle nicht mehr ganz")
    Z.schreibe("SCHIEDS", "Schiedsrichter Daumen = 1 hoch / 0 runter — entscheidet")
    Z.schreibe("KEIN", "Kein Wette, kein Shill — nur messen, nicht raten, nicht werben")
    print("HALT = OFFEN")
if __name__ == "__main__":
    spiel()
