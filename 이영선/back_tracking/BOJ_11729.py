# 재귀 - 11729번 - 하노이 탑 이동 순서
import sys
input = sys.stdin.readline
n = int(input())
ans = 0
ans_str = []

def hanoi(k, start, end):
    global ans, ans_str
    if k == 1:
        ans_str.append(str(start) + ' ' + str(end))
        ans += 1
        return
    mid = 6 - (start + end)
    hanoi(k - 1, start, mid)
    hanoi(1, start, end)
    hanoi(k - 1, mid, end)

hanoi(n, 1, 3)
print(ans)
print('\n'.join(ans_str))
