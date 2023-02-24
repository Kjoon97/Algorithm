import sys
from collections import deque
#sys.stdin = open("input.txt","r")
'''
n:가수의 수, m:보조 pd의 수 
'''
n, m = map(int,input().split())
singers=[]
for _ in range(m):
    singers.append(list(map(int,input().split())))

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]


'''
1. 그래프, indegree초기화
2. 진입점이 0인 정점을 큐에 넣는다.
3. 큐에서 해당 정점을 빼고 해당 정점의 간선을 -1 빼준다.
4. 진입점이 0인 정점 큐에 넣는다.
'''

for team in singers:
    for i in range(1,len(team)-1):
        graph[team[i]].append(team[i+1])
        inDegree[team[i+1]]+=1
#print(graph)
#print(inDegree)

result=[]
q=deque()

for i in range(1,n+1):
    if inDegree[i]==0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        inDegree[i]-=1
        if inDegree[i]==0:
            q.append(i)

#순서 정하는게 불가능한 경우            
if sum(inDegree)>0:
    print(0)
else:
    for r in result:
        print(r)
