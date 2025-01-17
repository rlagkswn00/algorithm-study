# 백트래킹 - 15651번 - N과 M (3)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

def bt(result):
    global m
    if len(result) == m:
        print(' '.join(map(str,result)))
        return
    for i in arr:
        result.append(i)
        bt(result)
        result.pop(-1)
bt([])