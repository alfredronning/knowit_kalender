def refine(rekke, coins):
    changed = False
    for i in range(len(rekke)):
        for j in [-2, -1, 1, 2]:
            if i+j < 0 or i+j >= len(rekke):
                continue
            if rekke[i] > rekke[i+j] and coins[i] <= coins[i+j]:
                coins[i] += 1
                changed = True
            elif rekke[i] == rekke[i+j] and coins[i] < coins[i+j]:
                coins[i] += 1
                changed = True
    return changed


if __name__ == "__main__":
    rekke = eval(open("rekke.txt").read())
    coins = [1]*len(rekke)
    while refine(rekke, coins):
        pass
    print(sum(coins))

