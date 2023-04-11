import sys
sys.stdin = open("input.txt","r")

'''
1. 문제:
* n*m 영역에 방화벽 설치하기.
* 불- 상하좌우 인접 공간으로 모두 번짐. 방화벽은 못 뚫음.
* 추가로 3개의 방화벽 설치해서 안전한 영역의 최댓 값 구하라.

2. 입력:
* n,m 격자 크기 (64)
* 격자 상태 - 2: 불, 1:방화벽, 0:빈칸.
'''
from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
empty_list = []
selected_index = []
bfs_q = deque()
max_empty_count =0


def remove_wall():
    for indx in selected_index:
        cur_x, cur_y = empty_list[indx]
        grid[cur_x][cur_y]=0


def bfs():
    dxs = [0,0,-1,1]
    dys = [-1,1,0,0]

    while bfs_q:
        x,y = bfs_q.popleft()

        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny] !=1:
                bfs_q.append((nx,ny))
                visited[nx][ny]= True

def build_wall():
    for indx in selected_index:
        cur_x, cur_y = empty_list[indx]
        grid[cur_x][cur_y]=1

def initailize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j]= False

def get_area():
    global max_empty_count
    initailize_visited()
    build_wall()

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j]==2:
                visited[i][j]= True
                bfs_q.append((i,j))
                bfs()


    empty_count =0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j]==0:
                empty_count+=1

    max_empty_count = max(empty_count, max_empty_count)

    remove_wall()

def dfs(cur_index, cnt):
    if cnt==3:
        get_area()
        return
    if cur_index == len(empty_list):
        return

    else:
        selected_index.append(cur_index)
        dfs(cur_index+1, cnt+1)
        selected_index.pop()
        dfs(cur_index+1, cnt)

#빈칸 수집하기
for i in range(n):
    for j in range(m):
        if grid[i][j]==0:
            empty_list.append((i,j))

#조합 탐색.
dfs(0,0)
print(max_empty_count)