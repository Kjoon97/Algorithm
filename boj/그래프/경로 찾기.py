import sys
sys.stdin = open("input.txt","r")
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited = [0]*n

    while q:
        now_n = q.popleft()
        for next_n in graph[now_n]:
            if not visited[next_n]:
                visited[next_n]=1
                q.append(next_n)

    print(*visited)



n = int(input())
graph = [[] for _ in range(n)]

#행렬 -> 인접리스트
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        if arr[j]==1:
            graph[i].append(j)

for i in range(n):
    bfs(i)