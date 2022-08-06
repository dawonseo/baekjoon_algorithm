# lambda key 사용
import sys
input = sys.stdin.readline

N = int(input())
stu_li = []

for _ in range(N):
    stu_li.append(list(map(str, input().split())))

# 0: 이름, 1: 국어, 2: 영어, 3: 수학
sorted_stu_li = sorted(stu_li, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in sorted_stu_li:
    print(i[0])


# sort 자체 우선순위 사용
import sys
input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    name, a, b, c = input().split()
    li.append((-int(a), int(b), -int(c), name))

li.sort()
for s in li: print(s[3])