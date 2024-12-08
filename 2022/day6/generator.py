import random

JULENISSEN_WEIGHT = 0.63
SNEGLULF_WEIGHT = 0.17
ALVEKONGEN_WEIGHT = 0.20

def get_slemme_handlinger(filename):
    lines = open(filename).read().strip().split("\n")
    return [line.split(":")[0] for line in lines]

def get_snille_handlinger(filename):
    return open(filename).read().strip().split("\n")

def generer_stemme(handlinger):
    # velg 2-5 tilfeldinge handlinger
    handlinger = ",".join(random.sample(handlinger, 2+int(random.random()*3)))
    rand = random.random()
    # velg kandidat basert på vekter
    if rand < JULENISSEN_WEIGHT:
        kandidat = ":julenissen"
    elif rand < JULENISSEN_WEIGHT + SNEGLULF_WEIGHT:
        kandidat = ":sneglulf"
    else:
        kandidat = ":alvekongen"
    return handlinger+kandidat

def skriv_til_fil(stemmer, filename):
    file = open(filename, "w")
    file.write("\n".join(stemmer))
    file.close()

if __name__ == "__main__":
    slemme_handlinger = get_slemme_handlinger("slemmehandlinger.txt")
    snille_handlinger = get_snille_handlinger("snillehandlinger.txt")
    handlinger = slemme_handlinger + snille_handlinger
    stemmer = [generer_stemme(handlinger) for _ in range(5000)]
    skriv_til_fil(stemmer, "stemmer.txt")

