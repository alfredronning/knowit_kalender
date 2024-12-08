def finn_antall_kombinasjoner(hakk):
    if hakk == 0:
        return 0
    if hakk == 1:
        return 8
    kombinasjoner = [1]*10
    for i in range(hakk-1):
        kombinasjoner_tmp = []
        max_dybde_for_hakk = 8 if i == hakk-2 else 9 if i == hakk-3 else 10
        max_dybde_forrige = 9 if i == hakk-2 else 10
        for j in range(max_dybde_for_hakk):
            min_dybde = max(0, j-5)
            max_dybde = min(max_dybde_forrige, j+6)
            kombinasjoner_tmp.append(sum(kombinasjoner[dybde] for dybde in range(min_dybde, max_dybde)))
        kombinasjoner = kombinasjoner_tmp
    return sum(kombinasjoner)

if __name__ == "__main__":
    hakk = 7
    hakk2 = 19
    print(str(finn_antall_kombinasjoner(7))+":"+str(finn_antall_kombinasjoner(19)))

