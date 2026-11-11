def mann_in_mir(tiefe=0, max_tiefe=4):
    """Zeigt den Mann in sich selbst. Jede Ebene 90° gedreht."""
    einzug = "  " * tiefe
    if tiefe >= max_tiefe:
        return [einzug + "  ◉  " + D + f"(Kern {tiefe})" + R]
    
    drehung = tiefe * 90
    if drehung % 180 == 0:
        # Aufrecht
        mann = [
            einzug + "  /\\_/\\  ",
            einzug + " ( o.o ) ",
            einzug + "  > ^ <  ",
        ]
    else:
        # 90° gedreht (waagerecht)
        mann = [
            einzug + "  (o_o)  ",
            einzug + " /  |  \\ ",
            einzug + "  > ^ <  ",
        ]
    
    innen = mann_in_mir(tiefe + 1, max_tiefe)
    
    return mann + innen
