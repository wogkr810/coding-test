def preorder(tree,root):
    if root != '.':
        print(root,end='')
        preorder(tree,tree[root][0])
        preorder(tree,tree[root][1])

def inorder(tree,root):
    if root != '.':
        inorder(tree,tree[root][0])
        print(root,end='')
        inorder(tree,tree[root][1])

def postorder(tree,root):
    if root != '.':
        postorder(tree,tree[root][0])
        postorder(tree,tree[root][1])
        print(root,end='')

from collections import defaultdict
N = int(input())
tree = defaultdict(list)
for _ in range(N):
    root, left, right = input().split()
    tree[root].append(left)
    tree[root].append(right)

preorder(tree,'A')
print()
inorder(tree,'A')
print()
postorder(tree,'A')