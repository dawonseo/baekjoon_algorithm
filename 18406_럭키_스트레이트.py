N = input()

l = 0
r = 0

for i in N[:len(N)//2]:
    l += int(i)
for i in N[len(N)//2:]:
    r += int(i)

print("LUCKY" if l == r else "READY")