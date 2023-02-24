import sys
sys.stdin = open("input.txt","r")
'''
n:정점의 개수,
m:간선의 개수
'''

def dfs(prev, node, graph, visited):
    visited[node] = True # 방문처리
    for next_node in graph[node]:
        # 다음 노드가 이전 노드와 같다면 DFS 수행 x (무시)
        if next_node == prev:
            continue
        # 다음 노드 != 이전 노드, 이미 방문했다면 사이클이 생긴것 (트리가 아님)
        if visited[next_node]:
            return False
        # 다음 노드 != 이전 노드, 다음 노드 첫 방문 -> DFS 수행
        # DFS 수행 도중 사이클이 생긴 경우에는 False 반환
        if not dfs(node, next_node, graph, visited):
            return False
    # DFS 수행 중 사이클이 생기지 않은 경우 True 반환
    return True

i = 1
n, m = map(int, input().split())
while n + m != 0:
    graph = [[] for _ in range(n+1)] # 인접 노드 저장하는 그래프
    visited = [False] * (n+1) # 방문 여부 확인하는 배열
    for _ in range(m):
        a, b = map(int, input().split())
        # 양방향으로 노드 저장
        graph[a].append(b)
        graph[b].append(a)

    t = 0 # 트리의 개수
    for v in range(1, n+1):
        if not visited[v]: # 방문하지 않은 경우만 DFS 수행
            if dfs(0, v, graph, visited):
                t += 1 # DFS 수행결과 사이클이 없는 경우 트리의 개수 증가
    if t == 0:
        print("Case {}: No trees.".format(i))
    elif t == 1:
        print("Case {}: There is one tree.".format(i))
    else:
        print("Case {}: A forest of {} trees.".format(i, t))

    n, m = map(int, input().split())
    i += 1