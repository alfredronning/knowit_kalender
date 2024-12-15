transaksjoner = open("transaksjoner.txt").read().strip().split("\n")

tall_map = {"J": 10000, "U": 5000, "L": 1000, "E": 500, "T": 100, "R": 50, "3": 10, "V": 5, "I": 1}
transaksjoner = [[tall_map[tall] for tall in transaksjon] for transaksjon in transaksjoner]

def decode(tall):
    index_sortert = sorted([i for i in range(len(tall))], key=lambda x: tall[x], reverse=True)
    res = 0
    oppspart = 0
    for i, t in enumerate(tall):
        if index_sortert[0] == i:
            res += t-oppspart
            oppspart = 0
        elif i != 0 and t > tall[i-1]:
            return 0
        else:
            oppspart += t
        index_sortert.remove(i)
    return res

print(max(decode(t) for t in transaksjoner))

