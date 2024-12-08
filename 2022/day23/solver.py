from collections import defaultdict
import json

def les_data_json(mnd):
    data = []
    for i in range(mnd):
        j = json.loads(open("datajson/{:02d}.json".format(i+1)).read())
        for line in j:
            data.append((-1, line['started_at'], line['start_station_id']))
            data.append((1, line['ended_at'], line['end_station_id']))
    return sorted(data, key=lambda tur: tur[1])

if __name__ == "__main__":
    data = les_data_json(11)

    sykler_paa_sted = defaultdict(int)
    maks_negativ = defaultdict(int)

    for diff_sykkel, tid, sted in data:
        sykler_paa_sted[sted] += diff_sykkel
        if maks_negativ[sted] > sykler_paa_sted[sted]:
            maks_negativ[sted] = sykler_paa_sted[sted]

    print(-sum(maks_negativ.values()))

