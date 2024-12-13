kamper = open("salary.txt").read().strip().split("\n") 

loenn = 0

vanselighet = {
    "FCB": 1,
    "J": 2,
    "NT": 1,
    "NF": 1,
    "SP": 2,
    "VM": 3,
}

tap_streak = 0


for kamp in kamper:
    lag, spilt, bane, score, utmerkelser = kamp.split("/")
    kamploenn = int(spilt)*100
    modifikator = 0
    scoret = int(score.split("-")[0 if bane == "H" else 1])
    sluppet_inn = int(score.split("-")[1 if bane == "H" else 0])
    modifikator += 5*scoret
    modifikator -= 5*sluppet_inn
    modifikator += 1*utmerkelser.count("A")
    modifikator += 2*utmerkelser.count("S")
    modifikator += 2*utmerkelser.count("B")
    vansk = int(vanselighet[lag])
    modifikator += vansk if scoret > sluppet_inn else -vansk if scoret < sluppet_inn else 0

    if scoret > sluppet_inn:
        if tap_streak == 1:
            modifikator += 3
        if tap_streak > 1:
            modifikator += 3 + tap_streak-1
        tap_streak = 0
    elif scoret < sluppet_inn:
        tap_streak += 1

    loenn += kamploenn * (1 + modifikator/100)

print(int(loenn))
    
