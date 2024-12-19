def djombetall(i):
    bits = format(i, "016b")
    for i in range(2, 7):
        if bits[:i] == bits[i:i+i] and bits[i+i:i+8] == bits[i-8:]:
            return True
        if bits[:i] == bits[-i:] and bits[i:8] == bits[8:-i]:
            return True
        if bits[:i] == bits[8:8+i] and bits[i:8] == bits[-8+i:]:
            return True
    return False

res = 0
for i in range(65536):
    if djombetall(i):
        res += 1
print(res)
