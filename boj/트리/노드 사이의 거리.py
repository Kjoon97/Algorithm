import sys
sys.stdin = open("input.txt","r")
'''
1.문제
* N개의 노드로 이루어진 트리. M개의 노드 쌍을 입력 받으면 두 노드 사이의 거리 출력
2. 입력
* N:노드의 개수 
* 트리 상에 연결된 두 점, 거리를 입력 받음.
'''
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

#탐색.
def dfs(start_node,end_node,sum):
    if start_node == end_node:
        print(sum)
        return
    visited[start_node]=True
    for next in graph[start_node]:
        if not visited[next[0]]:
            dfs(next[0],end_node,sum+next[1])
#트리 초기화
for _ in range(n-1):
    a,b,d = map(int,input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

for _ in range(m):
    start_node,end_node = map(int,input().split())
    visited = [False] * (n + 1)
    dfs(start_node,end_node,0)