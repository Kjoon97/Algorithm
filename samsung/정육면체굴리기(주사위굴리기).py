import sys

sys.stdin = open("input.txt","r")

'''
문제:
* 0~9 그려진 n*m 격자판
* 주사위 - 각 면에는 0이 쓰임.굴리면서 면의 숫자가 변함, 격자 밖으로는 이동 못함 -> 밖으로 갈 경우 무시.굴리지x
* 격자 칸:0 - 주사위 바닥 면 -> 칸에 복사됨. 주사위는 변하지 않음
* 격자 칸:숫자 - 주사위 바닥면으로 복사됨. 해당 칸은 0이됨.
* 이동할 때마다 주사위 상단 면의 숫자를 출력하자.

입력:
격자판 n*m, 주사위 위치: x,y, 굴리기 횟수 k
격자 정보.
굴리기 방향 - 1:동,2:서,3:북,4:남
'''

FACE_NUM =6
OUT_OF_GRID =(-1,1)

n,m,x,y,k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
movements = list(map(int, input().split()))

#주사위 인덱스.
up, front, right = 1, 2, 3

# 주사위의 각 면마다 적혀 있는 숫자
dices = [0 for _ in range(FACE_NUM+1)]


def next_pos(x,y,move_dir):
    #동서북남:1,2,3,4
    dx,dy = [0,0,0,-1,1], [0,1,-1,0,0]
    nx,ny = x+dx[move_dir], y+dy[move_dir]

    #격자 안에 존재하면
    if 0<=nx<n and 0<=ny<m:
        return (nx,ny)
    else:
        return OUT_OF_GRID


def simulate(move_dir):
    global x,y
    global up, front, right

    #move_dir 방향으로 굴렸을 때의 격자상 위치 구하기
    nx, ny = next_pos(x,y,move_dir)

    #격자 밖으로 나가면 그냥 패스
    if (nx,ny) == OUT_OF_GRID:
        return

    #위치 이동.
    x,y = nx,ny

    if move_dir == 1:  # 동쪽
        up, front, right = 7-right, front, up
    elif move_dir == 2:  # 서쪽
        up, front, right = right, front, 7 - up
    elif move_dir == 3:  # 북쪽
        up, front, right = front, 7 - up, right
    else:  # 남쪽
        up, front, right = 7 - front, up, right

    #주사위 바닥 인덱스
    bottom = 7-up

    #격자 칸:0 - 주사위 바닥 면이 칸에 복사 됨
    if grid[x][y]==0:
        grid[x][y] = dices[bottom]
    #격자 칸:0x - 주사위 바닥면 으로 복사 됨. 해당 칸은 0이됨.
    else:
        dices[bottom] = grid[x][y]
        grid[x][y]=0

    print(dices[up])


#시뮬레이션 진행
for move_dir in movements:
    simulate(move_dir)
