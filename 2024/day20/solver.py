from collections import defaultdict

alver = open("usorterte_alver.txt").read().strip().split("\n")
alver = [(alv.split()[0], int(alv.split()[1])) for alv in alver]
fester = defaultdict(int)

i = 0
flyttet = 0

while i < len(alver)-1:
    if i >= 0 and alver[i+1][1] < alver[i][1]:
        alver[i], alver[i+1] = alver[i+1], alver[i]
        flyttet += 1
        if flyttet == 7:
            flyttet = 0
            try:
                alver[i+1], alver[i+5] = alver[i+5], alver[i+1]
                alver[i+2], alver[i+4] = alver[i+4], alver[i+2]
            except:
                alver[i+1:i+6] = alver[i+1:i+6][::-1]
            for alv in alver[i+1:i+6]:
                fester[alv] += 1
        i -= 1
    else:
        i += 1

festealv = max(fester, key=lambda x: fester[x])
print(festealv[0]+","+str(fester[festealv]))


