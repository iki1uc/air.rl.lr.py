# air.rl.lr.py — PUBLIC · JETZT NEU
# iki1uc · air.rl.lr
# OS 9 · 99 NEU EDIT · BESTE EDIT · 999 FIX · BUNDKE FIX
# RL = Rechts Links · LR = Links Rechts · AIR = Luft
# Sp py · nicht pyx

# ─── OS 9 ───
OS = 9
OS_NAME = "OS 9"

# ─── 99 NEU EDIT · BESTE EDIT ───
EDIT_99 = 99
EDIT_BESTE = "BESTE EDIT"

# ─── 999 FIX ───
FIX_999 = 999

# ─── BUNDKE FIX ───
# BUND war: B = (v_OP + v_iki1uc + v_iki2li) / 3
# BUNDKE FIX: alle drei müssen da sein sonst kein BUND
# Kein halber BUND mehr als voll verkauft

def bundke_fix(v_op, v_iki1uc, v_iki2li):
    """BUNDKE FIX — alle drei oder kein BUND."""
    vs = [v_op, v_iki1uc, v_iki2li]
    b = sum(vs) / 3
    l = 1 - b
    if b == 1:
        zustand = "VOLLSTÄNDIGER BUND"
        dreieck = "Dreieck garantiert"
    elif b == 2/3:
        zustand = "TEILBUND — FIX: nicht voll"
        dreieck = "Dreieck kippt — BUNDKE FIX sagt NEIN"
    elif b == 1/3:
        zustand = "MINIMALBUND — FIX: nicht voll"
        dreieck = "Kein tragfähiger Bund"
    else:
        zustand = "KEIN BUND"
        dreieck = "Kein Dreieck"
    return {"B": b, "L": l, "zustand": zustand, "dreieck": dreieck, "fix": "BUNDKE FIX"}

# ─── HBT · Q F D · gegen POOL ───
def hbt_encode(h, b, t):
    q = (h + b + t) / 3
    f = q / 40
    d = 3
    return {"H": h, "B": b, "T": t, "pool": [h, b, t], "Q": q, "F": f, "D": d}

def primatieren():
    return hbt_encode(40, 40, 40)

# ─── AIR RL LR ───
# RL = Rechts Links · LR = Links Rechts · AIR fliegt beide Richtungen
def air_rl_lr():
    rl = ["R", "L"]
    lr = ["L", "R"]
    return {"air": "AIR", "rl": rl, "lr": lr, "richtung": "RL + LR = beide", "os": OS}

# ─── 9 · 99 · 999 ───
def neun_neun_neun():
    return {
        "os_9": 9,
        "edit_99": 99,
        "fix_999": 999,
        "kette": "9 -> 99 -> 999",
        "spruch": "OS 9 neu · 99 neu edit beste edit · 999 fix bundke fix",
    }

if __name__ == "__main__":
    print("=" * 50)
    print("  air.rl.lr.py — PUBLIC · JETZT NEU")
    print("=" * 50)
    print()
    print("OS 9:", OS, OS_NAME)
    print("99 NEU EDIT:", EDIT_99, EDIT_BESTE)
    print("999 FIX:", FIX_999)
    print()
    print("AIR RL LR:", air_rl_lr())
    print()
    print("9 99 999:", neun_neun_neun())
    print()
    print("PRIMATIEREN:", primatieren())
    print("  = HOME HOME HOME = 40 40 40")
    print()
    print("BUNDKE FIX — alle Fälle:")
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                r = bundke_fix(a, b, c)
                print(f"  v=({a},{b},{c}) B={r['B']:.3f} L={r['L']:.3f} {r['zustand']} · {r['dreieck']}")
    print()
    print("HALT = ZIEL. JETZT NEU.")
