inp = open("grep.txt").read().strip().split("\n")

HOEYRE = set()
VENSTE = set()

hand = """
        xxx      |
      xxxxxxx    |
     xxxxxxxxx   |
    xxxxxxxxxxx  |
   xxxxxxxxxxxx  |
  xxxxxxxxxxxxx  |
  xxxxxxxxxxxxx  |
 xxxxxxxxxxxxx   |
 xxxxxxxxxxxx    |
          o      |
""".split("\n")[1:-1]
for i, line in enumerate(hand):
    for j, loc in enumerate(line):
        if loc == "x":
            VENSTE.add((len(hand)-1-i, j-10))
            HOEYRE.add((len(hand)-1-i, 10-j))

GREP = set()
START = (0, 250)
END = (999, 749)
for i in inp:
    x, y = i.split()
    GREP.add((int(x), int(y)))

def kan_gripe(current, bruker_hoeyre, tak):
    dist = (tak[0]-current[0], tak[1]-current[1])
    return dist in (HOEYRE if bruker_hoeyre else VENSTE)

def kalk_dist(current, tak):
    return ((current[0]-tak[0])**2+(current[1]-tak[1])**2)**0.5

def kortestevei():
    dists = dict()
    dists[(START, True)] = 0
    dists[(START, False)] = 0
    queue = [(START, True, 0), (START, False, 0)]
    best = float("inf")
    while queue:
        current, bruker_hoeyre, dist = queue.pop(0)
        if dist > dists[(current, bruker_hoeyre)]:
            continue
        if dist >= best:
            continue
        if current == END:
            best = dist
            continue
        for tak in GREP:
            if tak[0] <= current[0]:
                continue
            if not kan_gripe(current, bruker_hoeyre, tak):
                continue
            next_dist = kalk_dist(current, tak) + dist
            if (tak, not bruker_hoeyre) in dists and dists[(tak, not bruker_hoeyre)] <= next_dist:
                continue
            dists[(tak, not bruker_hoeyre)] = next_dist
            queue.append((tak, not bruker_hoeyre, next_dist))
    return best

print(int(kortestevei()*10))

