import sys

sys.stdin = open("input.txt", "r")
from collections import deque

n = int(input())

pictures = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x, y))
    while q:
        ex, ey = q.popleft()
        for i in range(4):
            nx, ny = ex + dx[i], ey + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and pictures[ex][ey] == pictures[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

#색약이 아닐 경우 탐색
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt1+=1
print(cnt1, end=" ")

#visited 초기화 & 빨간색을 녹색으로 변경.
for i in range(n):
    for j in range(n):
        visited[i][j]=False
        if pictures[i][j]=='R':
            pictures[i][j]='G'

#색약일 경우 탐색.
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2+=1
print(cnt2)
