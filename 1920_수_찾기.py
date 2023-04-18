import sys
input = sys.stdin.readline

N = int(input())
n_arr = sorted(list(map(int, input().split())))
M = int(input())
m_arr = list(map(int, input().split()))


def binary_search(arr, n, start, end):
    if start > end:
        return 0

    m = (start + end) // 2

    if arr[m] == n:
        return 1
    elif arr[m] > n:
        return binary_search(arr, n, start, m - 1)
    else:
        return binary_search(arr, n, m + 1, end)


for num in m_arr:
    print(binary_search(n_arr, num, 0, N - 1))