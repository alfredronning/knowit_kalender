from datetime import date, timedelta

current = date(2020, 4, 1)
end = date(2024, 12, 12)

fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]

res = 0
streak = 0
sunday_count = 0

def er_advent(day):
    if day.month != 12 and day.month != 11:
        return False
    if day.month == 12 and day.day > 24:
        return False
    if day.year == 2020:
        return day >= date(2020, 11, 29)
    if day.year == 2021:
        return day >= date(2021, 11, 28)
    if day.year == 2022:
        return day >= date(2022, 11, 27)
    if day.year == 2023:
        return day >= date(2023, 12, 3)
    if day.year == 2024:
        return day >= date(2024, 12, 1)


while current <= end:
    if current.weekday() == 6:
        if er_advent(current) or current.month == 7 or sunday_count == 2:
            sunday_count = 0
            streak = 0
        else:
            sunday_count += 1
            streak += 1
    else:
        streak += 1
    res += fibs[streak]
    current += timedelta(days=1)
print(res)

