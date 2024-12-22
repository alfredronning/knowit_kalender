def parse_brikker(brett):
    brett = brett.split("\n")
    brikker = set()
    for i, row in enumerate(brett):
        for j, t in enumerate(row):
            brikker.add((len(brett)-1-i, j, t))
    return brikker

def finn_naboer(brikker, brikke):
    visited = {brikke}
    queue = [brikke]
    while queue:
        current = queue.pop()
        for d in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
            nabobrikke = (current[0]+d[0], current[1]+d[1], current[2])
            if nabobrikke not in brikker:
                continue
            if nabobrikke in visited:
                continue
            visited.add(nabobrikke)
            queue.append(nabobrikke)
    return visited

def graviter_brett(brikker):
    for brikke in sorted(brikker):
        h = brikke[0]
        flyttet = False
        while h != 0 and not any(b[0] == h-1 and b[1] == brikke[1] for b in brikker):
            h -= 1
            flyttet = True
        if flyttet:
            brikker.remove(brikke)
            brikker.add((h, brikke[1], brikke[2]))

def finn_prepops(brikker):
    for b in brikker:
        if any((b2[1]-b[1]) in [-1, 1] and b2[2] == b[2] for b2 in brikker):
            continue
        brikker_paa_siden = []
        brikker_over = []
        brikker_under = []
        for b2 in brikker:
            if b2[1]-b[1] in [-1, 1] and b2[2] == b[2]:
                brikker_paa_siden.append(b2)
            if b2[1] == b[1]:
                if b2[0] > b[0]:
                    brikker_over.append(b2)
                elif b2[0] < b[0]:
                    brikker_under.append(b2)
        if len(brikker_over) or len(brikker_paa_siden):
            continue
        sammenhengende = True
        current = b
        for b2 in sorted([b2 for b2 in brikker_under if b2[2] == b[2]], reverse=True):
            if current[0] != b2[0]+1:
                sammenhengende = False
                break
            current = b2
        if sammenhengende:
            return b

def beste_moves(brikker, moves, cache):
    visited = set()
    best = float("inf")
    min_remainding = len(set(b[2] for b in brikker))
    if moves+min_remainding >= cache["best"]:
        return best
    h = hash(frozenset(brikker))
    if h in cache["history"]:
        if cache["history"][h] <= moves:
            return float("inf")
        cache["history"][h] = moves
    if len(brikker) == 0:
        cache["best"] = moves
        return moves
    prepop = finn_prepops(brikker)
    if prepop is not None:
        fjernet_brikker = finn_naboer(brikker, prepop)
        new_brikker = set(b for b in brikker if b not in fjernet_brikker)
        return beste_moves(new_brikker, moves + 1, cache)
    for brikke in brikker:
        if brikke in visited:
            continue
        fjernet_brikker = finn_naboer(brikker, brikke)
        visited |= fjernet_brikker
        new_brikker = set(b for b in brikker if b not in fjernet_brikker)
        graviter_brett(new_brikker)
        best = min(best, beste_moves(new_brikker, moves + 1, cache))
    cache["history"][h] = moves
    return best
        
brikker = [parse_brikker(b) for b in open("stekebrett.txt").read().strip().split("\n\n")]
print(sum(beste_moves(b, 0, {"best": float("inf"), "history": dict()}) for b in brikker))

