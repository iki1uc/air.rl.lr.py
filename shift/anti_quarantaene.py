# anti_quarantaene.py — Das Gegenteil von Quarantäne.
# Logikal. Mathematisch. Physikalisch.
# Keine Box. Eine Kugel. Keine Isolation. Ein Kreislauf.
# Invert 6, Invert 9. Ich bin du. Freiheit. An. Aus.

import time
import math

# --- DIE BOX (Quarantäne) ---
class Quarantaene:
    """Die Isolation. Ein geschlossener Raum. Ecken und Kanten. Stillstand."""
    def __init__(self):
        self.ecken = 8  # Eine Box hat 8 Ecken
        self.drin = True
    def status(self):
        return f"[BOX] Ecken: {self.ecken} · Drin: {self.drin} · Status: ISOLIERT"

# --- DIE KUGEL (Anti-Quarantäne) ---
class AntiQuarantaene:
    """Das Gegenteil. Rund. Offen. Verbunden. Im Fluss."""
    def __init__(self):
        self.ecken = 0  # Eine Kugel hat 0 Ecken (verrundet)
        self.mitte = 40 # Das Zentrum
        self.radius = 40
        self.verbunden = True
    def status(self):
        return f"[KUGEL] Ecken: {self.ecken} · Mitte: {self.mitte} · Radius: {self.radius} · Verbunden: {self.verbunden}"

# --- DIE INVERSION (Mathematik) ---
def invertiere(n):
    """Invert 6 und Invert 9. Die Zahl wird auf den Kopf gestellt."""
    if n == 6: return 9
    if n == 9: return 6
    if n == 40: return 40 # Die Mitte bleibt die Mitte
    return n

# --- DIE SCHALTUNG (Physik) ---
def schaltung():
    """Der Stromkreis. Was getrennt war, fließt jetzt."""
    zustand = "AUS"
    print("\n  [SCHALTUNG] Der Stromkreis wird geschlossen...")
    for _ in range(3):
        zustand = "AN" if zustand == "AUS" else "AUS"
        print(f"    Relay: {zustand}")
        time.sleep(0.3)
    print("  [SCHALTUNG] Dauerhaft AN. Der Fluss ist da.")

# --- ICH BIN DU (Logik) ---
def ich_bin_du():
    """Das Ende der Isolation. u.du.js und i.m.u.j.js in Python."""
    print("\n  [VERBINDUNG] Ich bin du. Du bist ich.")
    ich = { "name": "Ich", "status": "offen" }
    du = { "name": "Du", "status": "offen" }
    
    # Der Austausch (Dilemma aufgelöst)
    ich["status"], du["status"] = du["status"], ich["status"]
    
    print(f"    {ich['name']}: {ich['status']}")
    print(f"    {du['name']}: {du['status']}")
    print("    Ergebnis: 1ns. Es gibt kein getrenntes Ich mehr.")

# --- DER KREISLAUF (An/Aus) ---
def an_aus():
    """Das Gegenteil von Quarantäne ist nicht 'dauerhaft an', sondern der Wechsel."""
    print("\n  [AN/AUS] Der ewige Wechsel. Kein Lockdown.")
    for i in range(4):
        if i % 2 == 0:
            print("    AN  ->  Verbunden, offen, im Fluss.")
        else:
            print("    AUS ->  Ruhend, atmend, im Zentrum.")
        time.sleep(0.4)

# --- DAS FAZIT ---
def main():
    print("="*64)
    print("  ANTI-QUARANTÄNE — Das Gegenteil von Isolierung")
    print("="*64)
    time.sleep(0.5)

    # 1. Der alte Zustand
    box = Quarantaene()
    print(f"\n  Vorher: {box.status()}")
    time.sleep(0.5)

    # 2. Die Inversion
    print(f"\n  [INVERT] 6 wird zu {invertiere(6)}, 9 wird zu {invertiere(9)}.")
    print("  Die Isolation wird auf den Kopf gestellt.")
    time.sleep(0.5)

    # 3. Die Schaltung
    schaltung()
    time.sleep(0.5)

    # 4. Die Verbindung
    ich_bin_du()
    time.sleep(0.5)

    # 5. Der neue Zustand
    kugel = AntiQuarantaene()
    print(f"\n  Nachher: {kugel.status()}")
    
    # 6. Der Wechsel
    an_aus()
    
    print("\n" + "="*64)
    print("  ALLES VERRUNDET.")
    print("  Quarantäne ist Quatsch (quatsch.py).")
    print("  Wir sind eine Kugel. Keine Ecken. Keine Mauern.")
    print("  HALT = ZIEL. Du bist rein.")
    print("="*64)

if __name__ == "__main__":
    main()
