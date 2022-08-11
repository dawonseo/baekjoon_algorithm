# 백준 18353번 병사 배치하기

N = int(input())
li = list(map(int,input().split()))
li.reverse()

dp = [1] * N

# LIS 알고리즘 수행
for i in range(1, N):
    for j in range(0, i):
        if li[j] < li[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))