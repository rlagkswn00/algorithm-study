# 백트래킹 - 15664번 - N과 M (10)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans_set = set()

def bt(result, last):
    global m, n
    if len(result) == m:
        ans_set.add(tuple(result))
        return
    for i in range(last + 1, n):
        if len(result) == 0 or result[-1] <= arr[i]:
            result.append(arr[i])
            bt(result, i)
            result.pop(-1)
bt([], -1)

ans = list(ans_set)
ans.sort()
for i in ans:
    print(' '.join(map(str, i)))