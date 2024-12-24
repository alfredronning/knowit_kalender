file = open("kryptert.txt", "rb").read()

res = bytearray()
res.append(file[0])

for b in file[1:]:
    res.append(res[-1]^b)

print(res.decode())

