def finn_vannstand(vannstand, x):
    for i in range(len(vannstand)):
        if vannstand[i][x] != " ":
            return i

def finn_energi_vannkraft(filnavn, vaer):
    vannstand = open(filnavn).read().split("\n")
    kwh = 0
    forrige = finn_vannstand(vannstand, 0)
    for x in range(1, len(vannstand[0])):
        neste = finn_vannstand(vannstand, x)
        if neste > forrige:
            if vaer[x-1] == "Mye regn":
                kwh += 120000
            else:
                kwh += 100000
        elif neste == forrige:
            if vaer[x-1] == "Mye regn":
                kwh += 80000
            else:
                kwh += 60000
        else:
            if vaer[x-1] == "Mye regn":
                kwh += 40000
            else:
                kwh += 5000

        forrige = neste
    return kwh

if __name__ == "__main__":
    kwh = 0
    vaer = open("vaer.csv").read().strip().split("\n")[1:]
    regn = [rad.split(",")[1] for rad in vaer]
    kwh += finn_energi_vannkraft("vannstand.txt", regn)
    print(kwh)

