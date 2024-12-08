if __name__ == "__main__":
    gløgg = []
    alver = open("alv_sti.txt").read().strip().split("\n")[1:]
    direct = {"g": (0, 0), "e": (1,0), "v": (-1,0), "n": (0,1), "s": (0,-1)}
    for alv in alver:
        pos, moves = alv.split(")")
        pos = [int(pos.split(", ")[0][1:]), int(pos.split(", ")[1])]
        for move in moves:
            if move == "g":
                gløgg.append((pos[0], pos[1]))
            pos[0] += direct[move][0]
            pos[1] += direct[move][1]
    print(len(set(gløgg)))

