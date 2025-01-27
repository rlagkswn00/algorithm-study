import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

chz = deque()
chzList = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            chzList.append((i,j))

#치즈가 없을떄 까지 뤂 돈다.
#1. 치즈의 두면 이상이 막혀있는지 확인
    # 2면 이하로 막혀있으면 녹음.
    # 3면 이상 막혀있으면 녹지 않음
#탐색은 시작점 기준 4방향에 대해서 bfs를 해서 벽에 닿는 점이 두개가 넘으면 그건 녹음.
#그 외에는 안녹음.

dList = [(1,0),(0,1),(-1,0),(0,-1)]
visited = []

#공기가 통하는 면의 개수를 센다.
def bfs(x,y):
    count = 0
    for d in dList:
        a,b = x + d[0], y + d[1]
        if a < 0 or a >=n or b < 0 or b >m: # 이미 벽이면 더 갈 필요없고 공기 통하니 + 1
            count += 1
            continue
        if board[a][b] == 1:
            continue
        q = deque()
        q.append((a,b))
        visited = [[False] * m for _ in range(n)]
        visited[a][b] = True
            
        while q:
            cx,cy = q.popleft()
            
            for d in dList:
                nx, ny = cx + d[0], cy + d[1]
                if nx < 0 or nx >=n or ny < 0 or ny >=m: # 벽에 닿음, 공기통함
                    count += 1
                    q = deque()
                    break
                if board[nx][ny] == 1: # 치즈를 만났으면 더 갈수없음.
                    continue
                if visited[nx][ny]:
                    continue
                
                visited[nx][ny] = True
                q.append((nx,ny))
                
    return count

time = 0
while chzList:
    deleteQ = deque()
    chz = deque(chzList)
    while chz:
        cx,cy = chz.popleft()
        count = bfs(cx,cy)
        if time == 10:
            exit(0)
        if count >= 2: #녹음
            deleteQ.append((cx,cy))
    
    for d in deleteQ:
        if d in chzList:
            chzList.remove(d)
            board[d[0]][d[1]] = 0
    time +=1

print(time)