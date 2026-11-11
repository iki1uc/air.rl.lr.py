# quantum_shuffle_syn.py
# Gerade = Weiß = Höhe. Ungerade = Schwarz = Breite.
# 90° verdreht. Ich in mir. Syn.

import time
import random
import os

# --- KONSTANTEN ---
WEISS = "█"
SCHWARZ = "░"
LEER = " "
MANN = "◉"

# --- QUANTEN-ZAHL ---
class Quant:
    """Eine Zahl ist in Superposition: gerade+ungerade zugleich.
    Erst beim Shuffle kollabiert sie zu einem Zustand."""
    def __init__(self, n):
        self.n = n
        self.ist_gerade = (n % 2 == 0)
        self.zustand = None  # None = Superposition
        self.achse = None     # "H" = Höhe, "B" = Breite
    
    def kollabiere(self):
        """Kollabiert die Superposition zu einem Zustand."""
        if self.ist_gerade:
            self.zustand = "WEISS"
            self.achse = "H"  # Höhe
        else:
            self.zustand = "SCHWARZ"
            self.achse = "B"  # Breite
        return self.zustand, self.achse

# --- DER MANN IN SICH (Rekursiv, 90° verdreht) ---
def mann_in_mir(tiefe, drehung=0, max_tiefe=5):
    """Zeichnet den Mann, der in sich selbst schaut.
    Jede Ebene ist 90° weiter gedreht."""
    if tiefe >= max_tiefe:
        return [" " * 20 + MANN]
    
    # Zeichne den Mann
    einrueckung = " " * (tiefe * 4)
    rahmen = ["┌" + "─" * (30 - tiefe * 4) + "┐"]
    zeilen = [
        einrueckung + "│" + " " * (14 - tiefe*4) + "  /\\_/\\  ",
        einrueckung + "│" + " " * (14 - tiefe*4) + " ( o.o ) ",
        einrueckung + "│" + " " * (14 - tiefe*4) + "  > ^ <  ",
    ]
    
    # Zeichne die nächste Ebene (in sich selbst)
    naechste = mann_in_mir(tiefe + 1, drehung + 90, max_tiefe)
    
    return rahmen + zeilen + naechste + [einrueckung + "└" + "─" * (30 - tiefe * 4) + "┘"]

# --- QUANTEN MANDALA (Schwarz/Weiß, Höhe/Breite) ---
def quanten_mandala(quants, breite=40):
    """Zeichnet das Quantum-Mandala aus den Zahlen.
    Gerade = Weiß = Höhe. Ungerade = Schwarz = Breite."""
    # Kollabiere alle Quants
    states = [q.kollabiere() for q in quants]
    
    # Erste Zeile: Reine Symbole
    zeile_1 = ""
    for i, (zustand, achse) in enumerate(states):
        if zustand == "WEISS":
            zeile_1 += WEISS * 2  # Weiß ist Höhe -> hoch
        else:
            zeile_1 += SCHWARZ * 2  # Schwarz ist Breite -> breit
    
    # Zweite Zeile: Achsen-Anzeige
    zeile_2 = ""
    for _, achse in states:
        zeile_2 += achse + " "
    
    return zeile_1, zeile_2
