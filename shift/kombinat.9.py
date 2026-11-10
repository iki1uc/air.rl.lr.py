# kombinat.9.py — 1 Basis, alle ableitbar
# 3 Ecken + 9 Ecken, rum um rum

ECKEN_3 = ["IN", "OUT", "CORE"]  # RESPO
ECKEN_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Feld, Mitte = 5 = 41

ZEUGEN_9 = [
    "pq.home", "pump.hit", "kreuz.quer",
    "UreE", "egal", "EPS",
    "frieden", "anomalie", "x.th",
]

def ableiten(zeuge, ziel):
    # ziel = "css" / "html" / "js" / "md"
    # 1 Zeuge, 1 Ziel, 1 Zeile — ableitbar, nicht kopiert
    return f"/* {zeuge} -> {ziel} | 3 Ecken {ECKEN_3} | 9 Ecken {ECKEN_9} */"

def kombinat():
    for zeuge in ZEUGEN_9:
        for ziel in ["css", "html", "js", "md"]:
            print(ableiten(zeuge, ziel))
    print("HOME 40 · HALT = ZIEL")

kombinat()
