# 백트래킹 - 9663번 - N-Queen
import sys
input = sys.stdin.readline

dy = [1, 1, 1]
dx = [0, -1, 1]

n = int(input())
ans = 0

def change(y, x, v):
    arr = []
    v[y][x] = True
    arr.append((y, x))
    for i in range(3):
        m = 1
        while True:
            ny = y + dy[i] * m
            nx = x + dx[i] * m
            if (0 <= ny < n) and (0 <= nx < n):
                if not v[ny][nx]:
                    v[ny][nx] = True
                    arr.append((ny, nx))
                m += 1
                continue
            break
    return arr

def restore(arr, v):
    for (y, x) in arr:
        v[y][x] = False

def put(y, x, v):
    global n, ans
    if y == n - 1:
        ans += 1
        return
    for i in range(n):
        if not v[y+1][i]:
            arr = change(y + 1, i, v)
            put(y + 1, i, v)
            restore(arr, v)


visited = [[False] * n for _ in range(n)]

for i in range(n):
    arr = change(0, i, visited)
    put(0, i, visited)
    restore(arr, visited)
print(ans)