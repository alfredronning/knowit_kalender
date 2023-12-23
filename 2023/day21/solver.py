print(sum((24-sum(int(n)*2 if not i%2 else int(n) for i, n in enumerate(k[:-2]))%24)%24 != int(k[-2:]) for k in open("kredittkort.txt").read().strip().split("\n")))
