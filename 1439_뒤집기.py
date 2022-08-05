S = input()
f = S[0]
answer = 0

for i in range(1, len(S)):
    if S[i] != f and S[i-1] == f:
        answer += 1

print(answer)