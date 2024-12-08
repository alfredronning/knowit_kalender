from itertools import permutations

def papirlengde(x, y, z):
    lengder = []
    for permutation in permutations([x, y, z], 3):
        current_x, current_y, current_z = permutation
        if current_x+min(current_y, current_z) <= 110:
            lengde = 2*(current_y+current_z)
            # Blir dobbelt så kort hvis man kan brette papiret over på tvers vs på langs
            if 2*(current_x+current_y) <= 110:
                lengde //= 2
            lengder.append(lengde)
    return 0 if not len(lengder) else min(lengder)

if __name__ == "__main__":
    f = open("pakker.csv").read().strip().split("\n")[1:]
    pakker = [pakke.split(",") for pakke in f]
    total_lengde = sum(papirlengde(int(pakke[0]), int(pakke[1]), int(pakke[2])) for pakke in pakker)
    print(total_lengde)

