def finn_grupper(bits):
    grupper = []
    toerpotens = 1
    while toerpotens < len(bits):
        current = []
        i = 0
        while i < len(bits):
            i += toerpotens
            current += bits[i:i+toerpotens]
            i += toerpotens
        grupper.append(sum(current) % 2 == 0)
        toerpotens<<=1
    return grupper

def finn_flippet_bit(bits, grupper):
    for i in range(len(bits)):
        tilhorende_grupper = []
        toerpotens = 1
        while toerpotens < len(bits):
            tilhorende_grupper.append(i//toerpotens % 2 == 0)
            toerpotens<<=1
        if tilhorende_grupper == grupper:
            return i

def rett_flippet_bit(bits, i):
    return bits[:i] + [bits[i]^1] + bits[i+1:]

def fjern_parity_bits(bits):
    return [b for i, b in enumerate(bits) if not i & (i-1) == 0]

if __name__ == "__main__":
    d = [int(d) for d in open("input.txt").read().strip()]

    block_size = 2**5
    res = []
    for i in range(len(d)//block_size):
        block = d[i*block_size:(i+1)*block_size]
        grupper = finn_grupper(block)
        if all(gruppe is True for gruppe in grupper):
            res += fjern_parity_bits(block)
            continue
        flippet_bit = finn_flippet_bit(block, grupper)
        rettet = rett_flippet_bit(block, flippet_bit)
        res += fjern_parity_bits(rettet)

    stringres = "".join(str(i) for i in res)
    print("".join(chr(int(stringres[i*8:(i+1)*8], 2)) for i in range(len(stringres)//8)))

