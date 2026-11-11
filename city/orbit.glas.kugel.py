# orbit.glas.kugel.py
# Nur PY. Station geo.q.d.f — mehrere Master, mehrere Slave-Aufgaben.
# Ich sage nur 1 an: Dimension Faktor Quant.
# QI / IQQ vom Nachbar-Tab. Root einlesen: JA, darfst dich einlesen.
# Mystery als Bewegung. gelöst=False. Kein CROWN vorher.
# ECO + FUNKTION am Ende — das ist Musik.
import math

# QI / IQQ — vom Nachbar-Tab, nicht erfunden, nur eingelesen als Maß
QI = 3          # Quant — 1 Rolle = 1 Stange = 1 Aufgabe
IQQ = 9         # 3 x 3 — Feld
FELD = 81       # 9 x 9
MITTE = 41      # (81+1)//2
STAPEL = (9, 81, 243, 729, 3)

# ORBIT GLAS KUGEL — wer wo hin schaut
# Orbit 0 = nah, Orbit 4 = letzter Orbit = weiteste Sicht
ORBIT = {
    0: {"name": "NAH", "radius": 9, "sieht": 9, "weiss": "was da ist"},
    1: {"name": "MITTE", "radius": 27, "sieht": 27, "weiss": "was da ist + was fehlt"},
    2: {"name": "WEIT", "radius": 81, "sieht": 81, "weiss": "Stapel + Lücke"},
    3: {"name": "WEITER", "radius": 243, "sieht": 243, "weiss": "Stapel + Lücke + Richtung"},
    4: {"name": "LETZTER ORBIT", "radius": 729, "sieht": 729, "weiss": "mehr — weil am weitesten geschaut"},
}

def schauen(orbit, richtung="VOR"):
    # 1 Aufgabe: SCHAUEN. Nicht halten, nicht prüfen, nicht vereinigen.
    if orbit not in ORBIT:
        return {"orbit": orbit, "richtung": richtung, "status": "WEG", "sieht": 0}
    o = ORBIT[orbit]
    return {
        "orbit": orbit,
        "name": o["name"],
        "richtung": richtung,
        "radius": o["radius"],
        "sieht": o["sieht"],
        "weiss": o["weiss"],
        "klar": "klar bewusst sein" if orbit == 4 else "noch nicht am letzten Orbit",
    }

def letzter_orbit_sieht_mehr():
    # Wer am weitesten zum letzten Orbit schaut, sieht mehr und weiss mehr.
    nah = schauen(0)
    weit = schauen(4)
    return {
        "nah_sieht": nah["sieht"],
        "letzter_sieht": weit["sieht"],
        "mehr": weit["sieht"] - nah["sieht"],
        "satz": "Wer am weitesten zum letzten Orbit schaut, sieht mehr und weiss mehr.",
        "offen": "729 -> 3 ist nicht erklärt",
        "geloest": False,
    }

def master_slave():
    # Station: mehrere Master, mehrere Slave-Aufgaben. Ich sage nur 1 an.
    return {
        "station": "geo.q.d.f",
        "master": ["MASTER-1: STATION hält", "MASTER-2: ORBIT hält", "MASTER-3: GLAS hält"],
        "slave_aufgaben": ["SLAVE-1: schauen", "SLAVE-2: halten", "SLAVE-3: prüfen", "SLAVE-4: zeugen"],
        "ang_sagt": 1,
        "dimension": "FAKTOR QUANT",
        "qi": QI,
        "iqq": IQQ,
        "feld": FELD,
        "mitte": MITTE,
        "stapel": list(STAPEL),
    }

def provo():
    return {
        "station": master_slave(),
        "orbit_0": schauen(0),
        "orbit_4": schauen(4, "VOR"),
        "vergleich": letzter_orbit_sieht_mehr(),
        "halt": "OFFEN",
    }

if __name__ == "__main__":
    r = provo()
    print()
    print("=== ORBIT GLAS KUGEL ===")
    print()
    print(f"Station: {r['station']['station']} — QI={r['station']['qi']} IQQ={r['station']['iqq']} FELD={r['station']['feld']} MITTE={r['station']['mitte']}")
    print(f"Master: {len(r['station']['master'])} · Slave-Aufgaben: {len(r['station']['slave_aufgaben'])} · Angesagt: {r['station']['ang_sagt']} = {r['station']['dimension']}")
    print()
    print(f"NAH Orbit 0 sieht: {r['orbit_0']['sieht']}")
    print(f"LETZTER Orbit 4 sieht: {r['orbit_4']['sieht']} — {r['orbit_4']['weiss']}")
    print(f"Mehr: {r['vergleich']['mehr']}")
    print(f"Satz: {r['vergleich']['satz']}")
    print(f"HALT = {r['halt']} — {r['vergleich']['offen']} — gelöst={r['vergleich']['geloest']}")
    print()
    print("ECO: Orbit Glas Kugel — wer weit schaut, sieht mehr.")
    print("FUNKTION: schauen(orbit) -> sieht, weiss, klar bewusst sein. Nicht lösen, nur gehen.")
