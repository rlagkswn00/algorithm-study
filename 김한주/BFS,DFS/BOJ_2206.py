import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,list(input().strip()))) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = True

dList = [(-1,0),(1,0),(0,-1),(0,1)]

q = deque()
q.append((0,0,0))
result = 0
while q:
    a,b,c = q.popleft()
    
    if a ==  n - 1 and b == m - 1:
        result = visited[a][b][c]
        break
    for d in dList:
        nx = a + d[0]
        ny = b + d[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1 and c == 0:
            visited[nx][ny][1] = visited[a][b][0] + 1
            q.append((nx,ny,1))
            continue
        if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
            visited[nx][ny][c] = visited[a][b][c] + 1
            q.append((nx,ny,c))

print(result)