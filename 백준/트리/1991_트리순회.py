# 문제 : https://www.acmicpc.net/problem/1991

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
for _ in range(n):
    a, b, c = input().strip().split()
    tree[a].append(b)
    tree[a].append(c)
pre = []
def preorder(current):
    global pre
    pre.append(current)
    if tree[current][0] != '.':
        preorder(tree[current][0])
    if tree[current][1] != '.':
        preorder(tree[current][1])

ino = []
def inorder(current):
    global ino
    if tree[current][0] != '.':
        inorder(tree[current][0])
    ino.append(current)
    if tree[current][1] != '.':
        inorder(tree[current][1])

post = []
def postorder(current):
    global post
    if tree[current][0] != '.':
        postorder(tree[current][0])
    if tree[current][1] != '.':
        postorder(tree[current][1])
    post.append(current)

preorder('A')
inorder('A')
postorder('A')
print(''.join(pre))
print(''.join(ino))
print(''.join(post))

