import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()
points = [[float(f) for f in l.split()] for l in open("lekescan.txt").read().strip().split("\n")]
x, y, z = zip(*points)
scatter = plt.scatter(y, [1-p for p in x], s=z)
plt.savefig('res.png', format='png')
plt.show()
