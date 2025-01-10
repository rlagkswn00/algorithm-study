# BFS - 7562번 - 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline

dy = [-2, -2, -1, -1, 1, 1, 2, 2]
dx = [-1, 1, -2, 2, -2, 2, -1, 1]

t = int(input())
for _ in range(t):
    n = int(input())
    y, x = map(int, input().split())
    t_y, t_x = map(int, input().split())

    arr = [[float('inf')] * n for _ in range(n)]
    arr[y][x] = 0
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < n) and (0 <= nx < n):
                if arr[ny][nx] > arr[y][x] + 1:
                    arr[ny][nx] = arr[y][x] + 1
                    q.append((ny, nx))
    print(arr[t_y][t_x])
