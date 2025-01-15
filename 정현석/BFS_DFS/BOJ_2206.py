from collections import deque
import sys

N, M = map(int, input().split())
graph = list()
for _ in range(N):
    graph.append(list(input()))

q = deque()
q.append((0, 0, True, 1))
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]  # 벽을 부순상태까지 저장
answer = -1
while q:
    y, x, can_break, count = q.popleft()
    if y == N-1 and x == M-1:
        answer = count
        break
    for dy, dx in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
        py = y + dy
        px = x + dx
        if py < 0 or px < 0 or py >= N or px >= M:
            continue
        if graph[py][px] == '0':
            if can_break:
                if not visited[0][py][px]:
                    q.append((py, px, can_break, count+1))
                    visited[0][py][px] = True
            else:
                if not visited[1][py][px]:
                    q.append((py, px, can_break, count+1))
                    visited[1][py][px] = True
        else:
            if not can_break:
                continue
            q.append((py, px, False, count+1))
            visited[1][py][px] = True

print(answer)