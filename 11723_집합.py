import sys
input = sys.stdin.readline
S = 0

M = int(input())

for _ in range(M):
    ip = input().split()
    if len(ip) == 1:
        if ip[0] == "all":
            S = (1 << 21) - 1
        elif ip[0] == "empty":
            S = 0
    else:
        a, b = ip
        b = int(b)

        if a == "add":
            S = S | (1 << b)
        elif a == "check":
            print(1 if S & (1 << b) != 0 else 0)
        elif a == "remove":
            S = S & ~(1 << b)
        elif a == "toggle":
            S = S ^ (1 << b)