import sys
sys.stdin = open("input.txt","r")
'''
입력.
n*n 도시, m: 병원 개수.
0:바이러스, 1:벽, 2:병원.
출력.
M개의 병원을 적절히 골라 모든 바이러스를 없애는데 필요한 최소 시간 출력하라. 
모든 바이러스를 없앨 수 없다면 -1 출력.
'''
from collections import deque
n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
hospitals =[]
s_hospitals=[]
visited = [[False for _ in range(n)] for _ in range(n)]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
if all([board[i][j]!=0 for i in range(n) for j in range(n)]):
    print(0)
    exit(0)
#병원 위치 저장
cnt=0
for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            hospitals.append((i,j))
            cnt+=1
indx =[0]*m
min_val = 2147000000
fail=False
def dfs(L,s):
    global fail
    global min_val
    if L==m:
        visited = [[False for _ in range(n)] for _ in range(n)]
        step = [b[:] for b in board]
        q= deque()
        for i in range(m):
            hy,hx = hospitals[indx[i]]
            q.append((hy,hx))
            visited[hy][hx]=True
        while q:
            ey, ex = q.popleft()
            for i in range(4):
                ny = ey+dy[i]
                nx = ex+dx[i]
                if 0<=ny<n and 0<=nx<n:
                    if visited[ny][nx]==False and board[ny][nx]!=1:
                        visited[ny][nx]=True
                        step[ny][nx]= step[ey][ex]+1
                        q.append((ny,nx))
        # for s in step:
        #     print(s)
        # print()
        if not any([step[i][j]==0 for i in range(n) for j in range(n)]):
            min_val = min(max([step[i][j] for i in range(n) for j in range(n) if (i,j) not in hospitals])-2, min_val)
        return
    else:
        for i in range(s,cnt):
            indx[L]=i
            dfs(L+1, i+1)

dfs(0,0)
if min_val!=2147000000:
    print(min_val)
else:
    print(-1)