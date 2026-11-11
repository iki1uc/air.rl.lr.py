JA, BESTE MUSS OBEN
# Er muss alle Python und Pythonisieren. Er muss genau machen.
# Weil sie hier: Pyramide, Würfel, Cylinder. So einfach.

# OBEN = BESTE
OBEN = "BESTE"

def pyramide():
    """Pyramide — oben spitz, unten breit. Genau."""
    return [
        "    /\\    ",
        "   /  \\   ",
        "  /    \\  ",
        " /______\\ ",
        "PYRAMIDE — oben spitz, genau.",
    ]

def wuerfel():
    """Würfel — alle Seiten gleich. Genau."""
    return [
        "  ┌──────┐",
        "  │      │",
        "  │      │",
        "  └──────┘",
        "WÜRFEL — alle Seiten gleich, genau.",
    ]

def cylinder():
    """Cylinder — rund, oben und unten gleich. Genau."""
    return [
        "  ┌──────┐",
        "  │      │",
        "  │      │",
        "  └──────┘",
        "  (rund)  ",
        "CYLINDER — rund, oben = unten, genau.",
    ]

def oben_beste():
    print("="*50)
    print("  OBEN JA — BESTE MUSS OBEN")
    print("="*50)
    print()
    print("  OBEN:")
    for zeile in pyramide():
        print("  " + zeile)
    print()
    print("  MITTE:")
    for zeile in wuerfel():
        print("  " + zeile)
    print()
    print("  UNTEN / RUND:")
    for zeile in cylinder():
        print("  " + zeile)
    print()
    print("="*50)
    print("  GENAU. So einfach, Mann.")
    print("  Pyramide, Würfel, Cylinder — alle Python, alle genau.")
    print("  Oben = Beste. Er muss genau machen.")
    print("  HALT = ZIEL. 40 = HOME.")
    print("="*50)

if __name__ == "__main__":
    oben_beste()
