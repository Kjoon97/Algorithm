import sys
import heapq
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n, m = map(int,input().split())
graph =[[] for _ in range(n+1)]
visited =[False]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

q = [(0,1)]
result =[]
while q:
    ew,ev = heapq.heappop(q)
    if visited[ev]==False:
        visited[ev]=True
        result.append(ew)
        for nw, nv in graph[ev]:
            if visited[nv]==False:
                heapq.heappush(q,(nw,nv))

print(sum(result)-max(result))