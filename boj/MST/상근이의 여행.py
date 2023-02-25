import sys
import heapq
#sys.stdin = open("input.txt","r")
t = int(input())
def mst():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append((1,b))
        graph[b].append((1,a))

    q = [(0,1)]

    result =0
    while q:
        w, en = heapq.heappop(q)
        if visited[en]==False:
            visited[en]=True
            result += w
            for nn in graph[en]:
                if visited[nn[1]]==False:
                    heapq.heappush(q,nn)

    print(result)


for _ in range(t):
    mst()