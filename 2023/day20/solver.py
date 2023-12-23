def getroll(p):
    roll = rolls[p][pointers[p]]
    pointers[p] = (pointers[p] + 1) % 1000
    return roll

if __name__ == "__main__":
    hp = 10000000
    sleiphet = 18

    rolls = [[int(i) for i in open(d).read().strip().split("\n")] for d in 
             ["d4.txt", "d6.txt", "d8.txt", "d10.txt", "d20.txt"]]
    pointers = [0, 0, 0, 0, 0]

    attacks = 0
    while hp > 0:
        if attacks%3 == 0:
            if getroll(4) + 8 >= sleiphet:
                hp -= max(getroll(1), getroll(1)) + 2 + getroll(0)
        elif attacks%3 == 1:
            if getroll(4) + 6 >= sleiphet:
                hp -= getroll(2) + 5
        else:
            if getroll(4) + 3 >= sleiphet:
                hp -= min(getroll(3), getroll(3)) + 6
        attacks += 1
    print(attacks)

