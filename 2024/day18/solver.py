fem_counter = dict((i, int(0)) for i in range(1, 8))
rekke = [0, 1]
alvonacci = 1
potenser = dict((i, 5**i) for i in range(8))
top = 5**8-1
maks = 10**20
forrige_fem = False

while alvonacci < top:
    alvonacci += 1
    if alvonacci % 5 == 0:
        for i in range(7, 0, -1):
            if alvonacci % potenser[i] == 0:
                rekke.append(rekke[fem_counter[i]])
                fem_counter[i] += 1
                forrige_fem = True
                break
    else:
        rekke.append((rekke[-1]+rekke[-2])%maks)
        if forrige_fem:
            forrige_fem = False
            rekke[-1] = (rekke[-1]+rekke[-4])%maks
print(rekke[-1])

