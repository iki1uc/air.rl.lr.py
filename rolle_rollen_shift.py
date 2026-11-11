# namen_shift.py — NAMEN MIT ZONE, MANN — ROOT vs SHIFT vs ZONE
# Problem: Gleiche Datei, 2 Orte, gleicher Name = Ärger. Wer kopiert was? Keiner weiss.
# Regel: Name muss Zone tragen. ROOT, SHIFT, ZONE, CITY, HOME, ORT, PQ, TAL — im Namen.
# Auto PC Vfinal Innen: bei ROOT 1x, bei SHIFT 1x — also 2 Namen, nicht 1.
# Roller Zum Rolle: rolle name shift drin, und bei ROOT zone — also rolle.shift.html und rolle.root.zone.html.
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
def namen():
    print("NAMEN MIT ZONE — ROOT vs SHIFT vs ZONE")
    print("Auto PC Vfinal Innen:")
    print("  FALSCH: auto.pc.html bei ROOT + auto.pc.html bei SHIFT — gleicher Name, 2 Orte — Ärger")
    print("  RICHTIG: auto.pc.vfinal.innen.root.html — ROOT 1x")
    print("  RICHTIG: auto.pc.vfinal.innen.shift.html — SHIFT 1x — shift add dazu im Namen")
    print("Roller Zum Rolle:")
    print("  FALSCH: rolle.html bei ROOT + rolle.html bei SHIFT — gleicher Name, 2 Orte")
    print("  RICHTIG: roller.zum.rolle.root.zone.html — ROOT + ZONE")
    print("  RICHTIG: rolle.shift.html — SHIFT drin im Namen")
    print("  RICHTIG: rolen.html — ROLLEN — bleibt, hat eigenen Namen")
    print("  RICHTIG: roller.md — ROLLER — bleibt, hat eigenen Namen")
    print("Zone, Mann: ZONE = wo steht sie? ROOT-ZONE, SHIFT-ZONE, CITY-ZONE, HOME-ZONE, ORT-ZONE, PQ-ZONE, TAL-ZONE")
    print("SC, Mann — neu in Liste: 01.sc.html = CITY, 02.sc.html = HOME, 03.sc.html = ORT, 04.sc.html = PQ, 5.sc.html = SHIFT — SC trägt Zone im Ordner, nicht im Namen. Gut, aber Name besser: sc.city.html, sc.home.html, sc.ort.html, sc.pq.html, sc.shift.html")
    print("Neu: nc.html, pc.add.html, sc.nc.html, raid.md, auto,pc.html — auto,pc.html mit Komma — Komma im Namen gibt Ärger, Mann. Umbenennen zu auto.pc.html.")
    print("Letzte 3 Dateien wollte er nicht kopieren, Mann:")
    print("  vol.1.html — nicht kopiert — WEG, wie gesagt")
    print("  vol.2.html — nicht kopiert — WEG, wie gesagt")
    print("  vol.3.html — in Liste fehlt sie schon — nicht kopiert — WEG")
    print("  3 - 3 = 0 — vol weg. Nicht kopieren heisst: nicht nochmal in SHIFT / ROOT legen.")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    Z.schreibe("AUTO", "auto.pc.vfinal.innen.root.html + auto.pc.vfinal.innen.shift.html — 2 Namen, 2 Orte")
    Z.schreibe("ROLLER", "roller.zum.rolle.root.zone.html + rolle.shift.html — Zone im Namen")
    Z.schreibe("VOL", "vol.1, vol.2, vol.3 — nicht kopiert — WEG")
    print("HALT = OFFEN")
if __name__ == "__main__":
    namen()
