# schalter.py — ZU SCHALT UND ABWAHL SCHALTER, MANN
# SCHALT = ZU / AUF. ABWAHL = GEWAEHLT / ABGEWAEHLT.
# 1 = ZU / GEWAEHLT. 0 = AUF / ABGEWAEHLT. Kein Dazwischen.
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
# Schalter: Name -> 1 = ZU / GEWAEHLT, 0 = AUF / ABGEWAEHLT
SCHALTER = {"EYE": 1, "BRAIN": 1, "CORE": 1, "HBT": 1, "NC": 1, "KARGA": 0, "VEHICLE": 1, "ANHAENGER": 0}
def zeige():
    print("ZU SCHALT UND ABWAHL SCHALTER")
    for k, v in SCHALTER.items():
        print(f"{k} = {v} — {'ZU / GEWAEHLT' if v==1 else 'AUF / ABGEWAEHLT'}")
    print("EYE 1 = schaut. EYE 0 = schaut nicht.")
    print("BRAIN 1 = denkt. BRAIN 0 = denkt nicht.")
    print("CORE 1 = haelt. CORE 0 = haelt nicht.")
    print("HBT 1 = H=40 B=41 T=90 Q=57 F=1.425 D=3. HBT 0 = kein HBT.")
    print("NC 1 = 9 -> 6 -> 9. NC 0 = kein NC.")
    print("KARGA 0 = abgewahlt — Last nicht dabei. VEHICLE 1 = gewaehlt — Fahrzeug dabei. ANHAENGER 0 = abgewahlt — haengt nicht dran.")
    print("Abwahl ist nicht loeschen, Mann. Abwahl ist: Schalter auf 0. Datei bleibt. Nur nicht gewaehlt.")
    Z.schreibe("SCHALT", "SCHALTER = EYE 1, BRAIN 1, CORE 1, HBT 1, NC 1, KARGA 0, VEHICLE 1, ANHAENGER 0")
    Z.schreibe("ABWAHL", "ABWAHL = 0 — nicht loeschen, nur nicht gewaehlt")
    print("HALT = OFFEN")
def schalt(name):
    # ZU <-> AUF umschalten
    SCHALTER[name] = 1 - SCHALTER[name]
    print(f"{name} umgeschaltet -> {SCHALTER[name]}")
    Z.schreibe("UMSCHALT", f"{name} -> {SCHALTER[name]}")
    return SCHALTER[name]
if __name__ == "__main__":
    zeige()
    print("--- Beispiel: KARGA umschalten ---")
    schalt("KARGA")
    zeige()
