# 백준 2798 블랙잭

def black_jack(N, M, arr):
    result = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if (arr[i] + arr[j] + arr[k]) <= M:
                    result = max(result, arr[i] + arr[j] + arr[k])
    return result


N, M = map(int, input().split())
card_list = list(map(int, input().split()))

print(black_jack(N, M, card_list))