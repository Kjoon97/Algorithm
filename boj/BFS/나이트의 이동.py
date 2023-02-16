import sys
sys.stdin = open("input.txt","r")
from collections import deque
testcase = int(input())
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    while q:
        ex, ey = q.popleft()
        for i in range(8):
            nx = ex+dx[i]
            ny = ey+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==False:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    board[nx][ny]= board[ex][ey]+1


for _ in range(testcase):
    n= int(input())
    visited = [[False for _ in range(n)] for _ in range(n)]
    board = [[0 for _ in range(n)] for _ in range(n)]
    sx,sy = map(int,input().split())
    endx,endy = map(int,input().split())
    bfs(sx,sy)
    print(board[endx][endy])
