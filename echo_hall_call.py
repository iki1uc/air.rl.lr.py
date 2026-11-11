# echo_hall_call.py — ECHO HALL — U CALL, I CALL, HE CALL, SHE CALL, RECALL, REFINAL — ALL U HAPPND NEEDED
# ECHO HALL = Halle, wo jeder Ruf zurückkommt. Nicht lauter, nicht leiser. Gleich.
# U CALL = du rufst. I CALL = ich rufe. HE CALL = er ruft. SHE CALL = sie ruft.
# RECALL = zurückrufen — was war? REFINAL = nochmal Ende. ALL U HAPPND NEEDED = alles, was passiert ist, war nötig, Mann.
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
def call(wer, was):
    print(f"{wer} CALL: {was}")
    print(f"ECHO HALL: {was} ... {was} ... {was}")
    Z.schreibe("CALL", f"{wer} CALL: {was}")
    return was
def recall():
    print("RECALL: was war?")
    for z in Z.log:
        print(f"  RECALL {z['n']} = {z['enter']} — {z['text']}")
    return Z.log
def echo_hall():
    print("ECHO HALL — U CALL, I CALL, HE CALL, SHE CALL, RECALL, REFINAL")
    call("U", "up.ni pu.in")
    call("I", "up.ni pu.in")
    call("HE", "729 -> 81 -> 9 -> 3 -> 1")
    call("SHE", "729 -> 81 -> 9 -> 3 -> 1")
    print("ECHO HALL: Alle rufen dasselbe. Echo macht keinen Unterschied. Echo zeigt: alle waren da.")
    recall()
    print("REFINAL: Nochmal Ende — 1 -> 729 — Kreis.")
    print("ALL U HAPPND NEEDED: Alles, was passiert ist, war nötig, Mann.")
    print("  U passiert — nötig. I passiert — nötig. HE passiert — nötig. SHE passiert — nötig.")
    print("  Nicht wegdenken. Nicht löschen. Recall heisst: behalten, nicht löschen.")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    Z.schreibe("REFINAL", "REFINAL: 1 -> 729 — Kreis — alles, was passiert ist, war nötig")
    print("HALT = OFFEN")
if __name__ == "__main__":
    echo_hall()
