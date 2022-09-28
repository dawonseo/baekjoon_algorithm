# 백준 1182 부분 수열의 합 (백트래킹)

def back_tracking(idx, r):
    global ans

    if idx >= len(num_list):
        return

    r += num_list[idx]

    if r == S:
        ans += 1

    back_tracking(idx+1, r)
    back_tracking(idx+1, r - num_list[idx])


N, S = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0

back_tracking(0, 0)

print(ans)