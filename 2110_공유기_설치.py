# 시간 초과

import itertools, sys
input = sys.stdin.readline

N, C = map(int, input().split())
home_list = []

for _ in range(N):
    home_list.append(int(input().strip()))

ans = 0

for routers in itertools.combinations(home_list, C):
    routers = sorted(list(routers))
    min_value = N
    for i in range(1, len(routers)):
        if routers[i] - routers[i-1] < min_value:
            min_value = routers[i] - routers[i-1]
    ans = max(min_value, ans)

print(ans)



# 이진 탐색

import sys
input = sys.stdin.readline

# 집의 개수 N, 공유기 개수 C
N, C = map(int, input().split())
houses = []

for _ in range(N):
    houses.append(int(input().rstrip()))

houses.sort()

routers = []
# 최소 거리
start = 1
# 최대 거리
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    router = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if houses[i] >= (router + mid):
            count += 1
            router = houses[i]

    if count >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)