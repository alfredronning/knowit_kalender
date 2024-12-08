def out_shuffle(deck):
    return deck[::2]+deck[1::2]

def tilbake_til_start(n):
    deck = [i for i in range(n)]
    count = 1
    current_shuffle = out_shuffle(deck)
    while current_shuffle != deck:
        current_shuffle = out_shuffle(current_shuffle)
        count += 1
    return count

def finnminste_stokk_med_shuffles(n):
    deck = 52
    while True:
        if tilbake_til_start(deck) == n:
            return deck
        deck += 2

if __name__ == "__main__":
    print(finnminste_stokk_med_shuffles(13))

