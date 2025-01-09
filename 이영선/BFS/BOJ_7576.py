# BFS - 7576번 - 토마토
import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

c, r = map(int, input().split())
result = [[float('inf')] * c for _ in range(r)]
arr = []
q = deque()
for i in range(r):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(c):
        if line[j] == -1:
            result[i][j] = -1
        if line[j] == 1:
            result[i][j] = 0
            q.append((i, j))

while q:
    # print('(', y, ',', x, ')')
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < r) and (0 <= nx < c):
            if arr[ny][nx] == -1:
                continue
            if result[ny][nx] > result[y][x] + 1:
                result[ny][nx] = result[y][x] + 1
                q.append((ny, nx))

ans = 0
for i in range(r):
    ans = max(ans, max(result[i]))
if ans == float('inf'):
    print(-1)
else:
    print(ans)