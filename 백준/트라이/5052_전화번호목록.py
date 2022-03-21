# 문제 : https://www.acmicpc.net/problem/5052
# 도움된 글 : https://alpyrithm.tistory.com/72

import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    def insert(self, string):
        curr_node = self.head

        for s in string:
            if s not in curr_node.children:
                curr_node.children[s] = Node(s)
            curr_node = curr_node.children[s]

    def search_prefix(self, string):
        curr_node = self.head
        for s in string:
            curr_node = curr_node.children[s]
        
        if curr_node.children:
            return False
        else:
            return True

t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    nums = []
    for _ in range(n):
        num = input().rstrip()
        nums.append(num)
        trie.insert(num)
    flag = True
    nums.sort()
    for num in nums:
        if not trie.search_prefix(num):
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')

