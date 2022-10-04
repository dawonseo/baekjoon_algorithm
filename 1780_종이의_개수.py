# 백준 1780 종이의 개수
import sys
input = sys.stdin.readline

N = int(input())
paper_map = []
ans_dict = {-1: 0, 0: 0, 1: 0}


def check(row_idx, col_idx, d):
    # 첫 숫자 추출
    tmp = paper_map[row_idx][col_idx]
    for i in range(row_idx, row_idx + d):
        for j in range(col_idx, col_idx + d):
            # 같지 않음
            if paper_map[i][j] != tmp:
                t = d//3
                for x in range(3):
                    for y in range(3):
                        check(row_idx+x*t, col_idx+y*t, t)
                return
    # 모두 같은 수로 이루어져 있음
    ans_dict[tmp] += 1
    return


for _ in range(N):
    paper_map.append(list(map(int, input().split())))


check(0, 0, N)

for i in ans_dict.values():
    print(i)