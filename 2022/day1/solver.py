def rekursiv_sjekk(letter, maxkeylen, zimbabwe_dict):
    if letter == "":
        return []
    for i in range(maxkeylen+1):
        if letter[:i] in zimbabwe_dict.keys():
            try:
                return [zimbabwe_dict[letter[:i]]] + rekursiv_sjekk(letter[i:], maxkeylen, zimbabwe_dict)
            except Exception:
                continue
    raise Exception("Ingen mulige videre valg")

if __name__ == "__main__":
    zimbabwe_dict = dict(line.split(",") for line in open("dictionary.txt").read().strip().split("\n"))
    letter = open("letter.txt").read().strip()
    maxkeylen = max(len(key) for key in zimbabwe_dict.keys())
    res = rekursiv_sjekk(letter, maxkeylen, zimbabwe_dict)
    print(len(" ".join(res)))

