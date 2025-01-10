import sys
input = sys.stdin.readline
from collections import deque

m,n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
q = deque()
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i,j))
            visited[i][j] = True

dList = [(-1,0),(1,0),(0,1),(0,-1)]

while q:
    x,y = q.popleft()
    for d in dList:
        nx,ny = x+d[0], y+d[1]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if board[nx][ny] == -1:
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        board[nx][ny] = board[x][y] + 1
        q.append((nx,ny))

result = 0
for row in board:
    if 0 in row:
        print(-1)
        exit(0)
    result = max(result, max(row))
print(result-1)