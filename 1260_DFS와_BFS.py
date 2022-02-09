# 백준 1260 DFS와 BFS

import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())  # 정점의 개수 N, 간선의 개수 M, 시작점 V
my_list = [[] for _ in range(N)]     # 정점 개수만큼의 list를 값으로 가지는 2차원 배열 생성

for _ in range(M):                   # 간선을 입력받아 2차원 배열에 저장
    a, b = map(int, input().split()) # 각 list들은 index+1 정점과 연결된 정점을 포함
    my_list[a-1].append(b)           # ex) 0번지에 저장된 list는 1번 정점과 연결된 정점을 포함
    my_list[b-1].append(a)

stack = [V]                          # stack, queue를 구현할 list 생성 후 시작 정점 V를 저장
queue = [V]
dfs_list = []
bfs_list = []

while len(queue):                   # queue 사용하여 bfs 구현
    now = queue.pop(0)
    if now not in bfs_list:
        queue += sorted(my_list[now - 1])
        bfs_list.append(now)
    if len(bfs_list) == N:
        break


while len(stack):                   # stack 사용하여 dfs 구현
    now = stack.pop()
    if now not in dfs_list:
        stack += sorted(my_list[now - 1], reverse=True)
        dfs_list.append(now)
    if len(dfs_list) == N:
        break

print(' '.join(map(str, dfs_list)))
print(' '.join(map(str,bfs_list)))

