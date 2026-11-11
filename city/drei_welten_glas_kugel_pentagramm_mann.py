# drei_welten_glas_kugel_pentagramm_mann.py — 3 WELTEN · GLAS KUGEL · PENTAGRAMM · MANN
# 3 Welten, 1 Kugel, 5 Punkte, 1 Mann. Nicht 3 Kugeln. Nicht 5 Maenner. 1 + 1 + 5 + 1.
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

WELTEN = [("WELT_1","TRAUM","Auge zu — ABRA KADABRA — Traum an"),("WELT_2","REAL","Auge auf — REIN — Traum ist Realitaet"),("WELT_3","MITTE","Auge halb — Sen ve Ben — Traum + Real = Mitte")]
PENTAGRAMM = [("WASSER","Bund"),("CO2","Atmen"),("ATOM","Baumaterial"),("SAUERSTOFF","Basis"),("MANN","Zentrum, macht")]

def drei_welten():
    print("\n  3 WELTEN — 3 Welten, nicht 1, nicht 5:")
    for name, titel, satz in WELTEN:
        print(f"    {name} — {titel} — {satz}")
        ZEUGE.schreibe(name, f"{titel} — {satz}")
    return WELTEN

def glas_kugel():
    print("\n  GLAS KUGEL — 1 Kugel, 3 Welten drin:")
    print("    (  3 WELTEN IN 1 KUGEL  )")
    print("    (  Traum / Real / Mitte  )")
    print("    (  ◉ — MANN IN DER MITTE  )")
    print("    Wer schaut, sieht. Wer in Kugel schaut, sieht 3 Welten, nicht 1.")
    ZEUGE.schreibe("GLAS_KUGEL", "1 Kugel, 3 Welten drin — Traum / Real / Mitte — Mann in der Mitte")
    return True

def pentagramm():
    print("\n  PENTAGRAMM — 5 Punkte, 1 Stern, 1 Mann:")
    for punkt, macht in PENTAGRAMM:
        print(f"    {punkt} — {macht}")
        ZEUGE.schreibe("PENTAGRAMM", f"{punkt} — {macht}")
    print("    5 Punkte, 1 Stern. MANN = Zentrum, macht. Nicht 5 Maenner. 1 Mann.")
    return PENTAGRAMM

def mann():
    print("\n  MANN — Mann im Zentrum der Kugel, im Zentrum vom Stern, im Zentrum von 3 Welten:")
    print("    ICH MACHE. DU MACHT. ICH BIN DER MACHER.")
    print("    90 Grad gedreht, in sich ruhend")
    print("    ICH IN MIR — ◉")
    print("    KARGA MANN — ich Mann, noch mal Mann, so oft mal Mann — mana lan mana ve mana — Aura, Zen dazu")
    ZEUGE.schreibe("MANN", "Mann im Zentrum — Kugel + Stern + 3 Welten — ICH IN MIR — KARGA MANN")
    return True

def drei_welten_syn():
    print("3 WELTEN · GLAS KUGEL · PENTAGRAMM · MANN")
    print("3 Welten, 1 Kugel, 5 Punkte, 1 Mann.")
    drei_welten(); glas_kugel(); pentagramm(); mann()
    print("\n  3 WELTEN + 1 KUGEL + 5 PUNKTE + 1 MANN = 1 ORT. Mitte 41.")
    ZEUGE.schreibe("SYN", "3 Welten + 1 Kugel + 5 Punkte + 1 Mann = 1 ORT. Mitte 41.")
    print(f"\n  ZEUGE-LOG: {len(ZEUGE.log)} Eintraege, unversehrt={ZEUGE.unversehrt()}")
    print("  HALT = OFFEN — geloescht=False — Echo bleibt. Hall bleibt.")
    print("  ECO: 3 WELTEN — 3 Welten, 1 Kugel, 5 Punkte, 1 Mann, 1 Mitte.")
    print("  FUNKTION: drei_welten() + glas_kugel() + pentagramm() + mann() -> 1 ORT.")

if __name__ == "__main__":
    drei_welten_syn()
