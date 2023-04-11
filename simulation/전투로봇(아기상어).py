import sys
sys.stdin = open("input.txt","r")

'''
1. 문제:
    * n*n 격자에 m개 몬스터, 1개 전투로봇.
    * 한칸 당 몬스터 하나
    * 전투로봇
        - 초기 레벨:2
        - 상하좌우 이동.   
        - 자신의 레벨보다 큰 몬스터 지나칠 수 없음.
        - 자신의 레벨보다 낮은 몬스터만 없앨 수 있음.
        - 자신의 레벨이랑 같은 몬스터는 없애지 못함, 지나칠수는 있음.
    * 전투 로봇 이동 규칙
        - 없앨 수 있는 몬스터 있으면 -> 해당 몬스터를 없애러 간다. 
        - 없앨 수 있는 몬스터가 여러개-> 거리가 가장 가가운 몬스터 없앤다. (-> 거리 순)
        - 가장 위에 존재하는 몬스터, 가장 왼족에 존재하는 몬스터부터 없앤다.(-> 행, 열 순)
        - 없앨 수 있는 몬스터가 없으면 종료.
    * 로봇 한 칸 이동: 1초 걸림
    * 전투로봇이 목표 몬스터 칸에 도달하면 몬스터 없어짐.
    * 같은 수의 몬스터를 없애면 레벨 상승.
2. 입력:
    n: 격자판 크기(2~20)
    1~6: 몬스터 레벨, 9: 전투로봇.
3. 출력:
    일을 끝내기 전까지 걸린 시간 출력. 
'''
from collections import deque

n= int(input())
board = [list(map(int,input().split())) for _ in range(n)]

#현재 로봇 위치, 로봇 레벨, 현재 레벨에서 잡은 몬스터 수,
robot_pos = (-1,-1)
robot_level =2
caught_cnt =0
q= deque()
time=0
step =[[0 for _ in range(n)] for _ in range(n)]
visited =[[False for _ in range(n)] for _ in range(n)]
dy=[0,1,0,-1]
dx=[1,0,-1,0]

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j]=False

def bfs():
    while q:
        ex, ey = q.popleft()
        for i in range(4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] <= robot_level:
                visited[nx][ny] = True
                q.append((nx, ny))
                step[nx][ny] = step[ex][ey] + 1


# best 위치를 새로운 위치로 바꿔줘야 하는지를 판단
def need_update(best_pos, new_pos):
    # 첫 도달 가능한 몬스터인 경우라면 update가 필요합니다.
    if best_pos==(-1,-1):
        return True
    bx, by = best_pos
    nx, ny = new_pos

    # 거리, 행, 열 순으로 더 작은 경우에만 골라져야 합니다.
    return (step[bx][by], bx, by)>(step[nx][ny], nx, ny)


#가장 우선 순위가 높은 몬스터 있는 곳을 찾아 이동 시키기.
def move_robot():
    global robot_pos, robot_level, caught_cnt
    global time

    #방문 초기화
    initialize_visited()

    #step1. 로봇으로 부터 각각의 몬스터까지 최단 거리 구하기.
    robot_x, robot_y = robot_pos
    visited[robot_x][robot_y]=True
    step[robot_x][robot_y]=0
    q.append(robot_pos)
    bfs()

    #step2. 도달할 수 있는 몬스터들 중 가장 우선 순위가 높은 몬스터 위치 구하기.
    best_pos = (-1,-1)
    for i in range(n):
        for j in range(n):
            #도달이 불가능 or 몬스터 없음 or 레벨이 같은 경우 패스
            if not visited[i][j] or not board[i][j] or board[i][j] == robot_level:
                continue
            #도달 할 경우
            new_pos=(i,j)
            #위치 바꿔야할지 판단하고 best위치 선정.
            if need_update(best_pos, new_pos):
                best_pos= new_pos


    #도달 가능한 몬스터가 있다면 그쪽으로 로봇 이동.
    if best_pos != (-1,-1):
        bx,by = best_pos
        time+=step[bx][by]
        board[bx][by]=0
        robot_pos = best_pos
        caught_cnt+=1

        #몬스터를 로봇 레벨 만큼 잡게되면 레벨 1 증가.
        if caught_cnt==robot_level:
            robot_level+=1
            caught_cnt=0

        return True

    #도달 가능한 몬스터가 없다면 움직임 종료.
    else:
        return False



#처음 로봇 위치
for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            board[i][j]=0
            robot_pos=(i,j)


# 없앨 수 있는 몬스터가 없을 때까지 반복
while True:
    if not move_robot():
        break
print(time)
