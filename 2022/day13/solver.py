from math import pi

if __name__ == "__main__":
    hoyde = 18-2
    radius = 5
    diagonal = (hoyde**2 + radius**2)**0.5
    areal = pi*diagonal*radius
    julepyntfasit = [(0.04, 10), (0.04, 15), (0.02, 30), (0.05, 15)]

    total = 0
    for dekningsprosent, kostnad in julepyntfasit:
        total += areal*dekningsprosent*kostnad
    print(round(total/10)*10)

