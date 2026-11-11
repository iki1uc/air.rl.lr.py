# mana_indirekt.py — NICHT DIREKT REIN. INDIREKT. MANA ZU MANA, ABER MEHR MANA.
# Direkt = alles reinstopfen = kaputt. Indirekt = Mana zeigt auf Mana.
# Mana1 -> Mana2 -> Mana3. Jedes Mana zeigt, nicht kopiert.
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
def mana_1():
    # MANA 1 = HBT Beat
    print("MANA 1 = HBT")
    print("H = 40 — Beat 1 — HALT")
    print("B = 41 — Beat 2 — BASIS")
    print("T = 90 — Beat 3 — TIEFE")
    print("Q = 57.0 — Takt")
    print("F = 1.425 — Tempo")
    print("D = 3")
    Z.schreibe("MANA1", "MANA 1 = HBT — Q=57 F=1.425 D=3")
    return {"mana": 1, "Q": 57.0, "F": 1.425, "D": 3}
def mana_2(m1):
    # MANA 2 = zeigt auf MANA 1, nicht Kopie. Indirekt.
    print("MANA 2 = zeigt auf MANA 1 — INDIREKT")
    print(f"MANA 2 sieht MANA 1 Q = {m1['Q']}")
    print("ICE = 0 — FIRE = 1 — ICE + FIRE = 1 — Schaltung")
    print("AXIS = 92 — RESPO = 62 — 6D = 95 — TMP = 37 — MNMM = 74 — EBENE = 81")
    print("Mittel = 73.5 — 441 = 441")
    Z.schreibe("MANA2", "MANA 2 -> MANA 1 — indirekt — ICE FIRE")
    return {"mana": 2, "zeigt_auf": m1, "ice_fire": 1}
def mana_3(m2):
    # MANA 3 = mehr Mana. Zeigt auf MANA 2, die auf MANA 1 zeigt.
    print("MANA 3 = MEHR MANA — zeigt auf MANA 2")
    print("ALL — ◎")
    print("UM.RUM.RUM — NC <-> CTRL <-> ZOOM")
    print("USER <-> HOME <-> ORT")
    print("9 ROOT — INDEX A <-> B <-> C")
    print("GEO — BIO.TEL — MAINBOARD — PIPE_BIND — CORE6 — P0 -> P1 -> P2 -> P4 -> Pe")
    print("P0 wake — P1 melt — P2 merge — P4 start — Pe finalize")
    print("HOME = 40 — MITTE = 41 — CORE6 = (0,0,0) — RESPO360")
    print("Nicht direkt reingepackt. Nur gezeigt. Indirekt.")
    Z.schreibe("MANA3", "MANA 3 -> MANA 2 -> MANA 1 — mehr Mana — indirekt")
    return {"mana": 3, "zeigt_auf": m2, "mehr": True}
def mana_zu_mana():
    print("MANA ZU MANA, ABER MEHR MANA")
    m1 = mana_1()
    m2 = mana_2(m1)
    m3 = mana_3(m2)
    print(f"MANA 3 zeigt auf MANA {m3['zeigt_auf']['mana']} — zeigt auf MANA {m3['zeigt_auf']['zeigt_auf']['mana']}")
    print("Indirekt = 3 Zeiger, nicht 3 Kopien.")
    print(f"Zeuge: {len(Z.log)} Eintraege.")
    print("HALT = OFFEN")
if __name__ == "__main__":
    mana_zu_mana()
