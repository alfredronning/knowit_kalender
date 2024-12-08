if __name__ == "__main__":
    transaksjoner = [t.split(";") for t in open("transaksjoner.txt").read().strip().split("\n")]
    res = ""
    alph = "abcdefghijklmnopqrstuvwxyzæøå"
    for name, price, hash in transaksjoner:
        s = sum(alph.index(c.lower())+1 if c.lower() in alph else 0 for c in name)
        s *= int(price)
        s %= 0xbeef
        if s != int(hash):
            res += name[0]
    print(res)

