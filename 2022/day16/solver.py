from PIL import Image
import numpy as np

if __name__ == "__main__":
    # Bruker kun 2 least significant bits fra hver piksel
    harambe = np.array(Image.open("harambe.png")) & 0b11
    giraffe = np.array(Image.open("giraffe.png")) & 0b11

    res = harambe ^ giraffe

    im = Image.fromarray(res.astype(np.uint8)*64)
    im.save("res.png")

