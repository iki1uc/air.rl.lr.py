# engine_3x3.py — sp py, nicht pyx
# 3x3 Eval — QI / IQQ Engine — arg · xarg · arg3te
# Gleiche Formel wie HTML-Engine.

def clamp(v, mn=0, mx=1):
    return max(mn, min(mx, v))

def compute(lang="DE", responses=None, qi=0.65, iqq=0.35):
    if responses is None:
        responses = [
            {"text": "Antwort 1 — kurze Deutung / Fakten", "conf": 0.70},
            {"text": "Antwort 2 — alternative Deutung", "conf": 0.50},
            {"text": "Antwort 3 — kreative / künstlerische Sicht", "conf": 0.30},
        ]
    confs = [r["conf"] for r in responses]
    base = sum(confs) / len(confs)
    maxc = max(confs)
    minc = min(confs)
    var = maxc - minc
    combined = clamp(qi * base + (1 - iqq) * maxc, 0, 1)
    arg = round(combined, 4)
    xarg = round(var, 4)
    arg3te = round(combined * (1 - var), 4)
    top = max(range(len(responses)), key=lambda i: responses[i]["conf"]) + 1
    return {
        "lang": lang, "responses": responses, "qi": qi, "iqq": iqq,
        "base": round(base, 4), "maxc": maxc, "minc": minc,
        "var": var, "arg": arg, "xarg": xarg, "arg3te": arg3te, "top": top,
    }

if __name__ == "__main__":
    r = compute()
    print("3x3 Eval — QI / IQQ Engine — sp py")
    print("base =", r["base"], "maxc =", r["maxc"], "var =", r["var"])
    print("arg =", r["arg"], "xarg =", r["xarg"], "arg3te =", r["arg3te"], "top =", r["top"])
    print("HALT = ZIEL.")
