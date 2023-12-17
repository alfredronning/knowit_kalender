from math import ceil

if __name__ == "__main__":
    rute = [[int(j) for j in i.split(",")] for i in open("rute.txt").read().strip().split("\n")]
    lyng = 0
    for i in range(len(rute)-1):
        lyng += ((rute[i][0]-rute[i+1][0])**2+(rute[i][1]-rute[i+1][1])**2)**0.5
    print(ceil(lyng/1000*9))
