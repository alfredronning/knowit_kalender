def map_to_char(i):
    if i == 26:
        return "æ"
    if i == 27:
        return "ø"
    if i == 28:
        return "å"
    return chr(ord("a")+int(i))

if __name__ == "__main__":
    cipher = open("cypher.txt").read().strip().split("\n")
    keys = [[int(i) for i in k[1:-1].split(", ")] for k in open("input.txt").read().strip().split("\n")]

    i = 0
    first_letters = ""
    for row in cipher:
        res = []
        for word in row.split():
            key = keys[i]
            decipher_map = dict((map_to_char(c), map_to_char(j)) for j, c in enumerate(keys[i]))
            res.append("".join(decipher_map[c] if c not in "," else c for c in word))
            i += 1
        if res:
            first_letters += res[0][0]
        print(" ".join(res))
    print(first_letters)

