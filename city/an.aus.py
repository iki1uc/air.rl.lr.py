# an.aus.py — NEIN MANN, SO EINFACH MACH ICH DAS
# An. Aus. Einfach, Mann. Nicht 60 Dateien. Nicht 10 Erklaerungen. So einfach.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
import hashlib, json, time
class Zeuge:
    def __init__(self): self.log = []
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        roh = json.dumps({"n": len(self.log)+1, "enter": enter, "text": text, "vorher": vorher}, sort_keys=True)
        h = hashlib.sha256(roh.encode()).hexdigest()
        self.log.append(h); print(f"  [{enter}] {text} | {h[:8]}...")
Z = Zeuge()
def an_aus():
    print("AN. AUS. EINFACH, MANN.")
    Z.schreibe("AN", "An — da")
    Z.schreibe("AUS", "Aus — nicht da")
    Z.schreibe("SCHALTUNG", "An + Aus = Schaltung — beide zusammen")
    Z.schreibe("XI", "XI IX IO OI IQ QI — vor rueck auf ab rein raus")
    Z.schreibe("MANN", "IN NI MANN — In Ni Mann — Mehr Mann")
    print(f"Zeuge: {len(Z.log)} Zeilen. HALT = OFFEN. Echo bleibt. Hall bleibt.")
if __name__ == "__main__":
    an_aus()
