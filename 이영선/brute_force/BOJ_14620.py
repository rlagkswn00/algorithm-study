# 브루트 포스 - 14620번 - 꽃길
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
ans = float('inf')

def check(flowers):
    global ans, n
    visited = [[False] * n for _ in range(n)]
    total = 0
    for x, y in flowers:
        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if not visited[ny][nx]:
                total += arr[nx][ny]
                visited[ny][nx] = True
            else:
                return
    ans = min(ans, total)

result = []
for i in range(1, n - 1):
    for j in range(1, n - 1):
        result.append((i, j))
for i in combinations(result, 3):
    check(i)

print(ans)
