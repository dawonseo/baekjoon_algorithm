# 백준 1010 다리 놓기
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    dp = [ [0] * M for _ in range(N) ]
    dp[0] = [i for i in range(1, M + 1)]

    if N >= 2:
        for i in range(1, M):
            dp[1][i] = dp[1][i-1] + i

    for i in range(2, N):
        for j in range(i, M):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

    print(dp[N-1][M-1])