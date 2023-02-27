import sys
sys.setrecursionlimit(10000)
#sys.stdin =open("input.txt","r")

'''
1. n:정점의 개수, m:간선의 개수
2. u,v : 양 끝 정점
3. 연결 요소의 개수를 구하라
'''

n, m = map(int,input().split())
visited = [False]*(n+1)
graph= [[] for _ in range(n+1)]

#그래프 초기화
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start]=True
    #연결된 노드들 방문 안했으면 방문 처리.
    for n in graph[start]:
        if not visited[n]:
            dfs(n)

#1번~n번 노드 전부 확인.
count = 0
for i in range(1,n+1):
    if not visited[i]:
        count+=1
        dfs(i)

print(count)