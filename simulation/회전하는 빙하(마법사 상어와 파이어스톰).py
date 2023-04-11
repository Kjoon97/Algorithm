import sys
sys.stdin = open("input.txt","r")
'''
2^n * 2^n 격자의 빙하를 회전.
얼음은 인접 회전성을 가짐. 
좌측 상단의 빙하를 특정 범위를 선택해서 회전 
빙하를 회전하는 범위: 레벨. 

n:회전 가능 레벨, q:횟수
빙하의 각 칸에 있는 얼음 양 
회전 레벨
'''

#현재 위치에서 이동해야할 위치 구하기 위해 dx,dy 테크닉 이용.
#각 칸마다 움직여야하는 방향에 대한 dx,dy 값에 움직여야할 크기에 half size를 곱하고 더해주기.
from collections import deque
n,q = map(int,input().split())
grid_size = 2**n
grid = [list(map(int,input().split())) for _ in range(grid_size)]
levels = list(map(int,input().split()))
next_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
dq = deque()
visited = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

#오른쪽, 아래, 위, 왼쪽.
dx = [0,1,-1,0]
dy = [1,0,0,-1]

def bfs():
    group_size =0
    while dq:
        cx,cy = dq.popleft()
        group_size+=1

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<grid_size and 0<=ny<grid_size:
                if not visited[nx][ny] and grid[nx][ny]:
                    dq.append((nx,ny))
                    visited[nx][ny]=True

    return group_size

def get_biggest_size():
    max_size=0
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] and not visited[i][j]:
                visited[i][j]=True
                dq.append((i,j))
                max_size = max(max_size,bfs())

    return max_size

def get_ice_nums():
    return sum([grid[i][j] for i in range(grid_size) for j in range(grid_size)])

def get_neighbor_nums(x,y):
    cnt =0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<grid_size and 0<=ny<grid_size and grid[nx][ny]:
            cnt+=1

    return cnt


def melt():
    #step1. 녹은 이후의 상태 저장할 배열 초기화
    for i in range(grid_size):
        for j in range(grid_size):
            next_grid[i][j]=0

    #step2. 인접한 칸의 수가 3개 이하인 곳의 얼음을 찾아 1씩 녹이기.
    for i in range(grid_size):
        for j in range(grid_size):
            cnt= get_neighbor_nums(i,j)
            if grid[i][j] and cnt<3:
                next_grid[i][j] = grid[i][j]-1
            else:
                next_grid[i][j] = grid[i][j]

    #step3. 녹은 이후 결과를 grid배열에 가져오기.
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = next_grid[i][j]


def move(sx,sy,half_size,move_dir):

    for x in range(sx,sx+half_size):
        for y in range(sy,sy+half_size):
            nx = x+dx[move_dir]*half_size
            ny = y+dy[move_dir]*half_size

            next_grid[nx][ny] = grid[x][y]

def rotate(level):
    #step1.
    #rotate 이후의 상태를 저장할 배열을 0으로 초기화.
    for i in range(grid_size):
        for j in range(grid_size):
            next_grid[i][j]=0

    box_size = 2**level
    half_size = 2**(level-1)

    #(2^level)*(2^level) 크기 격자의 왼쪽 위 모서리 위치를 잡는다.
    for i in range(0,grid_size,box_size):
        for j in range(0,grid_size,box_size):
            move(i,j,half_size,0)
            move(i,j+half_size,half_size,1)
            move(i+half_size,j,half_size,2)
            move(i+half_size,j+half_size,half_size,3)

    #rotate 이후의 결과를 grid배열로.
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j]=next_grid[i][j]


for level in levels:
    if level:
        rotate(level)
    melt()

print(get_ice_nums())
print(get_biggest_size())

