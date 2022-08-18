
def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value

    if i == N:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, arr + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, arr - nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, arr * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(arr / nums[i]))
            div += 1


# 수의 개수 N 입력 받기
N = int(input())
# 수열 입력 받기
nums = list(map(int, input().split()))
# 차례대로 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

dfs(1, nums[0])

print(max_value)
print(min_value)