<<<<<<< HEAD
def solution(dartResult):
    dartResult = list(dartResult)
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'#': -1, '*': 2}
    while dartResult:
        print(dartResult)
        tmp = dartResult.pop(0)
        
        if tmp == '1' and dartResult[0] == '0':
            tmp += dartResult.pop(0)
        
        score = int(tmp)
        
        tmp = dartResult.pop(0)
        score **= bonus[tmp]
        
        if dartResult[0] == '#' or dartResult[0] == '*':
            tmp = dartResult.pop(0)
            score *= option[tmp]
        print(score)

solution('1S2D*3T')
=======
N = int(input())

lineList = []

for _ in range(N):
    lineList.append(list(map(int, input().split())))

lineList.sort()

dp = [1]*N
for i in range(N):
    print(dp)
    for j in range(i):
        if lineList[i][1] > lineList[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
            print(i, j)

print(N-max(dp))
>>>>>>> 7c979a43d547a7b8ff1f7a97b7165fbe3d587eaa
