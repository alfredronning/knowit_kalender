
from datetime import date, timedelta

start = date(2020, 4, 1)
end = date(2024, 12, 12)

streaks = []

sunday_count = 0
count = 0
while start <= end:
    if start.weekday() == 6:
        if start.month == 12 or start.month == 7 or sunday_count == 2:
            streaks.append(count)
            count = 0
            sunday_count = 0
        else:
            sunday_count += 1
            count += 1
    else:
        count += 1
    start += timedelta(days=1)
streaks.append(count)

f = dict()

fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
f[4] = sum(fibs[:5])
f[6] = sum(fibs[:7])
f[13] = sum(fibs[:14])
f[18] = sum(fibs[:19])
f[20] = sum(fibs[:21])
print(sum(f[i] for i in streaks))
