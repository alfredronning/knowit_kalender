inp = open("tall.txt").read().strip()

tall_oversetter = {
    "seks": 6,
    "tolv": 12,
    "atten": 18,
    "tjuefire": 24,
    "tretti": 30,
    "førtito": 42,
    "førtiåtte": 48,
    "femtifire": 54,
    "seksti": 60,
    "syttito": 72,
    "syttiåtte": 78,
    "åttifire": 84,
    "nitti": 90,
}

tall_sortert = sorted(tall_oversetter.keys(), key=lambda x: -tall_oversetter[x])

res = 0
i = 0

while i < len(inp):
   for t in tall_sortert:
        if inp[i:i+len(t)] == t:
            res += tall_oversetter[t]
            i += len(t)
            break

print(res//6)

