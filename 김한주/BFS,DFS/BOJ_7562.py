import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
dList = [(-2,1),(-1,2),(1,2),(2,1),
         (2,-1),(1,-2),(-1,-2),(-2,-1)]
for k in range(t):
    i = int(input())
    cx,cy = map(int,input().split())
    destx, desty = map(int,input().split())
    visited = [[False] * i for _ in range(i)]
    board = [[0] * i for _ in range(i)]
    
    q = deque()
    q.append((cx,cy))
    visited[cx][cy] = True
    if cx == destx and cy == desty:
        q.clear()
    isFind = False
    while q:
        x,y = q.popleft()
        
        for d in dList:
            nx,ny = x + d[0], y + d[1]
            if nx >= i or nx < 0 or ny >= i or ny < 0:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            board[nx][ny] = board[x][y] + 1
            if nx == destx and ny == desty:
                isFind = True
                break
            q.append((nx,ny))
            
        if isFind:
            break

    print(board[destx][desty])