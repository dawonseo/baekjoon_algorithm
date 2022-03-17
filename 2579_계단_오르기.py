# 백준 2579번 계단 오르기

import sys

li = []
dp_arr = []

for _ in range(int(input())):
    li.append(int(sys.stdin.readline()))

if len(li) == 1:
    print(li[0])
    sys.exit()
elif len(li) == 2:
    print(li[0] + li[1])
    sys.exit()

dp_arr.append(li[0])
dp_arr.append(li[0]+li[1])
dp_arr.append(max(li[0]+li[2], li[1] + li[2]))

for i in range(3, len(li)):
    dp_arr.append(max(dp_arr[i-2] + li[i], dp_arr[i-3] + li[i] + li[i - 1]))