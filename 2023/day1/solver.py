if __name__ == "__main__":
    goals = open("goals.txt").read().strip().split(",")
    bets = open("bets.txt").read().strip().split("], ")

    sukkerstenger = 50_000

    for i in range(len(goals)):
        g, odds = bets[i][1:].split(", ")
        bet = round(sukkerstenger*0.175)
        if int(goals[i]) >= int(g):
            sukkerstenger += round(bet*float(odds))
        else:
            sukkerstenger -= bet
    print(50_000 - sukkerstenger)

