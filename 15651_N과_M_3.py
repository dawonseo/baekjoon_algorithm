N, M = map(int, input().split())


def solve(arr):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
    else:
        for i in range(1, N+1):
            solve(arr + [i])


solve([])
