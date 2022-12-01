N, K = map(int, input().split())
d = []
DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    d.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < d[i-1][0]:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(d[i-1][1] + DP[i-1][j-d[i-1][0]], DP[i-1][j])

print(DP[-1][-1])
