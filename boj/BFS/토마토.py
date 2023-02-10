import sys
sys.stdin = open("input.txt","r")
from collections import deque

m,n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
completed =[[False for _ in range(m)] for _ in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] ==1 :
            completed[i][j]=1
            q.append((i,j))

while q:
    ey, ex = q.popleft()
    for i in range(4):
        ny = ey+dy[i]
        nx = ex+dx[i]

        if 0<=ny<n and 0<=nx<m and board[ny][nx]!=-1 and completed[ny][nx]==False:
            completed[ny][nx]=True
            board[ny][nx]=board[ey][ex]+1
            q.append((ny,nx))


if any([board[i][j]==0 for i in range(n) for j in range(m)]):
    print(-1)
elif all([board[i][j]<=1 for i in range(n) for j in range(m)]):
    print(0)
else:
    max_value = max([board[i][j]] for i in range(n) for j in range(m))
    print(max_value[0]-1)