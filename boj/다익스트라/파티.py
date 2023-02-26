import sys
import heapq
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
'''
n:학생 수, m:단방향 도로,x:목적지
시작점,끝점, 소요시간 
1. 거리를 인접리스트에 저장한다.
2. 거리 배열을 무한 으로 초기화한다. 
3. 시작점을 힙큐에 넣는다. 거리 배열[start]=0
4. 큐에서 반복문으로 노드를 빼낸다. 
    나온 노드의 거리 값이 거리 배열보다 크면 무시
    경로를 경유하면서 거리 배열> 새로운 경로 합 -> 거리 배열 갱신,
    힙큐에(새로운 경로합, 노드)추가. 
'''
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

def dijkstra(start):
    dist = [INF] * (n + 1)
    q = [(0,start)]
    dist[start]=0
    while q:
        ew, ev = heapq.heappop(q)
        if dist[ev]<ew:
            continue
        for nw, nv in graph[ev]:
            if dist[nv] > ew+nw:
                dist[nv]=ew+nw
                heapq.heappush(q,(dist[nv],nv))

    return dist

result =0
for i in range(1,n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result,go[x]+back[i])

print(result)