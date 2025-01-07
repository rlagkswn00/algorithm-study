# BFS - 14442번 - 벽 부수고 이동하기 2
import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(n):
    line = list(input().strip())
    for j in range(m):
        if line[j] == '1':
            arr[i][j] = 1

# n행 m열 짜리 배열이 k층 있는 3차원 배열
# result[층][행][열]
result = [[[float('inf') for c in range(m)] for r in range(n)] for depth in range(k+1)]
result[0][0][0] = 1
q = deque()
q.append((0, 0, 0))

while q:
    depth, y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < n) and (0 <= nx < m):
            if arr[ny][nx] == 1:        # 벽인 칸
                if depth >= k:
                    continue
                if result[depth+1][ny][nx] > result[depth][y][x] + 1:
                    q.append((depth+1, ny, nx))
                    result[depth + 1][ny][nx] = result[depth][y][x] + 1

            else:       # 이동 가능한 칸
                if result[depth][ny][nx] > result[depth][y][x] + 1:
                    q.append((depth, ny, nx))
                    result[depth][ny][nx] = result[depth][y][x] + 1

ans = float('inf')
for i in range(k, -1, -1):
    ans = min(ans, result[i][n-1][m-1])
if ans == float('inf'):
    print(-1)
else:
    print(ans)

# for depth in range(k+1):
#     for row in range(n):
#         print(result[depth][row])
#     print()
