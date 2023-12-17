def is_prime(n):
    if n <= 3:
        return n > 1
    if n%2 == 0 or n%3 == 0:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

def er_summe_dele_prim(n):
    s = sum(int(i) for i in str(n))
    if n%s:
        return False
    return is_prime(n//s)

if __name__ == "__main__":
    res = 0
    for i in range(10, 100000000):
        if er_summe_dele_prim(i):
            res += 1
    print(res)

