import itertools

L, C = map(int, input().split())
a_list = list(map(str, input().split()))
# 자음
consonants = []
# 모음
vowels = []

for i in a_list:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(i)
    else:
        consonants.append(i)

v_count = 1
c_count = L - v_count
words = []

while c_count >= 2:
    for i in itertools.combinations(consonants, c_count):
        for j in itertools.combinations(vowels, v_count):
            words.append(sorted(i+j))
    v_count += 1
    c_count = L - v_count

words.sort()
for w in words:
    print(''.join(w))