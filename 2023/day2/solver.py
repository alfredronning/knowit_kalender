if __name__ == "__main__":
    log = open("log.txt").read().strip().split(", ")
    locks = 0
    pins = [True]*7
    for e in log:
        k, _, n = e.split()
        pins[int(n)-1] = k == "klakk"
        if not any(pins):
            pins = [True]*7
            locks += 1
    print(locks)


