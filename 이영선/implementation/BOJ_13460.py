# 구현 - 13460번 - 구슬 탈출 2
import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = []
by, bx, ry, rx, hy, hx = 0, 0, 0, 0, 0, 0
for i in range(n):
    line = list(input().strip())
    arr.append(line)

    for j in range(m):
        if line[j] == 'B':
            by, bx = i, j
        elif line[j] == 'R':
            ry, rx = i, j
        elif line[j] == 'O':
            hy, hx = i, j

ans = float('inf')
q = deque()
q.append((ry, rx, by, bx, 1))
visited = set()
visited.add((ry, rx, by, bx))


def move(y, x, dy, dx):
    cnt = 1
    while arr[y][x] != '#' and arr[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    if arr[y][x] == '#':
        return y-dy, x-dx, cnt -1
    return y, x, cnt


while q:
    ry, rx, by, bx, result = q.popleft()

    if result > 10:
        break
    for i in range(4):
        nry, nrx, rcnt = move(ry, rx, dy[i], dx[i])
        nby, nbx, bcnt = move(by, bx, dy[i], dx[i])

        if arr[nby][nbx] == 'O':  # 파란색이 구멍으로 들어감
            continue
        if arr[nry][nrx] == 'O':
            print(result)
            exit()

        if nry == nby and nrx == nbx:  # 둘이 겹쳐 있는 경우
            if rcnt > bcnt:
                nry -= dy[i]
                nrx -= dx[i]
            else:
                nby -= dy[i]
                nbx -= dx[i]

        if (nry, nrx, nby, nbx) not in visited:
            visited.add((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, result + 1))


print(-1)