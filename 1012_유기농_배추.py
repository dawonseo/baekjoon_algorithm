from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
cab_list = []
ans = 0


def bfs(x, y, cab_list):
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                continue
            else:
                if (nx, ny) in cab_list:
                    queue.append((nx, ny))
                    cab_list.remove((nx, ny))


for _ in range(N):
    ans = 0
    M, N, K = map(int, input().split())

    for _ in range(K):
        cab_list.append(tuple(map(int, input().split())))

    while cab_list:
        ans += 1
        x, y = cab_list.pop()
        bfs(x, y, cab_list)

    print(ans)