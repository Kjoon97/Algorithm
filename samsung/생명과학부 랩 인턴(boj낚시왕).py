import sys
sys.stdin = open("input.txt","r")

'''
1. 문제:
n*m 격자판에서 움직이는 곰팡이 채취.
채취 규칙
    - 빨간 숫자: 곰팡이 크기, 파란색 숫자: 속력
    - 첫번째 열부터 탐색
    - 위에서 아래서 탐색하면서 제일 빨리 발견한 곰팡이 채취 -> 채취하면 해당 칸은 빈칸.
    - 채취가 끝나면 곰팡이 이동(주어진 방향과 속력으로 이동. 벽에 도달하면 방향 바꿈.)
    - 모든 곰팡이가 이동 끝남 -> 한칸에 곰팡이가 두마리 이상일 경우 크기가 큰 곰팡이가 다른 곰팡이 모두 잡아먹음
    - 1초 끝. 다음 열로 이동.
2. 입력:
n,m: 격자판 크기, k:곰팡이 수
x,y:곰팡이 위치, s:1초 동안 곰팡이가 움직이는 거리, d:이동방향(1-위,2-아래,3-오,4-왼), b:크기
3. 출력:
채취한 곰팡이 크기의 총합을 구하라.
'''

n, m, k = tuple(map(int, input().split()))

BLANK = (-1, -1, -1)

mold = [[BLANK for _ in range(m)] for _ in range(n)]
next_mold = [[BLANK for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x,y,s,d,b = map(int,input().split())

    # 위, 아래 방향으로 움직이는 경우 2n - 2번 움직이면 다시 제자리로 돌아오게 되므로
    # 움직여야 할 거리를 2n - 2로 나눴을 때의 나머지 만큼만 움직이게 하면 최적화가 가능합니다.
    if d<=2:
        s%=(2*n-2)
    # 왼쪽, 오른쪽 움직이는 경우 마찬가지로 최적화.
    else:
        s%=(2*m-2)

    mold[x-1][y-1] = (b,s,d-1)

ans = 0
def collect(col):
    global ans
    for row in range(n):
        if mold[row][col]!=BLANK:
            size, _, _ = mold[row][col]

            ans+=size
            mold[row][col]=BLANK
            break

def get_next_pos(x,y,dist,dir):
    dx =[-1,1,0,0]
    dy =[0,0,1,-1]

    for _ in range(dist):
        nx =x+dx[dir]
        ny =y+dy[dir]

        # 현재 방향으로 이동했다 했을 때 만약 격자를 벗어나지 않는다면, 그대로 이동합니다.
        if 0 <= nx < n and 0 <= ny < m:
            x=nx
            y=ny
        #격자 벗어나면 방향 바꾸고 한 칸 이동
        else:
            #위 -> 아래, 오 -> 왼
            if dir%2==0:
                dir=dir+1
            #아래->위, 왼->오
            else:
                dir=dir-1
            x = x+dx[dir]
            y = y+dy[dir]

    return (x,y,dir)



def move(x,y):
    size, dist, dir = mold[x][y]
    nx, ny, nd = get_next_pos(x,y,dist,dir)

    new_mold = (size,dist,nd)

    if new_mold>next_mold[nx][ny]:
        next_mold[nx][ny]=new_mold

def move_all():

    #next_mold 초기화
    for i in range(n):
        for j in range(m):
            next_mold[i][j]=BLANK

    #곰팡이를 한번씩 이동
    for i in range(n):
        for j in range(m):
            if mold[i][j]!=BLANK:
                move(i,j)

    #next_mold 값을 mold에 옮겨주기
    for i in range(n):
        for j in range(m):
            mold[i][j]= next_mold[i][j]


def simulate(col):
    # 해당 열에 있는 곰팡이를 채취합니다.
    collect(col)
    # 곰팡이들을 전부 움직입니다.
    move_all()

#한 칸씩 이동하면서 곰팡이 채취
for col in range(m):
    simulate(col)


print(ans)