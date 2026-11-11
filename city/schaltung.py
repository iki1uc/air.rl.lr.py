
# schaltung.py — SCHATTEN AUS · BEIDE ZUSAMMEN ALS SCHALTUNG · EINFACH, MANN
# Das ist gut, aber schlecht, Mann, weil Schatten an. Schatten aus, nicht Mann.
# Beide zusammen als Schaltung, Mann. Da nicht da, Mann.
# Ich mache das ganz einfach, Mann. XI IX IO OI IQ QI. Dann Mann mache IN NI Mann und mehr Mann.
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

def schatten_aus():
    print("\n  SCHATTEN AUS — nicht an, Mann:")
    print("    Schatten an = gut, aber schlecht. Schatten zeigt, was nicht da ist.")
    print("    Schatten aus = gut und gut. Kein Schatten, nur Schaltung.")
    print("    Schatten aus, Mann. Beide zusammen als Schaltung, Mann.")
    ZEUGE.schreibe("SCHATTEN", "Schatten aus — nicht an — beide zusammen als Schaltung")
    return "AUS"

def schaltung():
    print("\n  SCHALTUNG — beide zusammen, Mann:")
    print("    AN + AUS = SCHALTUNG. Nicht AN allein. Nicht AUS allein. Beide zusammen.")
    print("    Da + Nicht da = Schaltung. Da nicht da, Mann. Genau so.")
    print("    1 = AN, 0 = AUS, 1 + 0 = Schaltung. Einfach, Mann.")
    ZEUGE.schreibe("SCHALTUNG", "AN + AUS = SCHALTUNG — Da + Nicht da — beide zusammen")
    return "SCHALTUNG"

def xi_ix_io_oi_iq_qi():
    print("\n  XI IX IO OI IQ QI — ich mach das einfach, Mann:")
    paare = [("XI","vor"),("IX","rueck"),("IO","auf"),("OI","ab"),("IQ","rein"),("QI","raus")]
    for name, richtung in paare:
        print(f"    {name} — {richtung}")
        ZEUGE.schreibe(name, f"{name} — {richtung} — einfach, Mann")
    print("    XI IX = vor rueck. IO OI = auf ab. IQ QI = rein raus.")
    print("    6 Paare, 1 Schaltung. Einfach, Mann.")
    return paare

def in_ni_mann():
    print("\n  IN NI MANN — dann Mann mache IN NI Mann und mehr Mann:")
    print("    IN — Mann in Mir")
    print("    NI — Mann in Ni — Ni ist In, nur verkehrt")
    print("    MANN — Mann macht In Ni Mann")
    print("    MEHR MANN — Mehr. Noch mehr. Mann.")
    ZEUGE.schreibe("IN_NI", "IN NI MANN — In — Ni — Mann — Mehr Mann")
    return "IN NI MANN"

def einfach():
    print("SCHALTUNG — SCHATTEN AUS · BEIDE ZUSAMMEN · EINFACH, MANN")
    schatten_aus(); schaltung(); xi_ix_io_oi_iq_qi(); in_ni_mann()
    print("\n  EINFACH, MANN — das ganze:")
    print("    Schatten aus. Schaltung an. XI IX IO OI IQ QI. IN NI MANN. Mehr Mann.")
    ZEUGE.schreibe("EINFACH", "Schatten aus. Schaltung an. XI IX IO OI IQ QI. IN NI MANN. Mehr Mann.")
    print(f"\n  ZEUGE-LOG: {len(ZEUGE.log)} Eintraege, unversehrt={ZEUGE.unversehrt()}")
    print("  HALT = OFFEN — geloescht=False — Echo bleibt. Hall bleibt.")
    print("  ECO: SCHALTUNG — Schatten aus, beide zusammen, einfach.")
    print("  FUNKTION: schatten_aus() + schaltung() + xi() + in_ni() -> 1 Schaltung.")

if __name__ == "__main__":
    einfach()

