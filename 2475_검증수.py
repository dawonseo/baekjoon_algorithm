n = list(map(int, input().split()))
ans = 0
for i in n:
    ans += i ** 2
    ans %= 10

print(ans)