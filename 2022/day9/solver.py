from collections import defaultdict

def finn_produksjon(temp, vann, kullsyre):
    if temp > 105 or temp < 95:
        return 0
    if vann > 1500 or vann < 400:
        return 0
    if kullsyre > 500 or kullsyre < 300:
        return 0
    produsert = vann-100 + kullsyre//10
    if temp >= 100:
        produsert -= produsert//40
    return produsert

if __name__ == "__main__":
    maskiner = open("julebrusmaskiner.txt").read().strip().split('\n')
    maskiner_produksjon = defaultdict(int)
    for maskin in maskiner:
        maskin_split = maskin.split(", ")
        navn = maskin_split[0][len("Maskin "):]
        temp = maskin_split[1][len("temperatur "):-1]
        vann = maskin_split[2][len("vann "):-1]
        kullsyre = maskin_split[3][len("kyllsyre "):-1]
        maskiner_produksjon[navn] += finn_produksjon(int(temp), int(vann), int(kullsyre))
    print("{} {}".format(sum(maskiner_produksjon.values()), max(maskiner_produksjon, key=maskiner_produksjon.get)))
