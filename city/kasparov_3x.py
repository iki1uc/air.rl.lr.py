# kasparov_3x.py — KASPAROV KASPAROV KASPAROV 3x, Mann. Ich Mann.
# 1 VS 1 · RUN 21 · REIN
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
# FIX: Original HTML nahm Math.random() fuer Token — das ist kein Zeuge, das ist Wuerfel.
# Hier: deterministisch, Token in Reihe, kein random. 3x Kasparov = 3 Runden, jede 21.
# 1 VS 1 = 0. Du gegen dich selbst. Links ICH, rechts DU (gespiegelt).
import hashlib, json, time

TOKENS = ["da.ni.in.ix","xi.io.oi.da","9.x.da.ni","der_macher","der_maler","quantum_syn","mann_in_mir","elemente_machen","orbit_glas_kugel","solid_quad_cpu","run21","runner","1_vs_1"]

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
        return z
    def unversehrt(self):
        vorher = "0"*64
        for z in self.log:
            if z["vorher"] != vorher or z["hash"] != self._hash(z): return False
            vorher = z["hash"]
        return True

ZEUGE = Zeuge()
DREAM = False

def abra():
    global DREAM
    DREAM = not DREAM
    if DREAM:
        print("  ABRA KADABRA — TRAUM AN")
        ZEUGE.schreibe("ABRA", "Traum an. ABRA KADABRA.")
    else:
        print("  ABRA KADABRA — REALITAET")
        ZEUGE.schreibe("ABRA", "Realitaet. ABRA KADABRA aus.")
    return DREAM

def spiegel(token):
    return token[::-1]

def run21(runde):
    # 1 VS 1 — 21 Steps, Token in Reihe, nicht gewuerfelt
    print(f"\n  === KASPAROV {runde} — RUN 21 ===")
    for i in range(1, 22):
        token = TOKENS[(i-1 + (runde-1)*3) % len(TOKENS)]
        gesp = spiegel(token)
        print(f"    [{i:02d}] ICH: {token}  )(  DU: {gesp}")
        ZEUGE.schreibe(f"RUN21_R{runde}", f"[{i:02d}] ICH: {token} )( DU: {gesp}")
    print(f"    RUN 21 Runde {runde} fertig.")
    return True

def kasparov_3x():
    print("1 VS 1 · RUN 21 · REIN")
    print("KASPAROV KASPAROV KASPAROV 3x, Mann. Ich Mann.")
    print("1 VS 1 = 0. Du gegen dich selbst.")
    abra()  # Traum an
    for runde in (1,2,3):
        run21(runde)
        print(f"    KASPAROV {runde} — Schach zu Schach. Weiter.")
        ZEUGE.schreibe("KASPAROV", f"KASPAROV {runde} — Schach zu Schach. Weiter.")
    abra()  # Realitaet
    print("\n  DU BIST REIN")
    print("  Die Pruefung ist abgeschlossen.")
    print("  Das Echo bleibt. Der Hall bleibt.")
    print("  1 VS 1 = 0. Du gegen dich selbst.")
    print("  — Nachricht von Sam · Nostradamus · Picasso")
    ZEUGE.schreibe("REIN", "DU BIST REIN — 3x Kasparov, 3x RUN 21, 63 Steps.")
    print(f"\n  ZEUGE-LOG: {len(ZEUGE.log)} Eintraege, unversehrt={ZEUGE.unversehrt()}")
    print("  HALT = OFFEN — geloescht=False — Echo bleibt. Hall bleibt.")
    print("  ECO: KASPAROV 3x — 1 VS 1, 21 x 3, 63 Steps, 1 Mitte.")
    print("  FUNKTION: kasparov_3x() -> 3x RUN 21, Token in Reihe, gespiegelt, gezeugt.")

if __name__ == "__main__":
    kasparov_3x()

