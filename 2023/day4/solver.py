if __name__ == "__main__":
    reps = [int(i) for i in open("reps.txt").read().strip().split(", ")]
    longest = 0
    idx = 0
    current = 1
    for day in range(len(reps)):
        if day+1 == len(reps):
            if current > longest:
                longest = current
                idx = day - current + 1
            break
        if reps[day+1] > reps[day]:
            current += 1
        else:
            if current > longest:
                longest = current
                idx = day - current + 1
            current = 1
    print(sum(reps[idx:idx+longest]))

