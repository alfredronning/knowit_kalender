ris = 100
erter = 100
gulroetter = 100
reinskjoett = 100
kringle = 100

d_ris = [0, 0, 1, 0, 0, 2]
d_erter = [0, 3, 0, 0]
d_gulroetter = [0, 1, 0, 0, 0, 8]
d_reinskjoett = [100, 80, 40, 20, 10]

t = 0
tomt_timer = 0
while kringle > 0:
    if ris == 0 and erter == 0 and gulroetter == 0:
        if reinskjoett == 0:
            kringle -= 1
        else:
            reinskjoett -= 2
    if ris > 0:
        ris = max(0, ris-5)
        if erter > 0:
            erter = max(0, erter-3)
        elif gulroetter > 0:
            gulroetter = max(0, gulroetter-3)
    elif erter > 0:
        erter = max(0, erter-5)
        if gulroetter > 0:
            gulroetter = max(0, gulroetter-3)
    else:
        gulroetter = max(0, gulroetter-5)

    ris += d_ris[t%len(d_ris)]
    erter += d_erter[t%len(d_erter)]
    if t > 30:
        gulroetter += d_gulroetter[t%len(d_gulroetter)]
    if tomt_timer == 50 and len(d_reinskjoett) > 0:
        reinskjoett += d_reinskjoett[0]
        d_reinskjoett = d_reinskjoett[1:]
        tomt_timer = 0
    if reinskjoett == 0:
        tomt_timer += 1
    t += 1

print(t)




