if __name__ == "__main__":
    pakker = open("data.csv").read().strip().split("\n")[1:]
    turer = 0
    while len(pakker):
        resterende_verdi = 1700
        resterende_volum = 120
        for pakke in pakker:
            pakke_verdi, pakke_volum = pakke.split(",")
            if resterende_verdi >= int(pakke_verdi) and resterende_volum >= int(pakke_volum):
                resterende_verdi -= int(pakke_verdi)
                resterende_volum -= int(pakke_volum)
                pakker.remove(pakke)
        turer += 1
    print(turer)

