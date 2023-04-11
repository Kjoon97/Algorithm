import sys
sys.stdin = open("input.txt","r")
from collections import deque
NOT_EXISTS = (-1,-1)
'''
1.문제:
    배터리 양이 모두 소진 되는 경우 더 이상 움직일 수 없음.
    n*n 격자 위에 지나갈 수 없는 벽과 m 명의 승객의 위치가 주어짐.
    출발지로 이동 or 목적지로 이동 시 항상 최단 거리로 이동.
    한 칸 이동시 1만큼 배터리 소모, 
    승객을 목적지로 태워주면, 배터리 += (승객을 태우면서 소모한 배터리 양)*2
    이동 중 배터리 모두 소모 -> 즉시 종료. 
    승객이 여러명 -> 현위치와의 최단 거리가 가장 짧은 승객을 먼저 태움. 가장 위, 가장 왼쪽 순,
    해당 배터리로 모든 승객을 성공적으로 데려다 줄 수 있는지 확인, 최종적으로 남는 배터리 양 출력하기.
    
2. 입력:
    n:격자 크기, m:승객의 수, c:배터리 충전량.
    0: 도로, 1: 벽, 
    x,y - 자율 주행 전기차의 초기 위치.(1~n)
    x_s,y_s: 승객의 출발지 위치 정보(서로 다름)
    x_e,y_e: 도착지 위치 정보.
'''
#bfs로 자동차에서 승객까지의 최단 거리 계산. 그 후(거리,행,열) 순으로 가장 가까운 승객의 위치 구하고 자동차 이동.
n, m, r_battery = map(int,input().split())
grid = [[0 for _ in range(n+1)] for _ in range(n+1)]
moved_passenger =[False for _ in range(n*n)]
cars_pos =(-1,-1)
q = deque()
step = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    row = list(map(int,input().split()))
    for j, num in enumerate(row, start=1):
        grid[i][j] = num
#현재 위치
car_pos = tuple(map(int,input().split()))
passengers = [tuple(map(int,input().split())) for _ in range(m)]
visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]

def need_update(best_pos, new_pos):
    #첫 후보가 승객이라면 UPDATE
    if best_pos == NOT_EXISTS:
        return True
    best_x, best_y = best_pos
    new_x, new_y = new_pos

    #거리, 행, 열 순으로 더 작은 경우에만 골라져야함.
    return (step[best_x][best_y], best_x, best_y) > (step[new_x][new_y], new_x, new_y)

def initialized_visit():
    for i in range(1,n+1):
        for j in range(1,n+1):
            visited[i][j]= False


def bfs(start_pos):
    #방문 초기화
    initialized_visit()
    sx, sy = start_pos
    visited[sx][sy]= True
    step[sx][sy]=0
    q.append((sx,sy))

    dxs, dys = [0,1,0,-1], [1,0,-1,0]

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx+dxs[i]
            ny = cy+dys[i]
            if 1<=nx<n+1 and 1<=ny<n+1:
                if not visited[nx][ny] and not grid[nx][ny]:
                    q.append((nx,ny))
                    step[nx][ny] = step[cx][cy]+1
                    visited[nx][ny]= True


#가장 우선 순위 높은 승객 찾고 목적지로 이동시키기.
def move_passenger():
    global car_pos, r_battery

    #1. 자동차 위치에서 각 승객까지 최단 거리 구하기.
    #시작 위치부터 bfs 진행.
    bfs(car_pos)

    #2. 태울수 있는 승객 중 가장 우선 순위가 높은 승객 구하기.
    best_pos = NOT_EXISTS
    best_index = -1
    for i, (sx,sy,ex,ey) in enumerate(passengers):
        if moved_passenger[i] or not visited[sx][sy] or step[sx][sy] > r_battery:
            continue

        if need_update(best_pos,(sx,sy)):
            best_pos = (sx,sy)
            best_index = i

    #현재 연료로 태울수 있는 승객이 없다면 불가.
    if best_pos == NOT_EXISTS:
        return False

    #승객의 위치로 이동.
    sx, sy, ex, ey = passengers[best_index]
    car_pos = (sx,sy)
    r_battery -=step[sx][sy]

    #해당 승객을 이동시키기 위한 최단 거리 구하기.
    bfs((sx,sy))

    #도착점 도달 자체가 불가, 필요한 연료가 충분하지 않으면 불가.
    if not visited[ex][ey] or step[ex][ey] > r_battery:
        return False

    #이동 가능한 경우,
    car_pos = (ex,ey)
    r_battery -= step[ex][ey]

    moved_passenger[best_index]=True
    r_battery+= step[ex][ey]*2

    return True


#m명의 승객을 전부 옮길 수 있는지 판단.
for _ in range(m):
    is_moved = move_passenger()

    #전부 옮기는 것이 불가능한 경우 -1 출력, 프로그램 종료.
    if not is_moved:
        print(-1)
        exit(0)


print(r_battery)