import sys
import heapq
#sys.stdin = open("input.txt","r")
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [False]*(n)
# print(graph)
q = [(0,0)]
result =0
while q:
    ew, ev = heapq.heappop(q)
    if visited[ev]==False:
        visited[ev]=True
        result+=ew
        for i in range(n):
            if ev!=i:
                heapq.heappush(q,(graph[ev][i],i))

print(result)


