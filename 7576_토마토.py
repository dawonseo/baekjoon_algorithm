import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
r_list = [[False for _ in range(M)]for _ in range(N)]
ttidx = []
tomato = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for x in range(N):
    this = list(map(int, input().split()))

    for y in range(M):
        if this[y] != 0:
            if this[y] == 1:
                ttidx.append((x, y, 0))
            r_list[x][y] = True
    tomato.append(this)

queue = deque(ttidx)

while queue:
    x, y, day = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M or r_list[nx][ny]:
            continue
        else:
            r_list[nx][ny] = True
            queue.append((nx, ny, day+1))

for i in r_list:
    if False in i:
        print(-1)
        exit()

print(day)