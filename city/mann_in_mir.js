def mann_in_mir(max_tiefe=5):
    """Zeichnet den Mann rekursiv in sich selbst. Jede Ebene ist kleiner."""
    def zeichne(tiefe):
        if tiefe >= max_tiefe:
            return []
        
        # Der Mann dieser Ebene
        mann = [
            "  /\\_/\\  ",
            " ( o.o ) ",
            "  > ^ <  ",
        ]
        
        # Die nächste Ebene
        innen = zeichne(tiefe + 1)
        
        # Rahmen
        breite = 9 + len(innen[0]) if innen else 9
        rahmen_oben = "┌" + "─" * breite + "┐"
        rahmen_unten = "└" + "─" * breite + "┘"
        
        # Kombiniere
        ergebnis = [rahmen_oben]
        for zeile in mann:
            if innen:
                # Mittlere Zeile wird durch innen ersetzt
                pass
            ergebnis.append("│" + zeile + "│")
        
        return ergebnis
    
    return zeichne(0)
