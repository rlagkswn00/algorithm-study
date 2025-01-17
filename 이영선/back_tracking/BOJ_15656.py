# 백트래킹 - 15656번 - N과 M (7)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

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