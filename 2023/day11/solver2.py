def traverse_spot(spot, kart, visited):
    queue = [spot]
    while queue:
        current = queue.pop()
        visited.add(current)
        for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            n = (current[0]+d[0], current[1]+d[1])
            if n[0] < 0 or n[1] < 0 or n[0] >= len(kart) or n[1] >= len(kart[0]):
                continue
            if n in visited:
                continue
            if kart[n[0]][n[1]] == "X":
                queue.append(n)

if __name__ == "__main__":
    kart = open("kart.txt").read().strip().split("\n")
    land = set()
    visited = set()
    islands = 0
    for i in range(len(kart)):
        for j in range(len(kart[i])):
            if kart[i][j] != "X" or (i, j) in visited:
                continue
            islands += 1
            traverse_spot((i, j), kart, visited)
    print(islands)

