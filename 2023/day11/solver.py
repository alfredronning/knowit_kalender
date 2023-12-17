def traverse_spot(spot, land, visited):
    queue = [spot]
    while queue:
        current = queue.pop()
        for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            neighbour = (current[0]+d[0], current[1]+d[1])
            if neighbour not in visited and neighbour in land:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    kart = open("kart.txt").read().split("\n")
    land = set()
    for i in range(len(kart)):
        for j in range(len(kart[i])):
            if kart[i][j] == "X":
                land.add((i, j))
    islands = 0
    visited = set()
    for landspot in land:
        if landspot not in visited:
            traverse_spot(landspot, land, visited)
            islands += 1
    print(islands)

