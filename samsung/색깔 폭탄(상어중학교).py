import sys
sys.stdin = open("input.txt","r")
'''
-1: 검은 돌
0: 빨간 색 폭탄
1~m: 빨간 색과 다른 색의 폭탄.(1:노란,2:초록,3:파란)
폭탄 묶음이 없을 때까지 계속 반복.
폭탄 묶음 : 모두 같은 색깔의 폭탄 or
          빨간색 폭탄을 포함하여 2개의 색으로 이루어진 폭탄.
          가장 크기가 크고, 빨간 색 폭탄이 가장 적게 포함, 기준점(가장 큰 행,작은 열) 중 가장 행이 큰 폭탄.
          기준점 중 가장 작은 폭탄 묶음.
선택된 폭탄 묶음 모두 제거. + 중력(폭탄- 떨어짐, 돌- 떨어지지 x)
반시계 방향으로 90도 만큼 격자 회전. +중력
c = 폭탄 묶음에서의 폭탄 개수. 
점수 = c*c
폭탄 묶음이 없을 때까지 라운드 반복.
* 입력:
n: 격자 크기(~20), m: 폭탄 종류
격자 주어짐.

* 풀이 - 빨간색이 아닌 폭탄에서 시작, 색이 동일하거나 빨간색인 곳에서만 탐색 진행.
tuple묶기 (폭탄 묶음 크기, -빨간색 폭탄 수, 기준점 행 번호, -기준점 열 번호) 
'''
from collections import deque
RED =0
ROCK =-1
EMPTY = -2
EMPTY_BUNDLE = (-1,-1,-1,-1)

n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
temp = [[EMPTY for _ in range(n)] for _ in range(n)]
dq = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
ans =0

#반시계 방향으로 90도 만큼 회전
def rotate():
    for i in range(n):
        for j in range(n):
            temp[i][j]=EMPTY

    #반시계 방향 90도 회전
    for j in range(n-1,-1,-1):
        for i in range(n):
            temp[n-1-j][i] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j]= temp[i][j]


def gravity():
    for i in range(n):
        for j in range(n):
            temp[i][j]=EMPTY

    for j in range(n):
        last_idx = n-1
        for i in range(n-1,-1,-1):
            if grid[i][j]==EMPTY:
                continue
            if grid[i][j]==ROCK:
                last_idx = i
            temp[last_idx][j] = grid[i][j]
            last_idx-=1

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


def clean(x,y):
    #1. (x,y)를 시작으로 지워야할 폭탄 묶음 표시
    bfs(x,y,grid[x][y])

    #제거
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                grid[i][j]=EMPTY
    #중력 작용.
    gravity()

def bfs(x,y,color):
    #visited 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j]=False

    #시작점 표시합니다.
    visited[x][y]=True
    dq.append((x,y))

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while dq:
        cx,cy = dq.popleft()

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==False:
                    if grid[nx][ny]==color or grid[nx][ny]==RED:
                        dq.append((nx,ny))
                        visited[nx][ny]=True


#(x,y) 지점을 시작으로 bundle 정보 계산
def get_bundle(x,y):
    #(x,y) 시작으로 bfs 탐색.
    bfs(x,y,grid[x][y])

    #bundle 정보 반환
    bomb_cnt=0
    red_cnt=0
    standard =(-1,-1)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                continue
            bomb_cnt+=1

            if grid[i][j]==RED:
                red_cnt+=1
            elif (i,-j) > standard:
                standard = (i,-j)

    std_x, std_y = standard

    return (bomb_cnt, red_cnt, std_x, std_y)


def find_best_bundle():
    best_bundle = EMPTY_BUNDLE

    #빨간색이 아닌 폭탄들 탐색
    for i in range(n):
        for j in range(n):
            if grid[i][j]>=1:
                bundle = get_bundle(i,j)
                if bundle >= best_bundle:
                    best_bundle = bundle

    return best_bundle

def simulate():
    global ans

    #1. 크기가 최대인 폭탄 묶음 찾기.
    best_bundle = find_best_bundle()
    bomb_cnt, _, x, y = best_bundle

    if best_bundle==EMPTY_BUNDLE or bomb_cnt<=1:
        return False

    #2.선택된 폭탄 묶음 제거, 중력 작용.
    ans+=bomb_cnt*bomb_cnt
    clean(x,-y)

    #3. 반시계 방향으로 90회전
    rotate()

    #중력 작용.
    gravity()

    return True

while True:
    keep_going = simulate()

    if not keep_going:
        break

print(ans)

