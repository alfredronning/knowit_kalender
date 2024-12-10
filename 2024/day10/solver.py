joe = open("joe.txt").read().replace(" ", "0").split("\n")
teppe = open("teppe.txt").read().replace(" ", "0").split("\n")

teppeset = set()
teppeScore = dict()
for i in range(len(teppe)):
    for j in range(len(teppe[i])):
        if teppe[i][j] != "0":
            teppeset.add((i, j))
            teppeScore[(i, j)] = teppe[i][j]

maxres = 0

def calc_point(o_x, o_y, joe, teppe, score):
    res = 0
    for i in range(len(joe)):
        for j in range(len(joe[i])):
            if (i-o_x, j-o_y) in teppe:
                res += (-2 if joe[i][j] == "x" else int(joe[i][j]))*int(score[(i-o_x, j-o_y)])
    return res

def mirrorTeppe(tep, score, l):
    scoretmp = dict(((i[0], l-i[1]), score[i]) for i in tep)
    tep = set((i[0], l-i[1]) for i in tep)
    return tep, scoretmp

def rotateTeppe(tep, score):
    scoretmp = dict(((i[1], -i[0]), score[i]) for i in tep)
    tep = set((i[1], -i[0]) for i in tep)
    return tep, scoretmp

for a in range(2):
    for b in range(4):
        for offset_x in range(len(joe)):
            for offset_y in range(len(joe[0])):
                maxres = max(maxres, calc_point(offset_x, offset_y, joe, teppeset, teppeScore))
        teppeset, teppeScore = rotateTeppe(teppeset, teppeScore)
    teppeset, teppeScore = mirrorTeppe(teppeset, teppeScore, len(teppe[0]))
print(maxres)

