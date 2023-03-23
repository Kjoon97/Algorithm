import sys
sys.stdin = open("input.txt","r")
'''
1:벽,
0:공간.
'''
from collections import deque
n, m = map(int, input().split())
map= [list(map(int,input())) for _ in range(n)]

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global visited
    q = deque()
    q.append((0,0,0))
    visited[0][0][0]=1
    while q:
        cx,cy,c = q.popleft()
        if cx ==n-1 and cy==m-1:
            return visited[cx][cy][c]
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if 0<=nx<n and 0<=ny<m:
                #다음 칸이 벽이 아니고, 방문하지 않았다면
                if map[nx][ny] ==0 and visited[nx][ny][c]==0:
                    visited[nx][ny][c]= visited[cx][cy][c]+1
                    q.append((nx,ny,c))

                #다음 칸이 벽이라면, 방문하지 않았다면
                if map[nx][ny] ==1 and visited[nx][ny][c]==0:
                    #벽을 부순적이 없다면 부숨.
                    if c==0:
                        visited[nx][ny][1] = visited[cx][cy][c]+1
                        q.append((nx,ny,1))
                    #벽을 부순 적이 있다면 넘어감.
                    elif c==1:
                        continue
    return -1

print(bfs())


