import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
dy=[0,1,0,-1]
dx=[1,0,-1,0]

def bfs(y,x):
    dq = deque()
    dq.append((y,x))

    res =1
    while dq:
        cy, cx = dq.popleft()
        for i in range(4):
            ny = cy +dy[i]
            nx = cx +dx[i]

            if 0<=ny<n and 0<=nx<m:
                if check[ny][nx]==False and board[ny][nx]==1:
                    check[ny][nx]=True
                    dq.append((ny,nx))
                    res+=1

    return res
cnt=0
max_value = -2147000000
for i in range(n):
    for j in range(m):
        if board[i][j]==1 and check[i][j]==False:
            check[i][j]=True
            max_value=max(bfs(i,j), max_value)
            cnt+=1


print(cnt)
print(max_value)
