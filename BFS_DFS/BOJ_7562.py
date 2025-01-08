import sys
from collections import deque

def bfs(start, dest, graph):
    dirs = [[1, -2], [-1, -2], [2, -1], [-2, -1], [1, 2], [-1, 2], [2, 1], [-2, 1]]
    q = deque()
    count = 0
    graph[start[0]][start[1]] = True
    q.append((start[0], start[1], count))
    while q:
        cy, cx, count = q.popleft()
        if cy == dest[0] and cx == dest[1]:
            return count
        for dir in dirs:
            dy = cy + dir[0]
            dx = cx + dir[1]
            if dy < 0 or dx < 0 or dy >= len(graph) or dx >= len(graph):
                continue
            if graph[dy][dx]:
                continue
            q.append((dy, dx, count+1))
            graph[dy][dx] = True

tc = int(input())
for _ in range(tc):
    lines = int(input())
    start = tuple(map(int, input().split()))
    destination = tuple(map(int, input().split()))
    graph = [[False for _ in range(lines)] for _ in range(lines)]   # 그래프 겸 visited 역할 동시에 수행
    print(bfs(start, destination, graph))