# 에라토스테네스의 체 이용
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(2 * i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i]]


M, N = map(int,input().split())
p_list = prime_list(N+1)
for i in range(len(p_list)):
    if p_list[i] >= M:
        for i in p_list[i:]: print(i)
        break
