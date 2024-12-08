def finn_beste_bfs(veksledict):
    queue = [("NOK", 1000, [])]
    while len(queue):
        next_depth = []
        max_nok = 1000
        sti = ["NOK"]
        for valuta, belop, visited in queue:
            veklsekurser = veksledict[valuta]
            mulige_valg = [valuta for valuta in veklsekurser.keys() if valuta not in visited]
            if "NOK" in veklsekurser and belop*veklsekurser["NOK"] > max_nok:
                max_nok = belop*veklsekurser["NOK"]
                sti = visited + [valuta, "NOK"]
            next_depth += [(valg, belop*veklsekurser[valg], visited+[valuta]) for valg in mulige_valg]
        if max_nok > 1000:
            print(sti)
            return max_nok
        queue = next_depth
    return 1000

if __name__ == "__main__":
    vekslekurser = open("exchange.csv").read().strip()[:-1].split(', \n')
    vekslekurser = [[cell for cell in row.split(", ")[1:]] for row in vekslekurser]
    valutas = vekslekurser[0]
    veksledict = {}
    for row in range(1, len(vekslekurser)):
        veksledict[valutas[row-1]] = dict((valutas[i], float(kurs)) for i, kurs in enumerate(vekslekurser[row]) if kurs != "x")
    print(finn_beste_bfs(veksledict))

