import sys
from collections import deque
sys.stdin = open("input.txt","r")
'''
n:학생번호(1~n번), m= 키를 비교한 횟수.
번호 a,b가 주어짐. a가 b에 앞에 서야함. 
'''
n, m = map(int,input().split())
#간선 정보
graph=[[] for _ in range(n+1)]
#진입 차수
inDegree=[0 for _ in range(n+1)]

#방향 그래프, 진입 차수 작성. 
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    inDegree[b]+=1

q=deque()
answer=[]

#진입차수가 0이면 큐에 삽입.
for i in range(1,n+1):
    if inDegree[i]==0:
        q.append(i)

while q:
    now=q.popleft()
    answer.append(now)
    #해당 원소와 연결된 노드들의 진입 차수 1빼기.
    for i in graph[now]:
        inDegree[i]-=1
        #진입 차수가 0이면 큐에 삽입. 
        if inDegree[i]==0:
            q.append(i)

print(*answer)
