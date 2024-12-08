joe = open("joe.txt").read().split("\n")
teppe = open("teppe.txt").read().split("\n")

teppeset = set()
for i in range(len(teppe)):
    for j in range(len(teppe[i])):
        if teppe[i][j] == "x":
            teppeset.add((i, j))

def calc_point(o_x, o_y, joe, teppe, rotated):
    res = 0
    for i in range(len(joe)):
        for j in range(len(joe[i])):
           if ((j-o_x, i-o_y) if rotated else(i-o_x, j-o_y)) in teppe and joe[i][j] != " ":
                res += int(joe[i][j])
    return res

res = 0
for offset_x in range(len(joe)):
    for offset_y in range(len(joe[0])):
        tmp = max(calc_point(offset_x, offset_y, joe, teppeset, False), calc_point(offset_x, offset_y, joe, teppeset, True))
        res = max(res, tmp)
print(res)

