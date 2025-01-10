# BFS - 16933번 - 벽 부수고 이동하기 3
## 최단경로 + 벽 부수는 횟수 + 낮밤까지 카운트 해야함
## (0, 0)에서 밤 -> 한칸 이동하면 낮 (이 때에는 벽 부수고 그 자리로 이동 가능)
### 최단 경로의 횟수가 홀수이면 벽을 부술 수 있다는 점을 이용하면 14442번 문제에서 변수를 추가하지 않고도 풀 수 있다!

import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]

for i in range(n):
    line = list(input().strip())
    for j in range(m):
        if line[j] == '1':
            arr[i][j] = 1

result = [[[float('inf') for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
result[0][0][0] = 1
q = deque()
q.append((0, 0, 0))

while q:
    depth, y, x = q.popleft()
    # if result[y][x][depth]가 홀수이면 다음 벽을 깰 수가 있다.
    # 짝수이면 못깸 -> 그럼 자리에서 기다리기
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < n) and (0 <= nx < m):
            if arr[ny][nx] == 1 and depth < k:  # 벽을 만났을 때, 제자리에 있는게 좋을까? 아니면 왔던 길이라도 돌아가는게 좋을까?
                if result[depth][y][x] % 2 == 1:
                    if result[depth + 1][ny][nx] > result[depth][y][x] + 1:
                        result[depth + 1][ny][nx] = result[depth][y][x] + 1
                        q.append((depth + 1, ny, nx))
                else:  # 벽을 못 부수는 상황
                    if result[depth + 1][ny][nx] > result[depth][y][x] + 2:
                        result[depth + 1][ny][nx] = result[depth][y][x] + 2
                        q.append((depth + 1, ny, nx))
                    # 만약 그자리에 있기 -> result[depth][y][x] += 1을 하고, 같은 좌표를 다시 큐에 넣어야함
                # 그렇게 1 키운 수를 나중에 접근하면..
            elif arr[ny][nx] == 1:
                continue
            else:  # 벽이 없는 경우
                if result[depth][ny][nx] > result[depth][y][x] + 1:
                    result[depth][ny][nx] = result[depth][y][x] + 1
                    q.append((depth, ny, nx))

ans = float('inf')
for i in range(k, -1, -1):
    # print(result[i])
    # print()
    ans = min(ans, result[i][n-1][m-1])

if ans == float('inf'):
    print(-1)
else:
    print(ans)