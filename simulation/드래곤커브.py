import sys
sys.stdin = open("input.txt",'r')
'''
1.문제:
드래곤 커브 - 복제 후 90도 시계방향으로 추가
만들어지는 정사각형의 개수를 구하라.
2. 입력:
* n: 드래곤 커브 개수
* 드래곤 커브 정보 - x,y:시작점, d:시작 방향, g:차수
* 방향-0,1,2,3: 오른쪽,위쪽,왼쪽,아래쪽
3. 출력:
크기가 1인 정사각형 개수 구하라
'''
GRID_SIZE=100
n = int(input())

# (x, y)점을 (center_x, center_y)를 기준으로 시계방향으로 90' 회전변환 했을 떄의 좌표값을 반환
def rotate(x, y, center_x, center_y):
    return (y - center_y + center_x, center_x - x + center_y)

#현재 드래곤 커브를 이루고 있는 점들의 위치를 나타내는 배열.
dragon_point = [[False for _ in range(GRID_SIZE+1)] for _ in range(GRID_SIZE+1)]

# 현재 세대에서 새롭게 그려지는 드래곤 커브 점들을 나타내는 배열
new_dragon_point = [[False for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]

# 최종적으로 그려지는 드래곤 커브들의 점들을 나타내는 배열
paper = [[False for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]

def simulate(center_x, center_y):

    #새로운 dragon point 값 초기화
    for i in range(GRID_SIZE+1):
        for j in range(GRID_SIZE+1):
            new_dragon_point[i][j]=False

    #드래곤 포인트 그리기.
    for i in range(GRID_SIZE+1):
        for j in range(GRID_SIZE+1):
            if dragon_point[i][j]:
                next_x, next_y = rotate(i,j,center_x,center_y)
                new_dragon_point[next_x][next_y] = True

    #새로운 드래곤 포인트들을 현재 dragon point에 추가.
    for i in range(GRID_SIZE+1):
        for j in range(GRID_SIZE+1):
            if new_dragon_point[i][j]:
                dragon_point[i][j]=True


def draw_dragon_curve(x,y,d,g):
    #dragon_poin값을 초기화
    for i in range(GRID_SIZE+1):
        for j in range(GRID_SIZE+1):
            dragon_point[i][j]=False

    dxs, dys = [0,-1,0,1], [1,0,-1,0]

    #0차 드래곤 커브 만들기
    start_x = x
    start_y =y
    end_x =x+dxs[d]
    end_y =y+dys[d]

    dragon_point[start_x][start_y] = True
    dragon_point[end_x][end_y] = True

    #g번에 걸쳐 드래곤 커브 확장
    for _ in range(g):
        simulate(end_x, end_y)
        end_x,end_y = rotate(start_x, start_y, end_x, end_y)

    #g차 드래곤 커브 점들을 paper에 전부 표시
    for i in range(GRID_SIZE+1):
        for j in range(GRID_SIZE+1):
            if dragon_point[i][j]:
                paper[i][j] = True

for _ in range(n):
    x,y,d,g = map(int, input().split())
    draw_dragon_curve(x,y,d,g)

ans = sum([
    1
    for i in range(GRID_SIZE)
    for j in range(GRID_SIZE)
    if paper[i][j] and paper[i][j + 1]
    and paper[i + 1][j] and paper[i + 1][j + 1]
])

print(ans)