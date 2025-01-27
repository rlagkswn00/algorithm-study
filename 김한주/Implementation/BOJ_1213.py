import sys
input = sys.stdin.readline

name = list(input().strip())
err = "I'm Sorry Hansoo"

nameDict = {}
for n in name:
    if n in nameDict:
        nameDict[n] += 1
    else:
        nameDict[n] = 1


left = []
right = []
rightIndex = len(name)-1
oddCnt = 0
oddVal = ""

for alph in sorted(nameDict.keys()): # 사전순으로 해야하기 떄문에 A-Z순으로 해야함. 그래서 정렬된 키 값을 사용해야 함.
    if nameDict[alph] % 2 != 0:
        oddCnt += 1
        oddVal = alph
        nameDict[alph]-=1

if oddCnt > 1:
    print(err)
    exit(0)
    
for alph in sorted(nameDict.keys()):
    while nameDict[alph] > 1:
        left.append(alph)
        right.append(alph)
        nameDict[alph] -= 2

right.reverse()
left.append(oddVal)
result = "".join(left + right)
print(result)