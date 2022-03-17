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

dp_arr.append(li[0]) # 계단의 갯수가 1개일 경우: 꼭 하나를 밟아야 함
dp_arr.append(li[0]+li[1]) # 계단의 갯수가 2개일 경우: 둘 다 밟는 것이 max
dp_arr.append(max(li[0]+li[2], li[1] + li[2])) # 계단의 갯수가 3개일 경우: 1,3번째 밟는 것과 2,3번째를 밟는 것 중 더 큰 것

for i in range(3, len(li)):
    # 계단의 갯수가 4개 이상일 때: 마지막 계단의 직전 계단을 밟았을 때와 밟지 않았을 때 중 큰 값
    # dp_arr에 저장된 해당 갯수까지의 최댓값을 활용한다
    dp_arr.append(max(dp_arr[i-2] + li[i], dp_arr[i-3] + li[i] + li[i - 1]))   
