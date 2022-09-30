import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []
N = int(input())

for _ in range(N):
    this = input().rstrip()
    if this == 'L':
        if len(left) == 0:
            continue
        right.append(left.pop())
    elif this == 'D':
        if len(right) == 0:
            continue
        left.append(right.pop())
    elif this == 'B':
        if len(left) == 0:
            continue
        left.pop()
    else:
        left.append(this[-1])

print(''.join(left) + ''.join(reversed(right)))