import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
li = [[] for _ in range(8)]
d = {}
ans = 0

for _ in range(N):
    this = input().rstrip()
    for idx,v in enumerate(this):
        li[8 - len(this) + idx].append(v)

t = 10000000

for l in li:
    for k, v in Counter(l).items():
        if k in d.keys():
            d[k] += t * v
        else:
            d[k] = t * v
    t /= 10

print(d)

cnt = 9

for i in sorted(d.items(), key = lambda x: -x[1]):
    ans += cnt * i[1]
    cnt -= 1

print(int(ans))