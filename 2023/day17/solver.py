from matplotlib import pyplot as plt
from scipy.integrate import quad

def derivative(x, a, b):
    return 2 * a * x + b

def arc_length(x1, x0, a, b):
    integral, _ = quad(lambda x: (1 + derivative(x, a, b)**2)**0.5, x0, x1)
    return integral

def get_light_position(a, b, c, l):
    x0 = 0
    x1 = 10 
    step_size = 10
    while True:
        current_length = arc_length(x1, x0, a, b)
        if abs(current_length - l) < 1e-3:
            break
        if current_length < l:
            x1 += step_size
        else:
            x1 -= step_size
            step_size /= 2 
    y = a * x1**2 + b * x1 + c
    return x1, y

def add_points(row, points):
    function, lights = row.split(": ")
    a, b, c = [float(i) for i in function[1:-1].split()]
    lights = [[float(i) for i in p.split()] for p in lights[1:-1].split(") (")]
    for x, l, s in lights:
        x, y = get_light_position(a, b, c, x)
        points.append((int(x), int(y), l, s))

if __name__ == "__main__":
    input = open("input.txt").read().strip().split("\n")
    points = []
    for row in input[1:]:
        add_points(row, points)

    plt.figure()
    for x, y, l, size in points:
        plt.scatter(x, y, color="red", alpha=l, s=size)
    plt.savefig("res.png")

