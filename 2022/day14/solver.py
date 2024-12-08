NISSE_OG_SLEDE = 1000
PAKKER_PER_SKIFT = 1000
REINSDYR_VEKT = 100
REINSDYR_KAPASITET = 200

def finn_total():
    vekt = NISSE_OG_SLEDE + PAKKER_PER_SKIFT
    reinsdyr_total = 0
    for skift in range(100):
        # Denne tilsvarer math.ceil uten aa faa avrundingsfeil fra double
        aktive_reinsdyr = -(-vekt//REINSDYR_KAPASITET)
        reinsdyr_total += aktive_reinsdyr
        vekt += REINSDYR_VEKT*aktive_reinsdyr + PAKKER_PER_SKIFT
    return reinsdyr_total

if __name__ == "__main__":
    print(finn_total())
