def finn_flippet(block):
    toerpotens = len(block)
    flippet_bit = 0
    while toerpotens-1:
        flippet_bit <<= 1
        flippet_bit += sum(b for j, b in enumerate(block) if j % toerpotens >= toerpotens >> 1) % 2
        toerpotens >>= 1
    return flippet_bit

def rett_flippet_bit(bits, i):
    return bits[:i] + [bits[i] ^ 1] + bits[i+1:]

def fjern_parity_bits(bits):
    return [b for i, b in enumerate(bits) if not i & (i-1) == 0]

def fiks_block(block):
    flippet_idx = finn_flippet(block)
    rettet = rett_flippet_bit(block, flippet_idx)
    return "".join(str(b) for b in fjern_parity_bits(rettet))

def fiks_alle_blocks(data, block_size):
    return "".join(fiks_block(data[i:i+block_size]) for i in range(0, len(data), block_size))

def bits_til_string(bits):
    return "".join(chr(int(bits[i*8:(i+1)*8], 2)) for i in range(len(bits)//8))

if __name__ == "__main__":
    data = [int(digit) for digit in open("input.txt").read().strip()]
    res = fiks_alle_blocks(data, 2**5)
    print(bits_til_string(res))
