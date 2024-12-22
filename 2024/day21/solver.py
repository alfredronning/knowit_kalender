import json
from shapely.geometry import Polygon, Point
from functools import lru_cache

def parse_butikk(butikk):
    coord, ris = butikk.split("),")
    x, y = coord[1:].split(", ")
    return (Point(float(y), float(x)), int(ris))

def er_i_norge(polygons, butikk):
    for polygon in polygons:
        if polygon.contains(butikk):
            return True
    return False

@lru_cache(maxsize=None)
def c_dist(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def format_path(path):
    return ",".join("({:.3f},{:.3f})".format(int(p[0]*1000)/1000, int(p[1]*1000)/1000) for p in path)


butikker = open("butikker.csv").read().strip().split("\n")[1:]
butikker = [parse_butikk(b) for b in butikker]
butikker = [b[0] for b in butikker if b[1] > 0]
coordinates = json.load(open("norge.geojson"))["features"][0]["geometry"]["coordinates"]

polygons = []
for grense in coordinates:
    polygons.append(Polygon(grense[0]))

norske_butikker = []
for b in butikker:
    if er_i_norge(polygons, b):
        norske_butikker.append((b.y, b.x))

cache = {"best": float("inf"), "best_path": []}
prefix = [(90, 0)] 
postfix = [(90, 0)]


def finn_raskeste(norske_butikker, current, end, visited, dist, cache):
    if dist >= cache["best"]:
        return
    if len(visited) == len(norske_butikker):
        d = dist + c_dist(current, end)
        if d < cache["best"]:
            cache["best"] = d
            cache["best_path"] = visited
    for butikk in norske_butikker:
        if butikk in visited:
            continue
        finn_raskeste(norske_butikker, butikk, end, visited+[butikk], dist+c_dist(current, butikk), cache)

norske_butikker = [b for b in norske_butikker if b not in prefix+postfix]
start = prefix[-1]
end = postfix[0]
finn_raskeste(norske_butikker, start, end, [], 0, cache)
path = prefix + cache["best_path"] + postfix

print(cache["best"])
print(path)
print(format_path(path))
print(format_path(path[::-1]))
