# 시간 초과 남...

import sys
input = sys.stdin.readline

def bt(cnt):
    global ans
    if cnt == M:
        ans = min(ans, operation(chickens))
    else:
        for i in range(len(chickens)):
            tmp = chickens[i]
            chickens[i] = [1e9, 1e9]
            bt(cnt - 1)
            chickens[i] = tmp


def operation(chickens):
    min_cd = [1e9] * len(homes)
    for c in chickens:
        for idx, val in enumerate(homes):
            min_cd[idx] = min(min_cd[idx], abs(val[0] - c[0]) + abs(val[1] - c[1]))
    return sum(min_cd)


N, M = map(int, input().split())
graph = []
homes = []
chickens = []

for i in range(N):
    this = list(map(int, input().split()))
    graph.append(this)
    for j in range(N):
        if this[j] == 1:
            homes.append([i, j])
        elif this[j] == 2:
            chickens.append([i, j])

ans = 1e9

bt(len(chickens))

print(ans)



# 개선 코드 (itertools.combinations 사용)

import itertools

N, M = map(int, input().split())
graph = []
homes = []
chickens = []

for i in range(N):
    this = list(map(int, input().split()))
    graph.append(this)
    for j in range(N):
        if this[j] == 1:
            homes.append([i, j])
        elif this[j] == 2:
            chickens.append([i, j])

ans = 1e9

for c in itertools.combinations(chickens, M):
    tmp = 0
    for h in homes:
        chi_dis = N*N
        for j in range(M):
            chi_dis = min(chi_dis, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        tmp += chi_dis
    ans = min(ans, tmp)


print(ans)


