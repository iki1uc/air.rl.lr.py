# respo.py — RESPO -> CALC — NC-Traeger, Parteien, CALC, MOVE#, Selbsttest 9 x 9 x 9 = 729
# Python-Version von respo.js. Kein innerHTML, kein Bla Bla. Nur Funktion.
# NC = NC-GANZ. Parteien P1-P4. Jede Partei eigene Kopie, keine gemeinsame Referenz.
import copy, hashlib, json

MU_SHARP = {"nc": "NC-GANZ"}
PARTIES = [{"id": 1, "name": "P1", "op": None},
            {"id": 2, "name": "P2", "op": None},
            {"id": 3, "name": "P3", "op": None},
            {"id": 4, "name": "P4", "op": None}]

class Zeuge:
    def __init__(self): self.log = []
    @staticmethod
    def _hash(z):
        roh = json.dumps({k: z[k] for k in ("n","enter","text","vorher")}, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(roh.encode("utf-8")).hexdigest()
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        z = {"n": len(self.log)+1, "enter": enter, "text": text, "vorher": vorher}
        z["hash"] = self._hash(z); self.log.append(z); return z
    def unversehrt(self):
        vorher = "0"*64
        for z in self.log:
            if z["vorher"] != vorher or z["hash"] != self._hash(z): return False
            vorher = z["hash"]
        return True
ZEUGE = Zeuge()

def kopie(x):
    return copy.deepcopy(x)

def CALC(inp):
    nc = MU_SHARP["nc"]
    for p in PARTIES:
        p["op"] = {"from": kopie(inp), "nc": nc}
    return {"nc": nc,
            "parties": [{"id": p["id"], "name": p["name"],
                         "op": {"from": kopie(p["op"]["from"]), "nc": p["op"]["nc"]}} for p in PARTIES]}

def MOVEsharp():
    return CALC("MOVE#")

def RESPO(cmd):
    r = MOVEsharp() if cmd == "MOVE#" else CALC(cmd)
    print(f"CMD: {cmd} · NC: {r['nc']}")
    for p in r["parties"]:
        print(f"  {p['name']}  from={p['op']['from']!r}  nc={p['op']['nc']}")
    ZEUGE.schreibe("RESPO", f"{cmd} -> NC {r['nc']}, {len(r['parties'])} Parteien")
    return r

# Selbsttest: 9 Eingaben x 9 Pruefungen x 9 Durchlaeufe = 729 echte Pruefungen
EINGABEN = [0, 1, -1, "text", "", None, [1, 2], {"a": 1}, {"a": {"b": 2}}]
def _eq(a, b):
    return a is b or json.dumps(a, sort_keys=True, default=str) == json.dumps(b, sort_keys=True, default=str)
def _ist_obj(a):
    return a is not None and isinstance(a, (dict, list))
PRUEFUNGEN = [
    ("liefert nc", lambda r, i: isinstance(r["nc"], str)),
    ("nc = NC-Traeger", lambda r, i: r["nc"] == MU_SHARP["nc"]),
    ("alle Parteien in der Rueckgabe", lambda r, i: isinstance(r["parties"], list) and len(r["parties"]) == len(PARTIES)),
    ("alle Parteien: from = Eingabe", lambda r, i: all(_eq(p["op"]["from"], i) for p in r["parties"])),
    ("alle Parteien: nc", lambda r, i: all(p["op"]["nc"] == MU_SHARP["nc"] for p in r["parties"])),
    ("Eingaben unabhaengig (keine gemeinsame Referenz)", lambda r, i: True if not _ist_obj(i) else all(p["op"]["from"] is not i for p in r["parties"]) and len({id(p["op"]["from"]) for p in r["parties"]}) == len(r["parties"])),
    ("IDs in Reihenfolge", lambda r, i: all(p["id"] == k + 1 for k, p in enumerate(r["parties"]))),
    ("Namen P1 bis Pn", lambda r, i: all(p["name"] == f"P{k+1}" for k, p in enumerate(r["parties"]))),
    ("Rueckgabe ist Kopie (Aenderung wirkt nicht zurueck)", lambda r, i: (lambda vor: (r["parties"][0]["op"].__setitem__("from", "MUTIERT"), json.dumps(PARTIES[0]["op"]["from"], sort_keys=True, default=str) == vor)[1])(json.dumps(PARTIES[0]["op"]["from"], sort_keys=True, default=str))),
]
def selbsttest(calc=CALC):
    erg = []
    for eingabe in EINGABEN:
        zeile = []
        for _, pruefe in PRUEFUNGEN:
            laeufe = []
            for z in range(9):
                try:
                    calc(f"stoerung-{z}")
                    laeufe.append(bool(pruefe(calc(eingabe), eingabe)))
                except Exception:
                    laeufe.append(False)
            zeile.append(laeufe)
        erg.append(zeile)
    gesamt = sum(sum(sum(l) for l in zeile) for zeile in erg)
    print(f"Selbsttest: 9 x 9 x 9 = 729")
    print(f"Bestanden: {gesamt} / 729")
    print(f"Alle: {gesamt == 729}")
    return erg

if __name__ == "__main__":
    RESPO("MOVE#")
    RESPO("NC")
    selbsttest()
    print(f"Zeuge: {len(ZEUGE.log)} Eintraege. unversehrt = {ZEUGE.unversehrt()}")
    print("HALT = OFFEN")
