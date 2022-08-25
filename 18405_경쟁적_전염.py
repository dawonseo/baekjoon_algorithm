from collections import deque
import sys
input = sys.stdin.readline


def bfs(S, X, Y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque(virus_pos)
    count = 0

    while q:
        if count == S:
            break
        for _ in range(len(q)):
            prev, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if examiner_map[nx][ny] == 0:
                        examiner_map[nx][ny] = examiner_map[x][y]
                        q. append((examiner_map[nx][ny], nx, ny))
        count += 1
    return examiner_map[X-1][Y-1]


N, K = map(int, input().split())
examiner_map = []
virus_pos = []

for i in range(N):
    examiner_map.append(list(map(int, input().split())))
    for j in range(N):
        if examiner_map[i][j] != 0:
            virus_pos.append((examiner_map[i][j], i, j))

S, X, Y = map(int, input().split())

virus_pos.sort()
print(bfs(S, X, Y))