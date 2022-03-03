# 백준 10829 이진수 변환


# 재귀함수 사용하지 않음
N = int(input())
print(bin(N)[2:])


# 재귀함수 사용
def to_bin(num):
    if num == 0:
        return ''
    elif num == 1:
        return '1'
    return to_bin(num//2) + str(num%2)

N = int(input())
print(to_bin(N))
