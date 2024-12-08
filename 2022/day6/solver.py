def tell_stemmer(stemmer, slemme_handlinger):
    julenissen = 0
    sneglulf = 0
    alvekongen = 0
    for stemme in stemmer:
        handlinger, kandidat = stemme.split(":")
        weight = min(float(slemme_handlinger[handling]) if handling in slemme_handlinger.keys() else 1 for handling in handlinger.split(","))
        if kandidat == "julenissen":
            julenissen += weight
        elif kandidat == "sneglulf":
            sneglulf += weight
        elif kandidat == "alvekongen":
            alvekongen += weight
    return julenissen - max(sneglulf, alvekongen)

if __name__ == "__main__":
    stemmer = open("stemmer.txt").read().strip().split("\n")
    slemme_handlinger = open("slemmehandlinger.txt").read().strip().split("\n")
    slemme_handlinger_dict = dict(handling.split(":") for handling in slemme_handlinger)
    seiersmargin = tell_stemmer(stemmer, slemme_handlinger_dict)
    print(round(seiersmargin))

