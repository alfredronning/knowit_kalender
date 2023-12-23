graphs = [open("graphs/graph_" + str(i) + ".txt").read().split("\n") for i in range(1, 11)]

earned = 0
for graph in graphs:
    stock_idx = 0
    stockprice, stockamount = graph[:-1], graph[-1].strip().split(", ")
    for i in range(len(stockprice[0])):
        for j in range(len(stockprice)):
            tile = stockprice[j][i]
            if tile == " ":
                continue
            if tile == "K":
                earned -= (150-j)*int(stockamount[stock_idx])
                stock_idx += 1
            if tile == "S":
                earned += (150-j)*int(stockamount[stock_idx])
                stock_idx += 1
print(earned) 

