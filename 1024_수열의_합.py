N, L = map(int, input().split())

for i in range(L, 101):
    tmp = (N / i) - ((i - 1) / 2)
    if tmp >= 0 and tmp % 1 == 0:
        tmp = int(tmp)
        for j in range(i):
            print(tmp, end=' ')
            tmp += 1
        exit()

print(-1)
