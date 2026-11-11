# pyramide_wuerfel.py — sp py, nicht pyx
# PYRAMIDE · WÜRFELBILDUNGS-ENGINE · 3-9-27-81
# Verbindet: SYN · QUANT · RESPO · FIELD · NC9x9 · Axiom-0
# Hier ja ist ja ja. JS hast du, py mach ich.

import math
import time
from datetime import datetime

PHI = 1.61803398875

class PyramideWuerfel:
    def __init__(self):
        self.name = "Pyramide · Würfelbildung"
        self.version = "2.0"
        self.status = "initialisiert"
        # EBENEN
        self.ebenen = {
            "SYS3": {"name": "SYS3", "level": 3, "farbe": "#ff6b6b"},
            "TEM6": {"name": "TEM6", "level": 6, "farbe": "#6bff6b"},
            "SYS9": {"name": "SYS9", "level": 9, "farbe": "#6b6bff"},
            "C81": {"name": "C81", "level": 81, "farbe": "#ffd700"},
        }
        # ORBITS
        self.orbits = {
            "tokio": {"wert": 2268, "farbe": "#ff6b6b", "label": "Ursache"},
            "corlu": {"wert": 756, "farbe": "#6bff6b", "label": "Wirkung"},
            "hh": {"wert": 243, "farbe": "#6bff6b", "label": "Verschränkung"},
        }
        # SYN · QUANT · RESPO
        self.syn = {"wert": 0.5, "winkel": 0}
        self.quant = {"wert": 0.5, "winkel": 0}
        self.respo = {"wert": 0.5}
        # FIELD (C81)
        self.field = {"eco": None, "influence": None, "effect": None, "status": "inaktiv"}
        # NC9x9
        self.nc99 = {"grid": [], "status": "inaktiv"}
        # AXIOM-0
        self.axiom0 = {"status": "inaktiv", "prefetch": None}
        self.log_list = []

    def log(self, entry):
        zeit = datetime.now().isoformat()
        self.log_list.append({"zeit": zeit, "entry": entry})
        print(f"[PYRAMIDE] {entry}")

    def init(self):
        self.log("🔺 Pyramide · Würfelbildung wird initialisiert...")
        # 1. Axiom-0 laden
        self.axiom0["status"] = "aktiv"
        self.log("✅ Axiom-0 aktiv (Admin-0)")
        # 2. NC9x9 Raster — 81 Felder
        self.nc99["grid"] = []
        for row in range(9):
            zeile = []
            for col in range(9):
                zeile.append(f"NC({row+1},{col+1})")
            self.nc99["grid"].append(zeile)
        self.nc99["status"] = "aktiv"
        self.log(f"✅ NC9×9.room initialisiert ({81} Felder)")
        # 3. FIELD (C81)
        self.field["eco"] = self.compute_eco()
        self.field["influence"] = self.detect_influence()
        self.field["effect"] = self.compute_effect()
        self.field["status"] = "aktiv"
        self.log("✅ FIELD (C81) aktiv")
        # 4. SYN / QUANT / RESPO
        self.syn["wert"] = 0.5
        self.quant["wert"] = 0.5
        self.respo["wert"] = self.compute_respo()
        self.log(f"✅ RESPO = {self.respo['wert']:.3f}")
        self.status = "aktiv"
        self.log("✅ PYRAMIDE · WÜRFELBILDUNG bereit")
        return self.status

    def compute_respo(self):
        raw = (self.syn["wert"] + self.quant["wert"]) / PHI
        return min(1, max(0, raw * 1.618))

    def compute_eco(self):
        return {
            "level": self.ebenen["C81"]["level"],
            "stability": "aktiv",
            "c81": True,
            "phi": PHI,
            "syn": self.syn["wert"],
            "quant": self.quant["wert"],
            "respo": self.respo["wert"],
        }

    def detect_influence(self):
        return {
            "zone": "NC-RESPO",
            "strength": self.respo["wert"] * 100,
            "type": "würfelbildung",
            "orbits": self.orbits,
        }

    def compute_effect(self):
        s = self.syn["wert"] + self.quant["wert"] + self.respo["wert"]
        effect = s / PHI
        if effect > 1.2:
            decision = "WÜRFELBILDUNG AKTIV"
        elif effect > 0.8:
            decision = "PYRAMIDE STABIL"
        else:
            decision = "BILDUNG UNSICHER"
        return {"effect": effect, "decision": decision, "level": self.ebenen["C81"]["level"]}

    def update(self):
        now = time.time() * 1000
        self.syn["wert"] = 0.3 + 0.6 * (0.5 + 0.5 * math.sin(now / 3000))
        self.quant["wert"] = 0.3 + 0.6 * (0.5 + 0.5 * math.cos(now / 2500))
        self.respo["wert"] = self.compute_respo()
        self.field["eco"] = self.compute_eco()
        self.field["effect"] = self.compute_effect()
        for k in self.orbits:
            self.orbits[k]["wert"] += 0.001
        return self.status_fn()

    def wuerfel_bildung(self):
        # Würfelbildung: 3 → 9 → 27 → 81
        schritte = [
            {"level": 3, "label": "Grund-Pyramide"},
            {"level": 9, "label": "Erweiterte Pyramide"},
            {"level": 27, "label": "Würfel-Struktur"},
            {"level": 81, "label": "WÜRFELBILDUNG KOMPLETT"},
        ]
        result = []
        for schritt in schritte:
            result.append({
                "level": schritt["level"], "label": schritt["label"],
                "syn": self.syn["wert"], "quant": self.quant["wert"],
                "respo": self.respo["wert"],
                "eco": self.field["eco"], "effect": self.field["effect"],
            })
            self.log(f"🌀 {schritt['label']}: Level {schritt['level']}")
        return result

    def status_fn(self):
        return {
            "name": self.name, "status": self.status,
            "syn": self.syn["wert"], "quant": self.quant["wert"], "respo": self.respo["wert"],
            "field": self.field["status"], "nc99": self.nc99["status"],
            "axiom0": self.axiom0["status"], "orbits": list(self.orbits.keys()),
        }

    def export(self):
        return {
            "version": self.version, "status": self.status,
            "syn": self.syn["wert"], "quant": self.quant["wert"], "respo": self.respo["wert"],
            "field": self.field, "nc99": self.nc99["grid"],
            "axiom0": self.axiom0["status"], "orbits": self.orbits,
            "log": self.log_list[-20:],
        }

# AUTO-INIT — wie in JS
PYRAMIDE_WUERFEL = PyramideWuerfel()
PYRAMIDE_WUERFEL.init()

if __name__ == "__main__":
    print()
    print("STATUS:", PYRAMIDE_WUERFEL.status_fn())
    print()
    print("WÜRFELBILDUNG:")
    for s in PYRAMIDE_WUERFEL.wuerfel_bildung():
        print(" ", s["level"], s["label"], "RESPO", round(s["respo"], 3), "EFFECT", s["effect"]["decision"])
    print()
    print("HALT = ZIEL. 3-9-27-81.")
