if __name__ == "__main__":
    res = 0
    concat = ""
    for i in range(100_000):
        if str(i) not in concat:
            concat += str(i)
            res += 1
    print(res)

