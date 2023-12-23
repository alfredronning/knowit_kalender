def check_lense(x, y, stars, seen):
    for i in range(-2, 3):
        fr, to = [[-5, 6], [-4, 5], [-2, 3]][abs(i)]
        for j in range(fr, to):
            check_x, check_y = ((x + i) % len(stars), (y + j) % len(stars[0]))
            if stars[check_x][check_y] == "*":
                seen.add((check_x, check_y))

if __name__ == "__main__":
    stars = open("stars.txt").read().split("\n")
    path = [[int(i) for i in p.split(", ")][::-1] for p in open("path.txt").read().strip().split("\n")]

    seen = set()
    x, y = path[0]
    shift = 0
    for end in path[1:]:
        dx = 0 if x == end[0] else 1 if x < end[0] else -1
        dy = 0 if y == end[1] else 1 if y < end[1] else -1
        while [x, y] != end:
            check_lense(x, y + shift, stars, seen)
            x += dx
            y += dy
            shift += 1
    print(len(seen))
