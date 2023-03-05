import sys
sys.stdin = open("input.txt","r")
from collections import deque
'''
상근이 동기: n명
학번: 1~n번
상근이 학번 : 1번.
리스트 가지고 있음. 리스트를 바탕으로 결혼식에 초대할 사람 구하기
'''
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    q = deque()
    visited[x]=1
    q.append(x)

    while q:
        ex = q.popleft()
        for nx in graph[ex]:
            if visited[nx]==0:
                q.append(nx)
                visited[nx]=visited[ex]+1

bfs(1)
result =0
for i in range(2, n+1):
    #본인이거나 친구거나 친구의 친구의 경우의 수가 최대 3개.
    if visited[i]<4 and visited[i]!=0:
        result+=1

print(result)