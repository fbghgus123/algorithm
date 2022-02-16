# 문제 : https://programmers.co.kr/learn/courses/30/lessons/17677

import re
def solution(str1, str2):
    noneWord = re.compile('[^a-z]')
    str1Arr = {}
    str2Arr = {}
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    uni = 0
    inter = 0
    
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if not noneWord.search(tmp):
            if tmp in str1Arr:
                str1Arr[tmp] += 1
            else:
                str1Arr[tmp] = 1
            uni += 1
            
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if not noneWord.search(tmp):
            if tmp in str2Arr:
                str2Arr[tmp] += 1
            else:
                str2Arr[tmp] = 1
            uni += 1
    
    for i in str1Arr.items():
        if i[0] in str2Arr:
            if i[1] > str2Arr[i[0]]:
                uni -= str2Arr[i[0]]
                inter += str2Arr[i[0]]
            else:
                uni -= i[1]
                inter += i[1]
    
    if uni == 0:
        return 65536
    
    print(str1Arr)
    print(str2Arr)
    print(uni, inter)
    
    return int(inter / uni * 65536)