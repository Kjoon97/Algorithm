import heapq
import sys
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

# 방향성 없는 그래프이므로 x, y일 때와 y, x일 때 모두 추가
for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((cost, y))
    graph[y].append((cost, x))


def dijkstra(start):
    dist = [INF] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        ew, ev = heapq.heappop(q)

        if dist[ev] < ew:
            continue

        for nw,nv in graph[ev]:
            if dist[nv] > nw+ew:
                dist[nv] = nw+ew
                heapq.heappush(q, (nw+ew,nv))

    # 반환값은 최단 거리 배열
    return dist


v1, v2 = map(int, input().split())

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v]

result = min(v1_path, v2_path)
print(result if result < INF else -1)