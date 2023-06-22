import sys
from collections import deque
sys.stdin = open("input.txt","r")

n, k = map(int,input().split())
q = deque()
q.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break
    if 0<=s-1<100001 and visited[s-1]==-1:
        visited[s-1]=visited[s]+1
        q.append(s-1)
    if 0<s*2<100001 and visited[s*2] == -1:
        visited[s*2] = visited[s]
        q.appendleft(s*2)
    if 0<=s+1<100001 and visited[s+1] == -1:
        visited[s+1] = visited[s]+1
        q.append(s+1)

'''
순간이동 : 0
걷기: 1
양방향 큐를 활용 - 순간이동하는 경우 appendleft로 맨 앞 추가(우선시)
                걷는 경우 append로 뒤에 추가
'''