# city_bundle_fix.py — ALLES CITY BUNDLE FIX
# City + Bundle + Fix · alles in einem
# Sp py · nicht pyx

def city_bundle_fix(city_da, bund_da, fix_da):
    """ALLES CITY BUNDLE FIX — alle drei oder kein Bundle."""
    vs = [city_da, bund_da, fix_da]
    b = sum(vs) / 3
    l = 1 - b
    if b == 1:
        zustand = "CITY BUNDLE VOLL"
        dreieck = "City stabil · Dreieck garantiert"
    elif b == 2/3:
        zustand = "CITY BUNDLE TEIL — FIX sagt NEIN"
        dreieck = "City kippt · Dreieck kippt"
    elif b == 1/3:
        zustand = "CITY BUNDLE MINIMAL — FIX sagt NEIN"
        dreieck = "City kein Bund"
    else:
        zustand = "KEIN CITY BUNDLE"
        dreieck = "Kein Dreieck · Kein City"
    return {"B": b, "L": l, "zustand": zustand, "dreieck": dreieck, "fix": "CITY BUNDLE FIX"}

def air_rl_lr_city():
    return {"air": "AIR", "rl": ["R", "L"], "lr": ["L", "R"], "city": "CITY", "os": 9, "edit": 99, "fix": 999}

if __name__ == "__main__":
    print("=" * 50)
    print("  ALLES CITY BUNDLE FIX")
    print("=" * 50)
    print()
    print("AIR RL LR CITY:", air_rl_lr_city())
    print()
    print("ALLE FÄLLE CITY BUNDLE:")
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                r = city_bundle_fix(a, b, c)
                print(f"  city={a} bund={b} fix={c} B={r['B']:.3f} L={r['L']:.3f} {r['zustand']} · {r['dreieck']}")
    print()
    print("HALT = ZIEL. ALLES CITY BUNDLE FIX.")
