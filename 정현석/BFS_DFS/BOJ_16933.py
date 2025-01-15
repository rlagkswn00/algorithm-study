"""
똑왜틀 ;;
https://kjimin0619.tistory.com/88
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
visited[0][0][K] = True
while q:
    # count 가 홀수인 경우 (낮)에만 벽을 부술 수 있음.
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
        elif graph[py][px] == '1' and break_count != 0 and not visited[py][px][break_count-1]:
            # 밤인 경우 하루 기다렸다가 벽뿌
            if (count & 1) == 0:
                q.append((y, x, break_count, count+1))
            else:
                q.append((py, px, break_count-1, count+1))
                visited[py][px][break_count-1] = True

print(answer)