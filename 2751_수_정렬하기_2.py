# 1. sorted 사용
# pypy3 기준 956ms
import sys
input = sys.stdin.readline

N = int(input())
li = []

for i in range(N):
    li.append(int(input().strip()))

for i in sorted(li):
    print(i)

# 2. merge sort 사용
# pypy3 기준 1348ms
import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(left_arr) and h < len(right_arr):
        if left_arr[l] < right_arr[h]:
            merged_arr.append(left_arr[l])
            l += 1
        else:
            merged_arr.append(right_arr[h])
            h += 1
    merged_arr += left_arr[l:]
    merged_arr += right_arr[h:]
    return merged_arr


N = int(input())
li = []

for i in range(N):
    li.append(int(input().strip()))

for i in merge_sort(li):
    print(i)


# 3. sys.stdin.readline() 사용하지 않고 input() 사용
# pypy3 기준 1176ms
N = int(input())
li = []

for i in range(N):
    li.append(int(input().strip()))

for i in sorted(li):
    print(i)
