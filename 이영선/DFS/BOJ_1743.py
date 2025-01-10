# dfs - 1743번 - 음식물 피하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

n, m, k = map(int, input().split())
arr = [[0] * (m+1) for _ in range(n+1)]
q = []
for i in range(k):
    r, c = map(int, input().split())
    arr[r][c] = 1
    q.append((r, c))

cnt = 0

def dfs(r, c):
    global n, m, cnt
    if arr[r][c] == 0:
        return
    arr[r][c] = 0
    cnt += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (0 < nr <= n) and (0 < nc <= m) and arr[nr][nc] == 1:
            dfs(nr, nc)


ans = 0
for (r, c) in q:
    cnt = 0
    dfs(r, c)
    ans = max(ans, cnt)
print(ans)