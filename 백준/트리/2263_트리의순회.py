# 문제 : https://www.acmicpc.net/problem/2263

import sys
sys.setrecursionlimit(100000)

n = int(input())
inorder = input().split()
postorder = input().split()

answer = []
def divide(si, ei, sp, ep):
    global count
    if si <= ei and sp <= ep:
        root = postorder[ep]
        answer.append(root)
        if si < ei and sp < ep:
            endIn = inorder.index(root)
            endPost = sp + (endIn-si-1)
            # print(root)
            # print(inorder[si:endIn], inorder[sp:endPost+1])
            # print(postorder[endIn+1:ei+1], postorder[endPost+1:ep])
            divide(si, endIn-1, sp, endPost)
            divide(endIn+1, ei, endPost+1, ep-1)
            

divide(0, len(inorder)-1, 0, len(postorder)-1)
print(*answer)