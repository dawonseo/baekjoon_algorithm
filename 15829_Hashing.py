# 백준 15829번 Hashing

L = int(input())
s = input()
ans = 0

for i in range(L):
    ans += (ord(s[i])-96) * (31**i)

print(ans % 1234567891)
