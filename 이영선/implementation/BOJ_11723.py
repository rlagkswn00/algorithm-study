# 구현 - 11723번 - 집합
import sys
input = sys.stdin.readline
n = int(input())
ans = set()

for _ in range(n):
    input_str = input().strip()
    if input_str == 'all':
        ans = {i for i in range(1, 21)}
        continue
    elif input_str == 'empty':
        ans.clear()
        continue

    op, str_num = input_str.split()
    num = int(str_num)
    if op == 'add':
        ans.add(num)
    elif op == 'check':
        if num in ans:
            print(1)
        else:
            print(0)
    elif op == 'remove':
        ans.discard(num)        # 집합에서 값을 안전하세 삭제하고 싶으면 discard() 메서드를 사용하자.
    else:   # toggle
        if num in ans:
            ans.remove(num)
        else:
            ans.add(num)