def tversum(n):
    return sum(int(i) for i in str(n))

def is_prime(n):
    if n <= 3:
        return n > 1
    if n%2 == 0 or n%3 == 0:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

i = 0
prime_i = 0
tver_primes_i = 0
res = 0
while tver_primes_i < 10000:
    if is_prime(i):
        prime_i += 1
        if tversum(i) == tversum(prime_i):
            tver_primes_i += 1
            res += i
    i += 1

print(res)


