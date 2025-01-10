# BFS - 2206번 - 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c = map(int, input().split())
arr = [[0] * c for _ in range(r)]

for i in range(r):
    line = list(input())
    for j in range(c):
        if line[j] == '1':
            arr[i][j] = 1

ans = float('inf')
result = [[[float('inf')] * c for _ in range(r)] for _ in range(2)]

q = deque()
q.append((0, 0, 0))
result[0][0][0] = 1        # DFS 탐색 시작 지점 초기화!!!! (모든 배열을 INF로 초기화, 시작 지점만 0/1로 초기화)
while q:
    depth, y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < r) and (0 <= nx < c):
            if arr[ny][nx] == 1:
                if depth == 1:
                    continue
                else:
                    result[depth+1][ny][nx] = result[depth][y][x] + 1
                    q.append((depth+1, ny, nx))
            if arr[ny][nx] == 0:
                if result[depth][ny][nx] > result[depth][y][x] + 1:
                    result[depth][ny][nx] = result[depth][y][x] + 1
                    q.append((depth, ny, nx))
ans = min(result[0][r-1][c-1], result[1][r - 1][c - 1])

if ans == float('inf'):
    print(-1)
else:
    print(ans)
