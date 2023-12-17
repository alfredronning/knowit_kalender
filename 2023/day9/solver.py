def find_start(neighbours):
    for n in neighbours:
        if len(neighbours[n]) == 1:
            return n

if __name__ == "__main__":
    rekke = eval(open("rekke.txt").read())
    neighbours = dict()
    for x, y in rekke:
        if x in neighbours:
            neighbours[x].append(y)
        else:
            neighbours[x] = [y]
        if y in neighbours:
            neighbours[y].append(x)
        else:
            neighbours[y] = [x]

    current = find_start(neighbours)
    for i in range(len(rekke)//2):
        neighbour = neighbours[current][0]
        neighbours[neighbour].remove(current)
        current = neighbour
    print(int(current) + int(neighbours[current][0])) #type: ignore

