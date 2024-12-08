def is_prime(n):
    if n <= 3:
        return n > 1
    if n%2 == 0 or n%3 == 0:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

ds = []
prime_count = 0

res = 0
for i in range(10000000):
    if is_prime(i):
        prime_count += 1
        s_prime = str(i)
        if len(s_prime) > len(ds):
            ds.append(0)
        for i, d in enumerate(s_prime):
            ds[i] += int(d)
        primTalv = 0
        for i, d in enumerate(ds):
            primTalv += d*(10**i)
        if primTalv > 10000000:
            break
        if is_prime(primTalv):
            res += 1

print(res)


