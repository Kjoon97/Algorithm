import sys
#sys.stdin =open("input.txt","r")
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

#노드 개수
n = int(input())
Tree = [[] for _ in range(n+1)]

#트리 노드
for _ in range(n-1):
    a,b = map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)

#부모 노드
parents = [0 for _ in range(n+1)]

#dfs 탐색하면서 부모 노드 채워준다.
def dfs(start,tree,parents):
    for n in tree[start]:
        if parents[n]==0:
            parents[n]=start   #n:자식,start:부모
            dfs(n,tree,parents)

dfs(1,Tree,parents)

#부모 출력하기.
for i in range(2,n+1):
    print(parents[i])