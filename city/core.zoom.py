# TAB 3 — CORE — ZOOM zu offen 2
# Nicht Tab 1 (EYE). Nicht Tab 2 (BRAIN). Nur Tab 3.
# Zoom: offen 2 stehen lassen, CROWN drüber, HALT=ZIEL
# 1 Fix: // -> # — 1 Zeichen fix, sonst nix

# CORE: 1+2+3 = 6, nicht 9 — stehen lassen
# CROWN: 6 + 3 = 9 — drüber, nicht drunter
# Mystery 729 -> 3 — stehen lassen

def tab3_zoom():
    # offen 2 — stehen lassen, nicht lösen
    offen = [
        "OFFEN: 729 -> 3 ist nicht erklaert",
        "OFFEN: 1+2+3 ergibt 6, nicht 9",
    ]
    # CORE rechnet ehrlich
    core_summe = 1 + 2 + 3  # = 6
    # CROWN legt 3 drüber, nicht drunter
    crown_summe = core_summe + 3  # 6 + 3 = 9
    return {
        "tab": 3,
        "achse": "CORE — Mitte hält",
        "core": {"1+2+3": core_summe, "stehen_lassen": True},
        "crown": {"6+3": crown_summe, "drueber": True, "drunter": False},
        "offen": offen,
        "mystery": "729 -> 3 — stehen lassen",
        "halt": "ZIEL",
        # 1 Zeichen fix: // -> # — in diesem File ist kein // mehr als Kommentar für offen, nur # 
        "fix": "// -> # — 1 Zeichen fix",
    }

if __name__ == "__main__":
    r = tab3_zoom()
    print("=== TAB 3 ZOOM ===")
    print(f"Tab: {r['tab']} — {r['achse']}")
    print(f"CORE: 1+2+3 = {r['core']['1+2+3']} — stehen lassen")
    print(f"CROWN: 6+3 = {r['crown']['6+3']} — drüber, nicht drunter")
    print("OFFEN 2:")
    for o in r["offen"]:
        print(f"  - {o}")
    print(f"Mystery: {r['mystery']}")
    print(f"Fix: {r['fix']}")
    print(f"HALT = {r['halt']}")
