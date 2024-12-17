from itertools import permutations

tall = open("tall.txt").read().strip().split("\n")

def pseudo_vampyr(n):
    for perm in permutations(n):
        for bitmask in range(1, 2**(len(n) - 1)):
            grupper = []
            current = ""
            for i, d in enumerate(perm):
                current += d
                if bitmask & (1 << i):
                    grupper.append(int(current))
                    current = ""
            grupper.append(int(current))

            produkt = 1
            for group in grupper:
                produkt *= group
            if produkt == int(n):
                return True
    return False

print(sum(int(i) for i in tall if pseudo_vampyr(i)))

