import sys

sys.stdin = open("input.txt", "r")
'''
4*4 격자 체스판에서 술래잡기.
술래 말 하나만 사용하여 도둑말을 잡기. 술래말을 잡을 때마다 도둑 말의 방향 갖음.
말 방향 - 상하좌우, 대각선.
x,y - 0~
도둑 말 - 1~16
규칙.
    1. (0,0)에 있는 도둑말 잡고 시작. 
    2. 도둑 말: 번호가 작은 순으로 자신의 이동 방향으로 이동.
               다음 칸 - 빈칸 or 다른 도둑말이 있으면(해당 말과 위치 바꿈) 이동 가능
                      - 술래가 있거나 격자 밖이면 이동 불가.
               이동할 수 있을 때까지 45도 회전하며 갈 수 있는 칸 탐색.
               이동할 수 있는 칸이 없으면 이동 x. 
    3. 술래말: 도둑 말의 이동이 모두 끝나면 이동.
              어느 방향으로든 이동 가능. 
              한번의 여러 개의 칸 이동 가능. 
              지나는 칸들의 말들은 잡지 않음. 목표물만 잡음
              도둑 말이 없는 곳으로 이동 불가.
              도둑 말 잡으면 도둑 말의 방향 갖음. 
              이동할 수 있는 곳에 도둑말이 더 이상 존재 안하면 게임 끝.
입력:
    도둑말의 정보: p(번호), 방향(d),
출력: 적절하게 도둑말을 선택하여 얻은 점수의 최댓값은?
'''

import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

#상어 이동 후보지 반환
def shark_move(array,x,y):
    positions = []
    dir = array[x][y][1]  #상어 방향
    for _ in range(1,4):
        nx,ny = x+dx[dir], y+dy[dir]
        #경계 값 안에 있고, 물고기가 있으면 움직일 수 있다.
        if 0<=nx<4 and 0<=ny<4 and 1<=array[nx][ny][0] <=16:
            positions.append([nx,ny])
        x,y = nx,ny
    return positions

#물고기 위치 찾기.
def find_fish(array,index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0]==index:
                return (i,j)
    #물고기가 없는 경우
    return None

def move_fish(array,shark_x,shark_y): #배열, 상어 좌표
    position=[]
    for i in range(1,17):
        position = find_fish(array,i)
        if position is None:
            continue
        x,y = position
        dir = array[x][y][1] #물고기 방향
        for _ in range(8):
            nx, ny = x+dx[dir], y+dy[dir]
            if 0<=nx<4 and 0<=ny<4:  #경계값 안에 있는 경우
                if not(nx == shark_x and ny==shark_y): #상어가 있는 칸이 아닌경우
                    #물고기 이동(값 변경)
                    array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                    array[x][y][1], array[nx][ny][1] = array[nx][ny][1], dir
                    break
            #상어가 있거나, 경계 값 밖에 있다면 45도 반시계 방향으로 돌리기
            dir = (dir+1)%8

def dfs(array, x, y, total):  #배열, 상어 위치, 총 합.
    global answer
    array = copy.deepcopy(array)

    # 해당 위치 물고기 먹기
    number = array[x][y][0]
    array[x][y][0] = -1

    #물고기 이동.
    move_fish(array,x,y)

    #상어 이동할 수 있는 후보 확인
    result = shark_move(array,x,y)

    #해당 먹이 먹는 모든 과정 탐색.
    answer = max(answer, total+number)
    for next_x, next_y in result:
        dfs(array,next_x,next_y,total+number)

temp = [list(map(int, input().split())) for _ in range(4)]
array = [[None] * 4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        array[i][j] = [temp[i][j * 2], temp[i][j * 2 + 1] - 1]
answer = 0
dfs(array, 0, 0, 0)
print(answer)
