"""
visited 배열 순서에 따라 정답/틀림이 갈림 (?)
visited[wall_count][y][x] : 틀림
visited[y][x][wall_count] : 정답
관련 게시글 : https://www.acmicpc.net/board/view/111938
근데 위 게시글에서 주장하는건 반대인것 같은데 ... ?

캐시 적중률..? 전자의 경우 wall count기준으로 먼저 접근하기 때문에 캐시 적중률이 떨어지고
후자의 경우 위치기반으로 먼저 접근하게 되기 때문에 그래프 탐색 특성상 비슷한 위치의 값이 자주나올거고 캐시적중률이 올라가서..?
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