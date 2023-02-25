import sys
import heapq
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
'''
정점:1번~v번까지 번호
출력- 최소 스패닝 트리의 가중치(모든 가중치 합)를 출력하라. 
시간복잡도 O(ElogE)
MST 절차. 
1. 간선을 인접 리스트에 넣기.
2. 힙에 시작 점 넣기.
3. 힙이 빌때까지 반복:
    - 힙의 최솟 값 꺼내서, 해당 노드 방문 안했다면
    - 방문 표시, 해당 비용 추가, 연결된 간선들 힙에 넣어주기. 
'''

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
visited=[False]*(v+1)
result = 0
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

#v가 최소 1이므로 1부터 넣어줌. (무게,노드번호)
heap = [(0,1)]

while heap:
    w,e_node = heapq.heappop(heap)
    if visited[e_node]==False:
        visited[e_node]=True
        result+=w
        for n_node in graph[e_node]:
            if visited[n_node[1]]==False:
                heapq.heappush(heap,n_node)


print(result)