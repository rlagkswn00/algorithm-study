"""
visited 배열 순서에 따라 정답/틀림이 갈림 (?)
visited[wall_count][y][x] : 틀림
visited[y][x][wall_count] : 정답
"""

from collections import deque
import sys

N, M, K = map(int, input().split())
graph = list()
for _ in range(N):
    graph.append(list(input()))

q = deque()
q.append((0, 0, K, 1))
visited = [[[False for _ in range(K+1)] for _ in range(M)] for _ in range(N)]  # 벽을 부순상태까지 저장
answer = -1
while q:
    y, x, break_count, count = q.popleft()
    if y == N-1 and x == M-1:
        answer = count
        break
    for dy, dx in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
        py = y + dy
        px = x + dx
        if py < 0 or px < 0 or py >= N or px >= M:
            continue
        if graph[py][px] == '0' and not visited[py][px][break_count]:
            q.append((py, px, break_count, count+1))
            visited[py][px][break_count] = True
        else:
            if break_count != 0 and not visited[py][px][break_count-1]:
                q.append((py, px, break_count-1, count+1))
                visited[py][px][break_count-1] = True

print(answer)