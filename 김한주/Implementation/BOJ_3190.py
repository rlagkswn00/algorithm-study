import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())
apples = [list(map(int,input().split())) for _ in range(k)]
l = int(input())
ops = {}
board = [[0] * n for _ in range(n)]

for apple in apples:
    x,y = apple
    board[x-1][y-1] = 1

for _ in range(l):
    time, d = input().split()
    time = int(time)
    ops[time] = d

dList = [(0,1),(1,0),(0,-1),(-1,0)]
dIndex = 0

q = deque()
q.append((0,0))
headX, headY = 0,0
board[0][0] = 2
time = 1

while True:
    nx, ny = headX + dList[dIndex][0], headY + dList[dIndex][1]

    if nx < 0 or nx >= n or ny < 0 or ny >=n: # 벽인경우
        break
    if board[nx][ny] == 2: # 몸인경우
        break
    
    if board[nx][ny] != 1: #사과가 아닌경우 꼬리를 자르기
        a,b = q.popleft()
        board[a][b] = 0 # 뱀 몸이없음.
        
    headX, headY = nx,ny
    board[headX][headY] = 2
    q.append((nx,ny))

    if time in ops.keys():
        if ops[time] == "D":  # 오른쪽 회전
            dIndex = (dIndex + 1) % 4
        elif ops[time] == "L":  # 왼쪽 회전
            dIndex = (dIndex - 1) % 4
    time += 1

print(time)