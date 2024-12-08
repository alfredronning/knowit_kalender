i = 10000000

def er_lystig(n):
    sn = str(n)
    if len(sn) == 1:
        return n == 1
    return er_lystig(sum(int(s)**2 for s in sn))

def er_jule_3(n):
    if not er_lystig(n):
        return False
    sn = str(n)
    if len(sn) == 1:
        return True
    if not er_lystig(int(sn[:len(sn)//2])) or not er_lystig(int(sn[-(len(sn)//2):])):
        return False
    if len(sn) > 3:
        for i in range(len(sn)-3):
            if not er_lystig(int(sn[i:i+3])):
                return False
    return True

while i > 0:
    if er_jule_3(i):
        print(i)
        break
    i -= 1

