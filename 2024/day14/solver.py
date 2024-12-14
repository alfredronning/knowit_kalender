sifre = dict((i, 100000) for i in range(10))

tom_rekkefolge = []
linjer = 0
while any(antall > 0 for antall in sifre.values()):
    linjer += 1
    for siffer in range(9, -1, -1):
        antall = sifre[siffer]
        if antall <= 0:
            melding = "0"+str(siffer)
        else:
            melding = str(antall) + str(siffer)

        for i in range(10):
            sifre[i] -= melding.count(str(i))
            if sifre[i] <= 0 and i not in tom_rekkefolge:
                tom_rekkefolge.append(i)
print(str(linjer) + " " + ",".join(str(i) for i in tom_rekkefolge))

