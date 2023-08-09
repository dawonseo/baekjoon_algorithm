import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline


def rolling(graph, x, y, xx, yy, direction):
    m = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    dx, dy = m[direction]
    flag = False

    while True:
        x += dx
        y += dy
        if graph[x][y] == '#':
            if flag:
                return False, x - (2 * dx), y - (2 * dy)
            else:
                return False, x - dx, y - dy
        elif graph[x][y] == 'O':
            return True, x, y
        elif (x, y) == (xx, yy):
            flag = True


N, M = map(int, input().split())
graph = []
visited = defaultdict(bool)
rx, ry, bx, by = 0, 0, 0, 0

for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
            graph[i][j] = '.'
        elif graph[i][j] == 'B':
            bx, by = i, j
            graph[i][j] = '.'

q = [(1, rx, ry, bx, by)]
heapq.heapify(q)
visited[(rx, ry, bx, by)] = True

while q:
    cnt, rx, ry, bx, by = heapq.heappop(q)

    if cnt > 10:
        print(-1)
        exit()

    for i in range(4):
        rtf, nrx, nry = rolling(graph, rx, ry, bx, by, i)
        btf, nbx, nby = rolling(graph, bx, by, rx, ry, i)
        if visited[(nrx, nry, nbx, nby)]:
            continue
        if btf:
            continue
        elif rtf:
            print(cnt)
            exit()
        else:
            heapq.heappush(q, (cnt + 1, nrx, nry, nbx, nby))
            visited[(nrx, nry, nbx, nby)] = True


print(-1)
