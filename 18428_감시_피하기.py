import sys
input = sys.stdin.readline


# 장애물을 세울 수 있는 모든 경우의 수를 탐색하는 함수
# 장애물을 3개 세웠을 경우 감시 함수 실행
# --> 학생 발각되지 않으면 True 리턴
def obstacle(cnt):
    global flag

    if cnt == 3:
        if watch():
            flag = True
            return
    else:
        for x in range(N):
            for y in range(N):
                if graph[x][y] == 'X':
                    graph[x][y] = 'O'
                    obstacle(cnt + 1)
                    graph[x][y] = 'X'


def watch():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in t: # 선생님의 위치에서
        for k in range(4): # 상/하/좌/우 탐색
            nx, ny = i

            while 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == "O":
                    break

                # 학생이 보이면 실패
                if graph[nx][ny] == "S":
                    return False

                nx += dx[k]
                ny += dy[k]

    # 모두 통과하면 학생이 안보이는 것으로 성공
    return True


N = int(input())
graph = []
t = []
flag = False

for _ in range(N):
    graph.append(list(map(str, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            t.append([i, j])

obstacle(0)

if flag:
    print("YES")
else:
    print("NO")