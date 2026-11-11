# defrag.alle4.enter.py
# Nur PY.
# 1 Aufruf -> 4 ENTER -> 1 rueckschauendes Log
# Reihenfolge: EYE -> BRAIN -> CORE -> CROWN
# CORE schaut auf EYE+BRAIN zurueck.
# CROWN schaut auf EYE+BRAIN+CORE zurueck.
# Dieses Skript defragmentiert keine Laufwerke,
# schreibt keine Dateien und loescht nichts.
import hashlib, json, math, sys, time, unittest
WORT = "up.ni pu.in"
ERWARTET = 11
UNTEN = 9
OBEN = math.isqrt(UNTEN)
FELD = UNTEN * UNTEN
MITTE = (FELD + 1) // 2
STAPEL = (9, 81, 243, 729, 3)
VIERER = {1: {"name": "EYE", "rolle": "sehen"}, 2: {"name": "BRAIN", "rolle": "halten"}, 3: {"name": "CORE", "rolle": "pruefen"}, 4: {"name": "CROWN", "rolle": "vereinigen"}}
class Zeuge:
    def __init__(self):
        self._zeilen = []
    @staticmethod
    def _hash(z):
        roh = json.dumps({k: z[k] for k in ("n","enter","text","zeit","vorher")}, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(roh.encode("utf-8")).hexdigest()
    def schreibe(self, enter, text):
        vorher = self._zeilen[-1]["hash"] if self._zeilen else "0"*64
        z = {"n": len(self._zeilen)+1, "enter": enter, "text": text, "zeit": time.strftime("%Y-%m-%d %H:%M:%S"), "vorher": vorher}
        z["hash"] = self._hash(z)
        self._zeilen.append(z)
    def zeilen(self):
        return [dict(z) for z in self._zeilen]
    def unversehrt(self):
        vorher = "0"*64
        for z in self._zeilen:
            if z["vorher"] != vorher: return False
            if z["hash"] != self._hash(z): return False
            vorher = z["hash"]
        return True
def eye_enter(wort, zeuge):
    zeichen = len(wort)
    verloren = max(0, ERWARTET - zeichen)
    zuviel = max(0, zeichen - ERWARTET)
    ok = (verloren==0 and zuviel==0 and OBEN**2==UNTEN and MITTE==41)
    res = {"zeichen": zeichen, "bytes": len(wort.encode("utf-8")), "verloren": verloren, "zuviel": zuviel, "hoehe_breite": f"{OBEN} oben / {UNTEN} unten", "mitte": MITTE, "ok": ok}
    zeuge.schreibe("EYE_ENTER", f"schaut zurueck: {zeichen} Zeichen gesehen, {verloren} verloren")
    return res
def brain_enter(zeuge):
    stapel = list(STAPEL)
    exponenten = [round(math.log(x,3)) for x in stapel]
    potenzen = all(3**e==x for e,x in zip(exponenten, stapel))
    delta = [round(stapel[i+1]/stapel[i],6) for i in range(len(stapel)-1)]
    res = {"stapel": stapel, "exponenten_zu_3": exponenten, "alle_potenzen_von_3": potenzen, "delta": delta, "mystery": "OFFEN: 729 -> 3 ist nicht erklaert", "ok": potenzen}
    zeuge.schreibe("BRAIN_ENTER", "schaut zurueck: Stapel " + " -> ".join(map(str, stapel)))
    return res
def core_enter(zeuge, eye, brain):
    nummern = (1,2,3)
    summe = sum(nummern)
    assimiliert = (eye["ok"] and brain["ok"])
    offen = [brain["mystery"]]
    if summe != 9:
        offen.append(f"1+2+3 ergibt {summe}, nicht 9")
    res = {"gesehen": list(nummern), "summe": summe, "assimiliert": assimiliert, "halt": "ZIEL" if assimiliert else "OFFEN", "offen": offen, "ok": assimiliert}
    zeuge.schreibe("CORE_ENTER", f"schaut zurueck: Summe {summe} assimiliert={assimiliert}")
    return res
def crown_enter(zeuge, eye, brain, core):
    vereinigt = (eye["ok"] and brain["ok"] and core["ok"])
    res = {"modell": "4ER", "stufen": ["EYE","BRAIN","CORE"], "vereinigt": vereinigt, "ok": vereinigt}
    zeuge.schreibe("CROWN_ENTER", f"schaut zurueck: EYE+BRAIN+CORE vereinigt={vereinigt}")
    return res
def alle4(wort=WORT):
    zeuge = Zeuge()
    eye = eye_enter(wort, zeuge)
    brain = brain_enter(zeuge)
    core = core_enter(zeuge, eye, brain)
    crown = crown_enter(zeuge, eye, brain, core)
    return {"wort": wort, "modell": "4ER", "vierer": VIERER, "eye": eye, "brain": brain, "core": core, "crown": crown, "log": zeuge.zeilen(), "log_unversehrt": zeuge.unversehrt(), "_zeuge": zeuge}
class TestAlleVierEnter(unittest.TestCase):
    def test_eye_enter(self):
        z=Zeuge(); res=eye_enter(WORT,z); self.assertTrue(res["ok"]); self.assertEqual(res["zeichen"],11)
    def test_brain_enter(self):
        z=Zeuge(); res=brain_enter(z); self.assertTrue(res["ok"]); self.assertTrue(res["alle_potenzen_von_3"])
    def test_core_enter(self):
        z=Zeuge(); eye=eye_enter(WORT,z); brain=brain_enter(z); core=core_enter(z,eye,brain); self.assertTrue(core["assimiliert"]); self.assertEqual(core["halt"],"ZIEL")
    def test_crown_enter(self):
        z=Zeuge(); eye=eye_enter(WORT,z); brain=brain_enter(z); core=core_enter(z,eye,brain); crown=crown_enter(z,eye,brain,core); self.assertTrue(crown["vereinigt"]); self.assertTrue(crown["ok"])
    def test_log_integritaet(self):
        r=alle4(); self.assertTrue(r["log_unversehrt"]); self.assertEqual(len(r["log"]),4)
if __name__=="__main__":
    import sys
    if len(sys.argv)>1 and sys.argv[1]=="--test":
        unittest.main(argv=[sys.argv[0]])
    else:
        r=alle4(sys.argv[1] if len(sys.argv)>1 else WORT)
        print(); print("=== ALLE4 ENTER ==="); print()
        for z in r["log"]:
            print(f"ENTER {z['n']} = {z['enter']}"); print(f"-> {z['text']}"); print()
        print(f'-> Wort: "{r["wort"]}"'); print("-> Modell: "+f'{r["modell"]}'); print("-> Log unversehrt: "+f'{r["log_unversehrt"]}'); print("HALT = "+f'{r["core"]["halt"]}')
        if r["core"]["offen"]:
            print()
            for o in r["core"]["offen"]:
                print("offen:", o)
