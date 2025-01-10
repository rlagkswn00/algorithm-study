# DP - 9465번 -스티커
## 그 동물원에 사자 넣는 DP 문제랑 비슷
import sys
input = sys.stdin.readline
t = int(input())


def dp(arr, n):
    result = [[0] * n for _ in range(2)]
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
        return
    elif n == 2:
        print(max(arr[0][0] + arr[1][1], arr[1][0] + arr[0][1]))
        return

    result[0][0] = arr[0][0]
    result[1][0] = arr[1][0]
    result[0][1] = arr[1][0] + arr[0][1]
    result[1][1] = arr[0][0] + arr[1][1]

    for i in range(2, n):
        result[0][i] = max(result[1][i-1], result[1][i-2]) + arr[0][i]
        result[1][i] = max(result[0][i-1], result[0][i-2]) + arr[1][i]
    print(max(result[0][n-1], result[1][n-1]))


for _ in range(t):
    n = int(input())
    arr = []
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))
    dp(arr, n)
