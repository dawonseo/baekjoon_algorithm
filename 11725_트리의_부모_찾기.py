import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
e = [[] for _ in range(N+1)]
ans_li = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    e[a].append(b)
    e[b].append(a)

queue = deque([1])
visited[1] = True

while queue:
    x = queue.popleft()

    for i in e[x]:
        if not visited[i]:
            ans_li[i] = x
            visited[i] = True
            queue.append(i)

for i in range(2, N+1):
    print(ans_li[i])
