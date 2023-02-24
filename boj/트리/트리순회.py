import sys
sys.stdin = open("input.txt","r")
#루트 노드: A
#입력: 노드,왼쪽 자식 노드, 오른쪽 자식 노드

n = int(input())
tree={}
#트리 입력
for i in range(n):
    root,left,right= input().split()
    tree[root]=[left,right]

#전위 순회
def preOrder(root):
    if root!='.':
        print(root, end="")
        preOrder(tree[root][0])
        preOrder(tree[root][1])

#중위 순회
def inOrder(root):
    if root!='.':
        inOrder(tree[root][0])
        print(root,end="")
        inOrder(tree[root][1])

#후위 순회
def postOrder(root):
    if root!='.':
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root, end="")



preOrder('A')
print()
inOrder('A')
print()
postOrder('A')