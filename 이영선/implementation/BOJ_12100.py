# 구현 - 12100번 - 2048 (Easy)
import sys
from itertools import product
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def right(arr):
    global n
    new_arr = [[0]* n for _ in range(n)]

    for r in range(n):
        idx = n-1
        for c in range(n-1, -1, -1):
            if arr[r][c] == 0:
                continue
            if arr[r][c] != 0:
                if idx == n-1 and new_arr[r][idx] == 0:
                    new_arr[r][idx] = arr[r][c]
                    continue
                if arr[r][c] == new_arr[r][idx]:
                    new_arr[r][idx] *= 2
                    idx -= 1
                else:
                    if new_arr[r][idx] != 0:
                        idx -= 1
                    new_arr[r][idx] = arr[r][c]
    return new_arr

def left(arr):
    global n
    new_arr = [[0]* n for _ in range(n)]

    for r in range(n):
        idx = 0
        for c in range(n):
            if arr[r][c] == 0:
                continue
            if arr[r][c] != 0:
                if idx == 0 and new_arr[r][idx] == 0:
                    new_arr[r][idx] = arr[r][c]
                    continue
                if arr[r][c] == new_arr[r][idx]:
                    new_arr[r][idx] *= 2
                    idx += 1
                else:
                    if new_arr[r][idx] != 0:
                        idx += 1
                    new_arr[r][idx] = arr[r][c]


    return new_arr

def up(arr):
    global n
    new_arr = [[0]* n for _ in range(n)]
    for c in range(n):
        idx = 0
        for r in range(n):
            if arr[r][c] == 0:
                continue
            if arr[r][c] != 0:
                if idx == 0 and new_arr[idx][c] == 0:
                    new_arr[idx][c] = arr[r][c]
                    continue
                if arr[r][c] == new_arr[idx][c]:
                    new_arr[idx][c] *= 2
                    idx += 1
                else:
                    if new_arr[idx][c] != 0:
                        idx += 1
                    new_arr[idx][c] = arr[r][c]
    return new_arr

def down(arr):
    global n
    new_arr = [[0]* n for _ in range(n)]

    for c in range(n):
        idx = n-1
        for r in range(n-1, -1, -1):
            if arr[r][c] == 0:
                continue
            if arr[r][c] != 0:
                if idx == n-1 and new_arr[idx][c] == 0:
                    new_arr[idx][c] = arr[r][c]
                    continue
                if arr[r][c] == new_arr[idx][c]:
                    new_arr[idx][c] *= 2
                    idx -= 1
                else:
                    if new_arr[idx][c] != 0:
                        idx -= 1
                    new_arr[idx][c] = arr[r][c]

    return new_arr

def calculate(order_str):
    global n
    new_arr = arr
    for i in range(5):
        if order_str[i] == 'r':
            new_arr = right(new_arr)
        elif order_str[i] == 'l':
            new_arr = left(new_arr)
        elif order_str[i] == 'u':
            new_arr = up(new_arr)
        elif order_str[i] == 'd':
            new_arr = down(new_arr)
    ans = 0

    # print(new_arr)
    for i in range(n):
        ans = max(ans, max(new_arr[i]))
    return ans


ans = 0
p = list(product(['r', 'l', 'u', 'd'], repeat=5))

# print(p)
for i in p:
    # print(i)
    ans = max(ans, calculate(i))

print(ans)