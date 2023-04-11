import sys
#sys.stdin = open("input.txt","r")
from collections import deque
n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
new_grid = [[0 for _ in range(m)] for _ in range(n)]
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
visited = [[False for _ in range(m)] for _ in range(n)]

def all_melt():
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                return False
    return True

def melt(x,y):
    cnt = 0
    for dx,dy in zip(dxs,dys):
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<m:
            if grid[nx][ny]==0:
                cnt+=1
    temp = grid[x][y]-cnt
    if temp<0:
        temp = 0
    new_grid[x][y] = temp

def doing_melt():
    for i in range(n):
        for j in range(m):
            new_grid[i][j] = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                melt(i, j)

    for i in range(n):
        for j in range(m):
            grid[i][j] = new_grid[i][j]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        ex,ey = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = ex+dx
            ny = ey+dy

            if 0<=nx<n and 0<=ny<m:
                if grid[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx,ny))




def count_mountain():

    for i in range(n):
        for j in range(m):
            visited[i][j]= False
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] and not visited[i][j]:
                bfs(i,j)
                cnt+=1

    return cnt

year = 0

while True:
    cnt = 0
    doing_melt()
    cnt = count_mountain()
    year += 1
    if cnt >= 2:
        break
    if all_melt():
        year=0
        break

print(year)


