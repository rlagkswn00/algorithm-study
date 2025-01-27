# 구현 - 14503번 - 로봇 청소기
## 구현은 다른 알고리즘에 비해 요구사항이 세부적이고 많은 것 같다.
## 하지만 차근차근 모든 요구사항을 구현하면 생각보다 쉬운 듯! 문제에서 시키는 대로만 하자!!
import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0


def near_dirty(y, x):
    global N, M
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if (0 <= ny < N) and (0 <= nx < M):
            if arr[ny][nx] == 0 and v[ny][nx] == False:
                return True
    return False


def vacuum(sy, sx, d):
    global N, M, cnt
    q = deque([(sy, sx)])

    while q:
        y, x = q.popleft()
        if not v[y][x]:     # 이미 청소 완료한 칸
            v[y][x] = True
            cnt += 1
        if near_dirty(y, x):        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
            for i in range(-1, -5, -1):
                dn = (d + i + 4) % 4
                ny, nx = y + dy[dn], x + dx[dn]
                if (0 <= ny < N) and (0 <= nx < M):
                    if arr[ny][nx] == 0 and v[ny][nx] == False:
                        d = dn
                        q.append((ny, nx))
                        # print('y=', ny, ', x=', nx)
                        break
        else:       # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            dn = (d+2) % 4
            ny, nx = y + dy[dn], x + dx[dn]
            if (0 <= ny < N) and (0 <= nx < M):
                if arr[ny][nx] == 1:
                    return
                else:
                    q.append((ny, nx))
                    continue


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[False] * M for _ in range(N)]


vacuum(r, c, d)
print(cnt)