import sys

sys.stdin = open("input.txt","r")
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]

ans =0
def bfs(y,x):
    global ans
    dq = deque()
    dq.append((y,x))
    visited[y][x]=1

    while dq:
        cy,cx = dq.popleft()
        if cy == n - 1 and cx == m - 1:
            print(visited[cy][cx])
            return

        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx]==0 and board[ny][nx]==1:
                    visited[ny][nx]= visited[cy][cx]+1
                    dq.append((ny,nx))
bfs(0,0)