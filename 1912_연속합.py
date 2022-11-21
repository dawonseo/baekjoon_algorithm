n = int(input())
num_li = list(map(int, input().split()))

DP = [0 for _ in range(n+1)]
DP[0] = -1001

for idx, num in enumerate(num_li):
    DP[idx+1] = max(DP[idx] + num, num)

print(max(DP))
