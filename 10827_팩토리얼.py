# 백준 10827 팩토리얼

# math 사용
import math
print(math.factorial(int(input())))

# 재귀함수 사용
def fac(num):
    if num == 0:
        return 1
    else:
        return num * fac(num-1)

print(fac(int(input())))