from collections import defaultdict

alver = open("usorterte_alver.txt").read().strip().split("\n")
alver = [(alv.split()[0], int(alv.split()[1])) for alv in alver]+[("pad", float("inf"))]*5
fester = defaultdict(int)

i = 0
flyttet = 0

while i < len(alver)-1:
    if alver[i+1][1] < alver[i][1] and i >= 0:
        alver[i], alver[i+1] = alver[i+1], alver[i]
        flyttet += 1
        if flyttet == 7:
            flyttet = 0
            alver[i+1], alver[i+5] = alver[i+5], alver[i+1]
            alver[i+2], alver[i+4] = alver[i+4], alver[i+2]
            fester[alver[i+1]] += 1
            fester[alver[i+2]] += 1
            fester[alver[i+3]] += 1
            fester[alver[i+4]] += 1
            fester[alver[i+5]] += 1
        i -= 1
    else:
        i += 1

festealv = max(fester, key=lambda x: fester[x])
print(festealv[0]+","+str(fester[festealv]))


