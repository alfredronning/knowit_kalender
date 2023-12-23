def calc_dist(p1, p2):
    x = p1[0]-p2[0]
    y = p1[1]-p2[1]
    return (x**2+y**2)**0.5*55500

def calc_time(adresser, choose_mode, canon):
    if canon == 0:
        rad, reload, overheat = 2000, 62, 0.1
    elif canon == 1:
        rad, reload, overheat = 1000, 22, 0.05
    else:
        rad, reload, overheat = 500, 16, 0.002

    visited = set()
    remainding = len(adresser_north)
    shots_fired = 0
    direction = 0
    pointers = [0, 0, 0, 0]
    while remainding > 0:
        while adresser[direction][pointers[direction]] in visited:
            pointers[direction] += 1
        adresse = adresser[direction][pointers[direction]]
        r = max(rad*0.2, rad-rad*overheat*shots_fired)
        for other in adresser[direction][pointers[direction]:]:
            if calc_dist(adresse, other) <= r:
                visited.add(other)
        remainding = len(adresser_north) - len(visited)
        shots_fired += 1
        if choose_mode == 0:
            pass
        elif choose_mode == 1:
            direction = (direction+1)%4
        else:
            if remainding%5 == 0:
                pass
            elif remainding%2 == 0:
                direction = (direction-1)%4
            else:
                direction = (direction+1)%4
    return shots_fired*reload-reload

if __name__ == "__main__":
    adresser = [(float(a.split()[0]), float(a.split()[1])) for a in open("gateadresser_oslo_koordinater_liten.txt").read().strip().split("\n")]
    adresser_north = sorted(adresser, key = lambda x: (-x[0], -x[1]))
    adresser_east = sorted(adresser, key = lambda x: (-x[1], x[0]))
    adresser_south = sorted(adresser, key = lambda x: (x[0], x[1]))
    adresser_west = sorted(adresser, key = lambda x: (x[1], -x[0]))
    adresser = [adresser_north, adresser_east, adresser_south, adresser_west]

    res = float("inf")
    for choose_mode in range(3):
        for canon in range(3):
            res = min(res, calc_time(adresser, choose_mode, canon))
    print(res)