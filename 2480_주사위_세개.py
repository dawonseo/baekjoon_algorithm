a, b, c = map(int, input().split())

l = [a, b, c]
s = {a, b, c}

if len(s) == 1:
    print(10000 + l[0] * 1000)
elif len(s) == 2:
    for i in l:
        if l.count(i) == 2:
            print(1000 + i * 100)
            exit()
else:
    print(max(l) * 100)