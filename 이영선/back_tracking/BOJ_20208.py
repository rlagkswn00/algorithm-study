# 백트래킹 - 20208번 - 진우의 민트초코우유
## 스트레스... Python3으로 하면 시간초과;; Pypy3로 돌려라
## 이건 재귀로 풀었어도 재귀 호출 횟수가 적어서 메모리 초과가 없나보다ㅠ
import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())
cnt = 0
place = dict()
HOME = 0
arr = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            place[HOME] = [i, j]
        if line[j] == 2:
            cnt += 1
            place[cnt] = [i, j]
if cnt == 0:
    print(0)
    exit()

# 각 초코우유/집 에서 초코우유 까지의 거리 = |ay-by| + |ax+bx|
ans = 0

def calculate(now, next):
    now_y, now_x = place[now]
    next_y, next_x = place[next]
    return abs(now_y - next_y) + abs(now_x - next_x)


def go(now, now_h, v, result):
    global cnt, ans, h, HOME
    if now_h >= calculate(now, HOME):
        ans = max(ans, result)
    # print('이동 후 위치 =', place[now])
    # print('현재까지 먹은 우유 개수 =', result)
    # print('현재 체력 =', now_h)
    # print()

    for i in range(1, cnt + 1):
        if not v[i]:
            dist = calculate(now, i)
            if now_h >= dist:
                v[i] = True
                go(i, now_h + h - dist, v, result + 1)
                v[i] = False


milk = [False] * (cnt + 1)  # 먹은 우유인지 확인하는 배열
milk[0] = True  # 집

for i in range(1, cnt + 1):
    d = calculate(HOME, i)
    if m >= d:
        milk[i] = True
        go(i, m + h - d, milk, 1)
        milk[i] = False

print(ans)