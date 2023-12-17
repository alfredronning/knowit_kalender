def finn_beste(kurs):
    mi = None
    ma = None
    diff = -float("inf")
    for i in range(len(kurs)):
        for j in range(i+1, len(kurs)):
            tmp_diff = kurs[j]-kurs[i]
            if tmp_diff > diff:
                diff = tmp_diff
                mi = kurs[i]
                ma = kurs[j]
    return mi, ma

if __name__ == "__main__":
    kurs = open("input.txt").read().strip().split("\n")
    kr = 200_000
    for bors in kurs:
        kurs = [int(i) for i in bors.split(",")]
        mi, ma = finn_beste(kurs)
        aksjer = kr//mi
        kr = kr + aksjer*(ma-mi)
    print(kr)
        
