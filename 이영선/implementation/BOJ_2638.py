# DFS - 2638번 - 치즈
## 내부 공기와 외부 공기를 구분하는 것이 포인트!!
## 메모리 초과가 나는 이유 파악 후 정리하기!!!!!!!!

import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
external_air = deque()

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
cheese = {(y, x) for y in range(r) for x in range(c) if arr[y][x] == 1}

def external_air():
    global r, c
    external_arr = [[False] * c for _ in range(r)]
    q = deque([(0, 0)])
    external_arr[0][0] = True

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if (0 <= ny < r) and (0 <= nx < c) and arr[ny][nx] == 0 and not external_arr[ny][nx]:
                external_arr[ny][nx] = True
                q.append((ny, nx))
    return external_arr

ans = 0
while cheese:
    remove = []
    ans += 1
    external = external_air()
    for (y, x) in list(cheese):
        cnt = 0
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if (0 <= ny < r) and (0 <= nx < c):
                if external[ny][nx]:
                    cnt += 1
        if cnt >= 2:
            remove.append((y, x))

    for (ry, rx) in remove:
        cheese.discard((ry, rx))
        arr[ry][rx] = 0
print(ans)

# 7 9
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0
# 답 = 3