# 백트래킹 - 25825번 - 빠른 무작위 메시지 전달
import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(12)]
ans = float('inf')

def pass_m(now, v, result):
    global ans
    # 항상 a -> b임
    a = (now // 2) * 2
    b = a + 1
    if now % 2 == 1:
        a, b = b, a
    # print('a=', a, ', b=', b)

    if not False in v:
        # print('현재 집단', now // 2, ', result =', result)
        ans = min(ans, result)

    for i in range(6):
        if not v[i]:
            v[i] = True
            pass_m(2 * i, v, result + arr[b][2 * i] + arr[2 * i][2 * i + 1])
            pass_m(2 * i + 1, v, result + arr[b][2 * i + 1] + arr[2 * i][2 * i + 1])
            v[i] = False

visited = [False] * 6
for i in range(6):
    visited[i] = True
    pass_m(2 * i, visited, arr[2 * i][2 * i + 1])
    pass_m(2 * i + 1, visited, arr[2 * i][2 * i + 1])
    visited[i] = False

print(ans)
