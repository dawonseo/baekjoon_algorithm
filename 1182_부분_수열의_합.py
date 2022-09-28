# 백준 1182 부분 수열의 합

from itertools import combinations

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
comb = []
ans = 0

for i in range(1, N+1):
    comb.extend(list(combinations(num_list, i)))

for i in comb:
    if sum(i) == S:
        ans += 1

print(ans)