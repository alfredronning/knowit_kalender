kandidater = dict((c.split(" - ")[0], c.split(" - ")[1]) for c in open("kandidater.txt").read().strip().split("\n"))
stemmer = [(int(s.split(" - ")[2]), s.split(" - ")[3]) for s in open("stater.txt").read().strip().split("\n")]

valgnisser = dict((k, int(0)) for k in kandidater)

for tot_valgnisser, stemme_fordeling in stemmer:
    stemme_fordeling = dict((s.split(": ")[0], int(s.split(": ")[1])) for s in stemme_fordeling.split(", "))
    tot = sum(stemme_fordeling.values())
    tmp_valgnisser = dict((k, float(0)) for k in kandidater)
    for kandidat in stemme_fordeling:
        tmp_valgnisser[kandidat] += stemme_fordeling[kandidat]*tot_valgnisser/tot
    for kandidat in tmp_valgnisser:
        valgnisser[kandidat] += int(tmp_valgnisser[kandidat])
        tot_valgnisser -= int(tmp_valgnisser[kandidat])
        tmp_valgnisser[kandidat] -= int(tmp_valgnisser[kandidat])
    while tot_valgnisser > 0:
        stoerst_rest = max(tmp_valgnisser, key=lambda x: tmp_valgnisser[x])
        tot_valgnisser -= 1
        valgnisser[stoerst_rest] += 1
        tmp_valgnisser[stoerst_rest] = 0

vinner = max(valgnisser, key=lambda x: valgnisser[x])
print(kandidater[vinner] + " - " + str(valgnisser[vinner]))


