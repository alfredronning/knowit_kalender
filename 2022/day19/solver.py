class Effekt:
    def __init__(self, navn):
        self.navn = navn
        self.varighet = 6 if navn == "S" else 2

    def utfoer_effekt(self, tyv):
        self.varighet -= 1
        if self.navn == "S":
            if self.varighet % 2 == 0:
                tyv.posisjon += 1
        elif self.navn == "A":
            if tyv.posisjon > 0:
                tyv.posisjon -= 1
        if self.varighet == 0:
            tyv.effekt = None


class Tyv:
    def __init__(self, posisjon_i_koe):
        self.posisjon_i_koe = posisjon_i_koe
        self.posisjon = -1
        self.effekt = None

    def flytt(self):
        if self.posisjon_i_koe:
            self.posisjon_i_koe -= 1
        else:
            if self.effekt is None:
                self.posisjon += 1
            else:
                self.effekt.utfoer_effekt(self)


class Forsvarspost:
    def __init__(self, navn, posisjon, alle_ruteposisjoner):
        self.navn = navn
        self.posisjon = posisjon
        self.cooldown = 3 if navn == "L" else 1
        self.aktiv_cooldown = 0
        self.posisjoner_i_rekkevidde = []
        # Finner alle posisjoner forsvarsposten har rekkevidde til hvis ikke forsvarsposten er laser
        if self.navn != "L":
            rekkevidde = 5 if self.navn == "S" else 10
            for i, ruteposisjon in enumerate(alle_ruteposisjoner):
                if ((self.posisjon[0]-ruteposisjon[0])**2+(self.posisjon[1]-ruteposisjon[1])**2)**0.5 <= rekkevidde:
                    self.posisjoner_i_rekkevidde.append(i)

    def paafoer_effekt(self, tyver):
        if self.aktiv_cooldown == 0:
            tyver_uten_effekt = [tyv for tyv in tyver if tyv.effekt is None]
            if self.navn == "L":
                # Laser har rekkevidde til alle som er inne på brettet
                tyver_i_rekkevidde = [tyv for tyv in tyver_uten_effekt if tyv.posisjon >= 0]
                if len(tyver_i_rekkevidde):
                    fremste_tyv = max(tyver_i_rekkevidde, key=lambda tyv: tyv.posisjon)
                    tyver.remove(fremste_tyv)
                    self.aktiv_cooldown = self.cooldown
            else:
                tyver_i_rekkevidde = [tyv for tyv in tyver_uten_effekt if tyv.posisjon in self.posisjoner_i_rekkevidde]
                if len(tyver_i_rekkevidde):
                    fremste_tyv = max(tyver_i_rekkevidde, key=lambda tyv: tyv.posisjon)
                    fremste_tyv.effekt = Effekt(self.navn)
                    self.aktiv_cooldown = self.cooldown
        elif self.aktiv_cooldown > 0:
            self.aktiv_cooldown -= 1


class Verden:
    def __init__(self, tyver, forsvarsposter, endeposisjon):
        self.tyver = tyver
        self.forsvarsposter = forsvarsposter
        self.endeposisjon = endeposisjon

    def er_over(self):
        if len(self.tyver):
            return max(self.tyver, key=lambda tyv: tyv.posisjon).posisjon == self.endeposisjon
        raise Exception("Alle tyver har blitt teleportert bort!")

    def neste_state(self):
        for tyv in self.tyver:
            tyv.flytt()
        for forsvarspost in self.forsvarsposter:
            forsvarspost.paafoer_effekt(self.tyver)


def lag_ruteposisjoner(punkter):
    # parser punktene fra input til tupler
    punkter = [(int(p.split(",")[0]), int(p.split(",")[1])) for p in punkter[1:-1].split("),(")]
    alle_posisjoner = []
    i = 0
    currentpunkt = [punkter[i][0], punkter[i][1]]
    while i < len(punkter)-1:
        alle_posisjoner.append((currentpunkt[0], currentpunkt[1]))
        # Beveger seg vertikalt
        if punkter[i][0] == punkter[i+1][0]:
            currentpunkt[1] += 1 if punkter[i+1][1] > punkter[i][1] else -1
        # Beveger seg horisontalt
        else:
            currentpunkt[0] += 1 if punkter[i+1][0] > punkter[i][0] else -1
        if currentpunkt[0] == punkter[i+1][0] and currentpunkt[1] == punkter[i+1][1]:
            i += 1
    alle_posisjoner.append(currentpunkt)
    return alle_posisjoner


def les_verden(tyver, forsvar, alle_ruteposisjoner):
    # parser forsvarspostene fra input til tupler
    forsvar_tuples = [(f.split(",")[0], int(f.split(",")[1]), int(f.split(",")[2])) for f in forsvar[1:-1].split("),(")]
    tyver_obj = [Tyv(i) for i, t in enumerate(tyver) if t == "T"]
    forsvar_obj = [Forsvarspost(f[0], (f[1], f[2]), alle_ruteposisjoner) for f in forsvar_tuples]

    return Verden(tyver_obj, forsvar_obj, len(alle_ruteposisjoner)-1)


def print_state(state, alle_posisjoner, tyver, t):
    print("t = " + str(t))

    max_x = max(alle_ruteposisjoner, key=lambda pos: pos[0])[0]
    max_y = max(alle_ruteposisjoner, key=lambda pos: pos[1])[1]
    board = [[" "]*(max_x+1) for _ in range(max_y+1)]
    for forsvar in state.forsvarsposter:
        board_pos = (max_y-forsvar.posisjon[1], forsvar.posisjon[0])
        board[board_pos[0]][board_pos[1]] = forsvar.navn
    for tyv in state.tyver:
        if tyv.posisjon >= 0:
            board_pos = (max_y-alle_posisjoner[tyv.posisjon][1], alle_posisjoner[tyv.posisjon][0])
            state_tyv = "T" if tyv.effekt is None else tyv.effekt.navn
            if board[board_pos[0]][board_pos[1]] == " " or board[board_pos[0]][board_pos[1]] == "t":
                board[board_pos[0]][board_pos[1]] = state_tyv.lower()
    for row in board[:-1]:
        print(" "*len(tyver), end="")
        print(row)
    print(" "*min(t, len(tyver))+tyver[t:][::-1], end="")
    print(board[-1])
    print()


if __name__ == "__main__":
    tyver, punkter, forsvar = open("input.txt").read().strip().split("\n")
    alle_ruteposisjoner = lag_ruteposisjoner(punkter)
    verden = les_verden(tyver, forsvar, alle_ruteposisjoner)

    t = 0
    while not verden.er_over():
        # print_state(verden, alle_ruteposisjoner, tyver, t)
        verden.neste_state()
        t += 1
    print(t)
