import sys
input = sys.stdin.readline

N = int(input())
sg_cards = sorted(list(map(int, input().split())))

M = int(input())
ad_nums = list(map(int, input().split()))

ans_dict = {}
ans = []

def binary_search(card_li, n, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if card_li[m] == n:
        return card_li[start:end+1].count(n)
    elif card_li[m] > n:
        return binary_search(card_li, n, start, m - 1)
    else:
        return binary_search(card_li, n, m + 1, end)

for num in ad_nums:
    if num not in ans_dict.keys():
        ans_dict[num] = str(binary_search(sg_cards, num, 0, N - 1))
    ans.append(ans_dict[num])

print(' '.join(ans))
