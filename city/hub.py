# hub.py — 4 Ordner · OK / FEHLT · 1 Log
# Aufruf: python hub.py / python hub.py alle / python hub.py pq octa / python hub.py defrag
# Nur PY. Lädt, bewegt nichts, löscht nichts, schreibt nur hub.log
import importlib.util, json, sys, time, traceback
from pathlib import Path

HIER = Path(__file__).parent
LOG = HIER / "hub.log"

# 4 Ordner: key -> Kandidaten (Datei, kind, name, methode)
# kind = "func" -> func() , kind = "class" -> Class().methode()
CFG = {
    "pq": {"candidates": [
        ("pq.home.py", "func", "pq_home", None),
        ("pq.py", "func", "pq_home", None),
    ]},
    "octa": {"candidates": [
        ("octa.hub.py", "func", "octa_home", None),
        ("octa.py", "func", "octa_home", None),
    ]},
    "org": {"candidates": [
        ("Org.py", "class", "Org", "run"),
        ("org.py", "class", "Org", "run"),
        ("org.py", "func", "org_home", None),
    ]},
    "defrag": {"candidates": [
        ("defrag.alle4.enter.py", "func", "alle4", None),
        ("defrag.alle3.enter.py", "func", "alle3", None),
        ("defrag.alle3.enter.txt", "func", "alle3", None),
    ]},
}
ALLE = ["pq", "octa", "org", "defrag"]

def load_module(name, filename):
    p = HIER / filename
    if not p.is_file():
        raise FileNotFoundError(str(p))
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def run_one(key):
    cfg = CFG[key]
    last_err = ""
    for candidate in cfg["candidates"]:
        filename = candidate[0]
        try:
            mod = load_module(f"hub_{key}", filename)
            used_file = filename
            used_cfg = candidate
            break
        except FileNotFoundError as e:
            last_err = str(e)
            continue
        except Exception as e:
            # Datei da, aber Fehler beim Laden -> melden, nicht weiter probieren
            return (False, None, f"{filename}: {e}\n{traceback.format_exc(limit=1)}")
    else:
        return (False, None, f"keine Datei (versucht: {[c[0] for c in cfg['candidates']]}) — last: {last_err}")
    # Aufrufen: class vs func
    try:
        if used_cfg[1] == "class":
            cls_name = used_cfg[2]; method_name = used_cfg[3]
            cls = getattr(mod, cls_name)
            instance = cls()
            result = getattr(instance, method_name)()
        elif used_cfg[1] == "func":
            func_name = used_cfg[2]
            func = getattr(mod, func_name)
            # defrag.alle4() braucht kein arg, gibt dict mit _zeuge (nicht json-fähig) -> säubern
            result = func()
        else:
            raise ValueError(f"Unbekannter kind: {used_cfg[1]}")
        # _zeuge ist nicht JSON-fähig -> raus
        if isinstance(result, dict):
            result = {k: v for k, v in result.items() if not k.startswith("_")}
        return (True, {"file": used_file, "result": result}, "")
    except Exception as e:
        return (False, None, f"{used_file}: {e}\n{traceback.format_exc(limit=2)}")

def main(argv):
    args = [a.lower() for a in argv[1:]]
    if not args or args == ["alle"]:
        keys = ALLE
    else:
        keys = [a for a in args if a in CFG]
        if not keys:
            print(f"Unbekannt: {args} — nutze: pq octa org defrag / alle"); return 2
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"=== hub.py · {stamp} ===")
    print(f"Aufruf: {keys}")
    print()
    ok = 0; fehlt = 0
    lines = [f"=== hub.py · {stamp} ===", f"Aufruf: {keys}"]
    for key in keys:
        print(f"--- {key} ---")
        print(f"[{key}] geladen: {CFG[key]['candidates'][0][0]} (versucht)")
        success, data, err = run_one(key)
        if success:
            ok += 1
            print(f"[{key}] OK")
            # Kurz-Resultat, nicht das ganze Log
            res = data["result"]
            if isinstance(res, dict):
                kurz = {k: res[k] for k in list(res.keys())[:6]}
            else:
                kurz = str(res)[:200]
            print(f"Result: {json.dumps(kurz, ensure_ascii=False, default=str)[:600]}")
            lines.append(f"  ✓ {key} ({data['file']})")
        else:
            fehlt += 1
            print(f"[{key}] FEHLT / FEHLER: {err.splitlines()[0] if err else ''}")
            lines.append(f"  ✗ {key}: {err.splitlines()[0] if err else ''}")
        print()
    print(f"=== STAND ===")
    print(f"OK: {ok} · FEHLT: {fehlt} · Gesamt: {len(keys)}")
    for key in keys:
        mark = "✓" if key in [l.split()[1] for l in lines if l.strip().startswith("✓")] else "✗"
        # einfacher: aus ok/fehlt ableiten via lines
        pass
    # Log schreiben
    lines.append(f"OK: {ok} · FEHLT: {fehlt} · Gesamt: {len(keys)}")
    LOG.write_text("\n".join(lines), encoding="utf-8")
    print(f"Log: {LOG}")
    return 0 if fehlt == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
