N = int(input())
cnt = 0
row = [-1] * N


def is_promising(x):
    for i in range(x):
        if abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def solve(x, v):
    global cnt
    if x == N:
        cnt += 1
        return
    else:
        for i in range(N):
            if v[i]:
                continue
            row[x] = i
            if is_promising(x):
                v[i] = True
                solve(x+1, v)
                v[i] = False


solve(0, [False for _ in range(N)])

print(cnt)
