# 백준 18352 특정 거리의 도시 찾기

import heapq
import sys

input = sys.stdin.readline
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int,input().split())

cost = [sys.maxsize for _ in range(N + 1)]
node = [[] for _ in range(N + 1)]

# node의 n번 인덱스에 (n과 연결된 노드, 비용)을 추가한다.
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append((b, 1))

q = []
# 시작 노드의 최단 경로를 0으로 설정, 큐에 삽입
# (거리, 경로)
heapq.heappush(q, (0, X))
cost[X] = 0
while q:
    dist, now = heapq.heappop(q)
    if cost[now] < dist:
        continue
    for i in node[now]:
        c = dist + i[1]
        if c < cost[i[0]]:
            cost[i[0]] = c
            heapq.heappush(q, (c, i[0]))


if K not in cost:
    print(-1)
    sys.exit()

for i in range(len(cost)):
    if cost[i] == K:
        print(i)
