import heapq
import sys
input = sys.stdin.readline

N = int(input())

left_queue = []
right_queue = []
cnt = 0

for _ in range(N):
    num = int(input())
    if len(left_queue) == len(right_queue):
        heapq.heappush(left_queue, -num)
    else:
        heapq.heappush(right_queue, num)

    if len(right_queue) and -(left_queue[0]) > right_queue[0]:
        right_value = -heapq.heappop(right_queue)
        left_value = -heapq.heappop(left_queue)

        heapq.heappush(right_queue, left_value)
        heapq.heappush(left_queue, right_value)

    print(-left_queue[0])