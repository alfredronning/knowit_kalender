sviller, bakke = open("el-paso_santa-cruz.txt").read().split("\n")[:2]

res = 0
for i in range(len(sviller)):
    current_sviller = sviller[i:i+29]
    current_bakke = bakke[i:i+29]
    if "g" in current_bakke:
        continue
    if current_bakke.count("j") == 29 and "*" not in current_sviller:
        res += 1
        continue
    if not "*" in current_sviller[24:]:
        continue
    if "*" in current_sviller[22:24]:
        continue
    if "s" in current_bakke[22:24]:
        continue
    if current_sviller[:10].count("*") > 1:
        continue
    res += 1
print(res)

