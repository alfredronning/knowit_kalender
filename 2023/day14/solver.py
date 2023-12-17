push = [int(i) for i in open("push.txt").read().strip().split(", ")]

max_series_len = 0
series_start = 0
max_series_start = 0
increasing = True
for i in range(1, len(push)):
    if increasing:
        if push[i] < push[i-1]:
            increasing = False
    else:
        if push[i] > push[i-1]:
            if i-series_start > max_series_len:
                max_series_len = i-series_start
                max_series_start = series_start
            series_start = i-1
            increasing = True

print(sum(push[max_series_start:max_series_start+max_series_len]))

