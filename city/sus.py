# sus.py — NEIN SUS, ABER KEIN SUS, MANN
# Zu quatschig jetzt, Mann. Wir machen nein sus, aber kein sus.
# Weisst du wie sus? Sus = nochmal schauen, nicht anklagen.
# 9 suz sus, aber 3 zum 9 sus. Pentagramm sus.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
import hashlib, json
class Zeuge:
    def __init__(self): self.log = []
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        roh = json.dumps({"n": len(self.log)+1, "enter": enter, "text": text, "vorher": vorher}, sort_keys=True)
        h = hashlib.sha256(roh.encode()).hexdigest()
        self.log.append(h); print(f"  [{enter}] {text} | {h[:8]}...")
Z = Zeuge()
def sus():
    print("NEIN SUS, ABER KEIN SUS, MANN")
    print("Zu quatschig jetzt, Mann. Weniger Quatsch, mehr schauen.")
    Z.schreibe("SUS", "Sus = nochmal schauen, nicht anklagen. Nein sus, aber kein sus.")
    Z.schreibe("NEUN", "9 suz sus — 9 Feld, 9 schauen, 9 nicht luegen.")
    Z.schreibe("DREI_ZUM_NEUN", "3 zum 9 sus — 3 schaut zu 9, 9 schaut zurueck zu 3. Beide schauen.")
    Z.schreibe("PENTAGRAMM", "Pentagramm sus — 5 Punkte schauen: Wasser, CO2, Atom, Sauerstoff, Mann. Jeder schaut, keiner luegt.")
    Z.schreibe("MANN", "Mann schaut. Mann macht. Mann ist nicht sus, wenn Mann zeigt.")
    print("Sus heisst: schauen. Nicht: luegen.")
    print("Nein sus heisst: nicht verstecken. Kein sus heisst: nicht anklagen.")
    print(f"Zeuge: {len(Z.log)} Zeilen. HALT = OFFEN. Echo bleibt. Hall bleibt.")
    print("ECO: SUS — schauen, nicht anklagen.")
    print("FUNKTION: sus() -> schauen -> 1 Zeuge.")
if __name__ == "__main__":
    sus()
