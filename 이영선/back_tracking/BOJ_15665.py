# 백트래킹 - 15665번 - N과 M (11)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans_set = set()

def bt(result):
    global m, n
    if len(result) == m:
        ans_set.add(tuple(result))
        return
    for i in range(n):
        result.append(arr[i])
        bt(result)
        result.pop(-1)

bt([])

ans = list(ans_set)
ans.sort()
for i in ans:
    print(' '.join(map(str, i)))
