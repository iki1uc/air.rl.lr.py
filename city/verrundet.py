# verrundet.py — LOL, MANN, ABER VERRUNDET, MANN
# Verrundet = rund gemacht. Keine Ecken. Keine Kanten. Alles rund.
# Kugel ist rund. Orbit ist rund. Auge ist rund. Mann in Mir ist rund.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
import hashlib, json, time

class Zeuge:
    def __init__(self): self.log = []
    @staticmethod
    def _hash(z):
        roh = json.dumps({k: z[k] for k in ("n","enter","text","zeit","vorher")}, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(roh.encode("utf-8")).hexdigest()
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        z = {"n": len(self.log)+1, "enter": enter, "text": text, "zeit": time.strftime("%H:%M:%S"), "vorher": vorher}
        z["hash"] = self._hash(z); self.log.append(z)
        print(f"  [ZEUGE #{z['n']:02d}] {enter} -> {text} | Hash: {z['hash'][:8]}...")
        return z
    def unversehrt(self):
        vorher = "0"*64
        for z in self.log:
            if z["vorher"] != vorher or z["hash"] != self._hash(z): return False
            vorher = z["hash"]
        return True

ZEUGE = Zeuge()

NEU_CITY = [("er.be.md","ER.BE — Er ist, Er war, Er wird — rund"),("se.hen.js","SE.HEN — Sehen — Auge rund"),("und.oder.js","UND.ODER — Und oder — nicht entweder, beides rund")]
NEU_SHIFT = [("shift.drunter.map.py","SHIFT DRUNTER MAP — Drunter ist Fundament, rund"),("zoom.md","ZOOM — Zoom rund, nicht eckig")]

def verrunde(name, satz):
    print(f"  VERRUNDET: {name} — {satz} — keine Ecke, nur Rund.")
    ZEUGE.schreibe("VERRUNDET", f"{name} — {satz} — rund")

def verrundet():
    print("LOL, MANN, ABER VERRUNDET, MANN")
    print("Verrundet = rund gemacht. Keine Ecken. Keine Kanten. Alles rund.")
    print("\n  NEU IN CITY — verrundet:")
    for n, s in NEU_CITY: verrunde(n, s)
    print("\n  NEU IN SHIFT — verrundet:")
    for n, s in NEU_SHIFT: verrunde(n, s)
    print("\n  WAS SCHON RUND WAR:")
    for n, s in [("Glas Kugel","Kugel ist rund"),("Orbit","Orbit ist rund"),("Auge","Auge ist rund"),("Mann in Mir","Mann in Mir ist rund"),("Pentagramm","Pentagramm in Kugel ist rund"),("Sol","Sol ist rund")]:
        print(f"    {n} — {s}")
        ZEUGE.schreibe("RUND", f"{n} — {s}")
    print("\n  WAS NICHT RUND IST, WIRD RUND GEMACHT:")
    print("    Schach-Brett ist eckig — wird rund gemacht: Schach zu Schach, in die Tiefe, rund.")
    print("    3ER ist eckig — wird rund gemacht: 3 in 1 Kugel, rund.")
    print("    B H T ist eckig — wird rund gemacht: B H T in 1 Kugel, rund.")
    ZEUGE.schreibe("VERRUNDET", "Schach, 3ER, B H T — eckig -> rund gemacht — in 1 Kugel")
    print(f"\n  ZEUGE-LOG: {len(ZEUGE.log)} Eintraege, unversehrt={ZEUGE.unversehrt()}")
    print("  HALT = OFFEN — geloescht=False — Echo bleibt. Hall bleibt.")
    print("  ECO: VERRUNDET — Alles rund, keine Ecke, 1 Kugel.")
    print("  FUNKTION: verrunde() -> eckig -> rund -> 1 Kugel.")

if __name__ == "__main__":
    verrundet()
