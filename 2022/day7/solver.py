from PIL import Image
import numpy as np

def skriv_til_fil(matrix, filnavn):
    im = Image.fromarray(matrix)
    im.save(filnavn)


def finn_onde_piksler(matrix):
    res = []
    for row in matrix:
        res.append([255 if bin(num).count("1")%2==0 else 0 for num in row])
    return res

if __name__ == "__main__":
    kryptert = open("encrypted.txt").read().splitlines()
    kryptert_matrix = [[int(num) for num in row.split()] for row in kryptert]
    onde_piksler = finn_onde_piksler(kryptert_matrix)
    skriv_til_fil(np.asarray(onde_piksler, dtype=np.uint8), "solved.png")

