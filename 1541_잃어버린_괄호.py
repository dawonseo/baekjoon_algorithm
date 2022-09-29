# 백준 1541 잃어버린 괄호

num_list = list(input().split('-'))

if '+' in num_list[0]:
    tmp_list = num_list[0].split('+')
    tmp = 0
    for t in tmp_list:
        tmp += int(t.lstrip('0'))
    ans = tmp
else:
    ans = int(num_list[0].lstrip('0'))

for i in range(1, len(num_list)):
    if '+' in num_list[i]:
        tmp_list = num_list[i].split('+')
        tmp = 0
        for t in tmp_list:
            tmp += int(t.lstrip('0'))
        ans -= tmp
    else:
        ans -= int(num_list[i].lstrip('0'))

print(ans)