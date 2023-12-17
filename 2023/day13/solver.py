def is_prime(p):
    if p<=3:
        return p>1
    if p%3==0: 
        return False
    for i in range(5, int(p**0.5)+1, 6):
        if p%i==0 or p%(i+2)==0:
            return False
    return True

if __name__ == "__main__":
    working = [int(i) for i in open("alver_på_jobb.txt").readlines()]
    not_working = [int(i) for i in open("alver_ikke_på_jobb.txt").readlines()]
    grinchen = set(int(i) for i in open("grinchen.txt").readlines())
    windows = 400009

    primes = [2]
    m = max(max(working), max(not_working))
    i = 3
    while len(primes) <= m:
        if is_prime(i):
            primes.append(i)
        i += 2

    lights = set()
    for elf in working:
        lights.add(elf*2%windows)
        lights.add((elf+primes[elf])%windows)

    caught = 0
    for elf in not_working:
        if elf*2%windows not in lights or (elf+primes[elf])%windows not in lights:
            continue
        caught += elf*2%windows in grinchen or (elf+primes[elf])%windows in grinchen
    print(caught)

