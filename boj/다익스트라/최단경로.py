'''
- 한점 시작, 모든 거리: 다익스트라
- 간선, 인접 리스트 저장
- 거리 배열 무한대 초기화
- 시작점: 거리 배열0, 힙에 넣어주기
- 힙에서 빼면서 다음 것들 수행
    - 최신 값인지 먼저 확인
    - 간선을 타고 간 비용이 더 작으면 갱신

입력:
n:정점의 개수(1번~), m:간선의 개수,
'''
import sys
import heapq

sys.stdin = open("input.txt", "r")
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
#최단 거리 테이블
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    #a->b로 가는데 c비용
    graph[a].append((c,b))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        ew, ev = heapq.heappop(q)
        if distance[ev]<ew:
            continue

        for nw,nv in graph[ev]:
            if distance[nv]>ew+nw:
                distance[nv]=ew+nw
                heapq.heappush(q,(distance[nv],nv))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])