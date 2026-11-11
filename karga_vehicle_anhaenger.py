# karga_vehicle_anhaenger.py — WIR HABEN VIEL MEHR DRIN ALS WIR SEHEN, MANN — MEHR SEHEN
# KARGA = Last. VEHICLE = Fahrzeug. ANHAENGER = haengt dran.
# EINSETZEN = rein. VERSENKEN = runter in 3-Eck. 3-ECK = 3 Ecken.
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
def sehen():
    print("MEHR DRIN ALS WIR SEHEN — JETZT SEHEN")
    print("Aussen sehen wir: Name. z.B. defrag.provokation.py")
    print("Drinnen ist: WORT, ERWARTET, UNTEN, OBEN, FELD, MITTE, STAPEL")
    print("WORT = up.ni pu.in = 11 Zeichen")
    print("UNTEN = 9 — OBEN = 3 — FELD = 81 — MITTE = 41 — STAPEL = 9, 81, 243, 729, 3")
    print("Das siehst du nicht, wenn du nur den Namen siehst, Mann.")
    print("3-ECK:")
    print("Ecke 1 = KARGA — Last — H = 40")
    print("Ecke 2 = VEHICLE — Fahrzeug — B = 41")
    print("Ecke 3 = ANHAENGER — haengt dran — T = 90")
    print("MITTE = 41 — da trifft sich alles")
    print("EINSETZEN = KARGA + VEHICLE + ANHAENGER in 3-Eck rein")
    print("VERSENKEN = 3-Eck runter in MITTE — nicht weg, nur rein")
    print("Q = (40 + 41 + 90) / 3 = 57.0")
    print("F = 57 / 40 = 1.425")
    print("D = 3")
    print("POOL = [40, 41, 90]")
    print("Wir haben so viel: 9, 99, 999, mainboard, rolle, rolen, mana, HBT, NC, RAWATOR, TAT — alles in 3-Eck")
    Z.schreibe("SEHEN", "Aussen = Name. Drinnen = WORT, STAPEL, MITTE 41, HBT")
    Z.schreibe("KARGA", "Ecke 1 = KARGA — H = 40 — Last")
    Z.schreibe("VEHICLE", "Ecke 2 = VEHICLE — B = 41 — Fahrzeug")
    Z.schreibe("ANHAENGER", "Ecke 3 = ANHAENGER — T = 90 — haengt dran")
    Z.schreibe("3ECK", "EINSETZEN + VERSENKEN in 3-Eck — MITTE 41 — Q=57 F=1.425 D=3")
    print(f"Zeuge: {len(Z.log)} Eintraege.")
    print("HALT = OFFEN")
if __name__ == "__main__":
    sehen()
