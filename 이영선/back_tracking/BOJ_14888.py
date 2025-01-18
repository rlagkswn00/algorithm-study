# 백트래킹 - 14888번 - 연산자 끼워넣기
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
ans_max, ans_min = -float('inf'), float('inf')

def calculate(value, idx, operator):
    if operator == 0:  # 덧셈
        return value + arr[idx]
    elif operator == 1:  # 뺄셈
        return value - arr[idx]
    elif operator == 2:  # 곱셈
        return value * arr[idx]
    else:  # 나눗셈
        if value  > 0:
            return value // arr[idx]
        return - ((-value) // arr[idx])


def bt(value, cnt):
    global n, ans_max, ans_min
    if cnt == n:
        ans_max = max(ans_max, value)
        ans_min = min(ans_min, value)
        return
    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            new_value = calculate(value, cnt, i)
            bt(new_value, cnt + 1)
            op[i] += 1

value = arr[0]
cnt = 1
for i in range(4):
    if op[i] > 0:
        op[i] -= 1
        new_value = calculate(value, cnt, i)
        if n == 1:
            print(new_value)
            print(new_value)
            exit()
        bt(new_value, cnt + 1)
        op[i] += 1

print(ans_max)
print(ans_min)
