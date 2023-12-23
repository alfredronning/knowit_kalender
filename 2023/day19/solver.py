from collections import defaultdict

if __name__ == "__main__":
    kuler = [int(k[1:], 16) for k in open("kuler.txt").read().strip().split("\n")]
    halvor, alvhild = 0x811A89, 0x8EAA54

    children = defaultdict(lambda:[None, None])
    parent = dict()
    top = kuler[0]
    for kule in kuler[1:]:
        current = top
        while True:
            if kule > current:
                if children[current][1] is None:
                    children[current][1] = kule # type:ignore
                    parent[kule] = current
                    break
                else:
                    current = children[current][1]
            else:
                if children[current][0] is None:
                    children[current][0] = kule # type:ignore
                    parent[kule] = current
                    break
                else:
                    current = children[current][0]
    halvor_path = set()
    while halvor != top:
        halvor = parent[halvor]
        halvor_path.add(halvor)
    while alvhild not in halvor_path:
        alvhild = parent[alvhild]
    print(hex(alvhild))


