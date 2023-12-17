from PIL import Image

def get_right_of(puzzle, left, top, visited):
    for piece in puzzle:
        if piece in visited:
            continue
        sides = puzzle[piece]
        if left in sides and top in sides:
            for rotation in range(4):
                if sides[rotation] == top and sides[(rotation-1)%4] == left:
                    return piece, rotation

def solve_puzzle(puzzle):
    connections = sum_connections = 0
    for _, sides in puzzle.items():
        for side in sides:
            if side == -1:
                continue
            connections += 1
            sum_connections += side
    summing_to = 2*sum_connections//connections

    grid = []
    visited = set()
    top = -1
    left = -1
    while True:
        if len(visited) == len(puzzle):
            break
        row = []
        while True:
            current = get_right_of(puzzle, left, top, visited)
            visited.add(current[0]) # type: ignore
            row.append(current)
            current_right = puzzle[current[0]][(1+current[1])%4] # type: ignore
            if current_right == -1:
                grid.append(row)
                break
            left = summing_to - current_right
            if len(grid):
                top_of = grid[-1][len(row)]
                top = summing_to - puzzle[top_of[0]][(2+top_of[1])%4] # type: ignore
        left = -1
        top_of = grid[-1][0]
        top = summing_to - puzzle[top_of[0]][(2+top_of[1])%4] # type: ignore
    return grid

def create_merged_image(grid):
    base_dir = "pieces/"
    total_height = sum(Image.open(base_dir+grid[0][0][0]).height for _ in grid)
    total_width = sum(Image.open(base_dir+grid[0][0][0]).width for _ in grid[0])

    merged_image = Image.new('RGB', (total_width, total_height))
    y_offset = 0
    for row in grid:
        x_offset = 0
        row_height = 0
        for piece in row:
            img = Image.open(base_dir+piece[0])
            img = img.rotate(90*piece[1])
            merged_image.paste(img, (x_offset, y_offset))
            x_offset += img.width
            row_height = max(row_height, img.height)
        y_offset += row_height
    return merged_image

if __name__ == "__main__":
    puzzle = [p.split(", [") for p in open("puzzle.txt").read().strip().split("\n")]
    puzzle = dict((p[0], [int(i) for i in p[1][:-1].split(", ")]) for p in puzzle)
    grid = solve_puzzle(puzzle)
    merged_image = create_merged_image(grid)
    merged_image.save("solution.jpg")

