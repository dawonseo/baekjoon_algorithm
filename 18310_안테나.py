# 개선 전 (median 사용)
import statistics

N = int(input())
house_list = list(map(int, input().split()))
house_tuple = []

median = statistics.median(house_list)

for i in house_list:
    house_tuple.append((i, abs(i - median)))

print(sorted(house_tuple, key = lambda x: (x[1], x[0]))[0][0])


# 개선 후
N = int(input())
house_list = list(map(int, input().split()))
house_list.sort()
print(house_list[(N-1)//2])