import sys
from collections import deque

# 하루 경과 구현 (인접한 토마토 숙성시키고 해당 토마토 리스트 반환)
def day_one(graph, q):
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    new_q = deque()
    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            py = y + dy
            px = x + dx
            if py < 0 or px < 0 or py >= len(graph) or px >= len(graph[0]):
                continue
            if graph[py][px] != 0:
                continue
            graph[py][px] = 1
            new_q.append((py, px))
    return new_q

def check(graph):
    for g in graph:
        for tomato in g:
            if tomato == 0:
                return False
    return True

M, N = map(int, input().split())
graph = list()
q = deque()
for y in range(N):
    temp = list(map(int, input().split()))
    for x, tomato in enumerate(temp):
        if tomato == 1:
            q.append((y, x))
    graph.append(temp)

answer = 0
while True:
    q = day_one(graph, q.copy())
    # 더이상 익을수 있는 토마토가 없으면 종료
    # 토마토가 하나라도 익었으면 day + 1
    if len(q) == 0:
        break
    else:
        answer += 1

if not check(graph):
    print(-1)
else:
    print(answer)