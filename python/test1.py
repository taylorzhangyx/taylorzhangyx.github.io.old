import random
from collections import defaultdict

# sampling

sampleCount = 100
selectCount = 5


def sample():
    res = []

    for i in range(selectCount):
        res.append(i)

    for i in range(selectCount, sampleCount):
        r = random.randint(0, i)
        if r < selectCount:
            res[r] = i

    return res


dic = defaultdict(int)
for k in range(10000):
    res = sample()
    if k % 100 == 0:
        print(k)
    for s in res:
        dic[s] += 1

print(dic)
