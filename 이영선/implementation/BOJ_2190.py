# 구현 - 2190번 - 뱀
import sys

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# (0, 1)에서 왼쪽 -> (-1, 0)
# (0, 1)에서 오른쪽 -> (1, 0)
# (0, -1)에서 왼쪽 -> (1, 0)
# (0, -1)에서 오른쪽 -> (-1, 0)
# (1, 0)에서 왼쪽 -> (0, 1)
# (1, 0)에서 오른쪽 -> (0, -1)
# (-1, 0)에서 왼쪽 -> (0, -1)
# (-1, 0)에서 오른쪽 -> (0, 1)

n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    arr[y - 1][x - 1] = 1
l = int(input())  # 뱀의 방향 변환 횟수
direction = [[0] * 2 for _ in range(l)]
for i in range(l):
    x, c = input().split()  # 게임 시작 x초 후 L->왼쪽, D->오른쪽 으로 90도 회전
    direction[i] = (int(x), c)
# print(arr)
# print(direction)

snake = []
snake.append([0, 0])
arr[0][0] = -1
head = [0, 0]
nd = 1  # 왼쪽으로 회전 -> (nd+3) % 4, 오른쪽으로 회전 -> (nd+1) % 4
sec, sec_idx = 0, 0

while True:
    if sec_idx < l and sec == direction[sec_idx][0]:
        if direction[sec_idx][1] == 'L':
            nd = (nd + 3) % 4
        else:
            nd = (nd + 1) % 4
        sec_idx += 1
        continue
    sec += 1
    ny, nx = head[0] + dy[nd], head[1] + dx[nd]
    # print(f'ny={ny}, nx={nx}')
    # print('snake=', snake)
    if not (0 <= ny < n) or not (0 <= nx < n) or arr[ny][nx] == -1:
        # print('break')
        break
    if arr[ny][nx] == 0:
        tail = snake.pop(0)
        # print('tail=', tail)
        arr[tail[0]][tail[1]] = 0
    snake.append([ny, nx])

    head = [ny, nx]
    arr[ny][nx] = -1

    # print('sec=', sec)
    # for i in range(n):
    #     print(arr[i])
    # print()

print(sec)