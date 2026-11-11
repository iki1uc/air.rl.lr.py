# BIENEN-WEISHEIT — atalardan
# 1 bis 5 offen. 6ter eye closed. Er wollte es so.

def bienen_weisheit():
    sammlung = []
    total = 0
    for n in [1, 2, 3, 4, 5]:
        # sammeln, nicht nehmen
        total += n
        sammlung.append(total)
        print(f"{n} -> sammelt sich -> {total}")

    # 6ter: eye closed. Er wollte es so.
    print("6 -> eye closed. Nicht aufmachen.")
    print("So 1. Alles liegen lassen.")
    return sammlung

if __name__ == "__main__":
    bienen_weisheit()
