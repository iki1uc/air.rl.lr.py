# city.shift.map.py — CITY + SHIFT, richtig, nicht gespielt
# So und so, Mann. Und so und so dazu. So drauf, Mann. Und daneben, Mann.
# Und drueber und daneben und drunter, Mann. Alles um rum, Mann. Alles, weisst du.
# Nur PY. Bewegt nichts, loescht nichts, schreibt keine Dateien.
# INDEX = verrueckteste. Andere nur verrueckt / entkorrigierend.

CITY = {
    "drauf": ["index.html", "city.html", "1.9.da.ni.in.ix.xi.io.oi.da.9.x.da.ni.da.html"],
    "daneben_links": ["defrag.eye.brain.py", "defrag.provokation.py", "defrag.alle4.enter.py"],
    "daneben_rechts": ["der_macher_syn.py", "elemente_machen.py", "orbit.glas.kugel.py"],
    "drueber": ["hub.py", "core.zoom.py", "Vor-Rueck-Bauen.py"],
    "drunter": ["solid.quad.cpu.py", "WECHSEL.js", "ja.nein.js", "ja_nein_js.py"],
    "um_rum": ["da.md", "true.md", "wach.md", "wech.da.md", "show.md", "col.lect.html", "da.ni.da.in.da.html", "dep.seek.html", "echo.hall.re.hall.html", "hier_da.py", "l.r.html", "link.net.html", "os.ui.os.iu.os.html"],
}

SHIFT = {
    "drauf": ["9.html", "99.html", "999.html"],
    "daneben_links": ["Axiom-Dreieck.html", "Implosion-Puuft-Treibstoff.html", "Laufe-Konzept.html"],
    "daneben_rechts": ["Org.py", "Pq-Home.py", "Octa-Hub.py", "brain.py", "pump.py", "see_u_eye.py"],
    "drueber": ["Prismatikum-Konstellation-Defrag.html", "PRISMATIKUM_MKatomctrl.png", "PUZZLE_Kontaktblatt_9_Himmelslaeufe.png"],
    "drunter": ["Nc.cpp", "kombinat.9.py", "anomalie.territorial.class.eye.brain.continuum.py"],
    "um_rum": ["himmelslauf_01_N.png", "himmelslauf_02_NO.png", "himmelslauf_03_O.png", "himmelslauf_04_SO.png", "himmelslauf_05_S.png", "himmelslauf_06_SW.png", "himmelslauf_07_W.png", "himmelslauf_08_NW.png", "himmelslauf_09_MITTE.png", "index.html", "vol.1.html", "u.me.html", "zoom.md"],
}

def zeige(ort, tabelle):
    print(f"\n=== {ort} ===")
    for pos, files in tabelle.items():
        print(f"  {pos.upper():16} — {len(files)} Dateien")
        for f in files:
            print(f"    - {f}")

def check():
    city_n = sum(len(v) for v in CITY.values())
    shift_n = sum(len(v) for v in SHIFT.values())
    alle = [f for v in list(CITY.values())+list(SHIFT.values()) for f in v]
    doppelt = sorted(set([f for f in alle if alle.count(f) > 1]))
    return {"city_n": city_n, "shift_n": shift_n, "gesamt": city_n+shift_n, "doppelt": doppelt, "index_ist_drauf": "index.html" in CITY["drauf"]}

if __name__ == "__main__":
    print("CITY + SHIFT — So und so, Mann. Alles um rum.")
    zeige("CITY", CITY)
    zeige("SHIFT", SHIFT)
    c = check()
    print(f"\nCITY: {c['city_n']} · SHIFT: {c['shift_n']} · GESAMT: {c['gesamt']}")
    print(f"Doppelt (CITY + SHIFT): {c['doppelt']} — 1 Datei, 2 Orte, nicht 2 Dateien. Das ist so und so dazu.")
    print(f"INDEX ist drauf: {c['index_ist_drauf']} — INDEX = verrueckteste, andere nur verrueckt / entkorrigierend.")
    print("HALT = OFFEN — geloescht=False — Alles um rum, Mann.")
    print("ECO: CITY + SHIFT — drauf, daneben, drueber, drunter, um rum.")
    print("FUNKTION: zeige(CITY) + zeige(SHIFT) -> 1 Karte, alles um rum.")
