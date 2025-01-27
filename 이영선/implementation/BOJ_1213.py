# 구현 - 1213번 - 팰린드롬 만들기
## 입력받은 문자열 배열을 정렬 -> 앞에서부터 순서대로 팰린드롬 배치를 한다. (대칭을 이루도록)
## 만약 홀수개인 알파벳이 있으면 가운데에 배치하기
## 만약 홀수개인 알파벳이 여러개이면 중단하기

import sys
input = sys.stdin.readline
input_str = list(input().strip())
n = len(input_str)
input_str.sort()
ans = ['']* n
center = (n % 2 == 1)        # 홀수인지 짝수인지
pivot = n //2
idx, i = 0, 0
# print(input_str)

while True:
    if i >= (n-1) or n <= idx:
        if center and i == n - 1 and idx == n // 2 and ans[pivot] == '':
            ans[pivot] = input_str[i]
            i += 1
        break

    if input_str[i] == input_str[i+1]:
        ans[idx] = input_str[i]
        ans[n -1 - idx] = input_str[i]
        i += 2
        idx += 1
    else:
        if center and ans[pivot] == '':
            ans[pivot] = input_str[i]
            i += 1
        else:
            # print('center=', center, ', pivot=', pivot)
            print("I'm Sorry Hansoo")
            exit()

print(''.join(ans))