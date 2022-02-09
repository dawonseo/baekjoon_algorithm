# 백준 2606 바이러스

import sys
input = sys.stdin.readline


N1 = int(input())
N2 = int(input())
node_list = [[] for _ in range(N1)]

for _ in range(N2):
    a, b = map(int, input().split())
    node_list[a - 1].append(b)
    node_list[b - 1].append(a)

queue = [1]
bfs_list = []

while len(queue):
    now = queue.pop(0)
    if now not in bfs_list:
        queue += node_list[now - 1]
        bfs_list.append(now)

print(len(bfs_list)-1)