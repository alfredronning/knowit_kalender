def count_bar(sjokk_2d, cut_squares, other_cut_squares, start, half):
    queue = [start]
    visited = set()
    while queue:
        current = queue.pop()
        visited.add(current)
        if len(visited) > half:
            return []
        for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            n = (current[0]+d[0], current[1]+d[1])
            if n[0] < 0 or n[1] < 0 or n[0] >= len(sjokk_2d) or n[1] >= len(sjokk_2d):
                continue
            if n in visited or sjokk_2d[n[0]][n[1]] == 0:
                continue
            if current in cut_squares and n in other_cut_squares:
                continue
            queue.append(n)
    return visited

def is_valid(sjokk, squares, width=8, transposed=False):
    half = squares//2
    if transposed:
        sjokk_2d = [[sjokk[i*width+j] for i in range(width)] for j in range(width)]
    else:
        sjokk_2d = [sjokk[i*width:i*width+width] for i in range(width)]
    for vert in range(0, width-1):
        neighbours = []
        for hor in range(0, width):
            if sjokk_2d[hor][vert] and sjokk_2d[hor][vert+1]:
               neighbours.append(hor)
        for i in range(len(neighbours)):
            for j in range(i+1, len(neighbours)+1):
                cuts = neighbours[i:j]
                cut_squares = set((c, vert) for c in cuts)
                other_cut_squares = set((c, vert+1) for c in cuts)
                count_left = count_bar(sjokk_2d, cut_squares, other_cut_squares, (cuts[0], vert), half)
                if len(count_left)*2 != squares:
                    continue
                count_right = count_bar(sjokk_2d, other_cut_squares, cut_squares, (cuts[0], vert+1), half)
                if len(count_left) == len(count_right):
                    if not any(l in count_right for l in count_left):
                        return True
    return False

if __name__ == "__main__":
    sjokkis = [[int(i) for i in sjokk] for sjokk in open("sjokkis.txt").read().strip().split("\n")]
    res = 0
    for sjokk in sjokkis:
        sjokk = [int(i) for i in sjokk]
        squares = sum(sjokk)
        if squares%2:
            continue
        if is_valid(sjokk, squares) or is_valid(sjokk, squares, transposed=True):
            res += 1
    print(res)

