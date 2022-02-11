# 백준 5692 팩토리얼 진법

import math
import sys

num_list = []

while True:
    n = sys.stdin.readline()[:-1]
    if n == '0':
        break
    else:
        num_list.append(n)

for i in num_list:
    l = len(i)
    ans = 0
    for j in i:
        ans += int(j) * math.factorial(l)
        l -= 1
    print(ans)


