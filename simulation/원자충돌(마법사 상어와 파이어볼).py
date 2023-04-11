import sys
sys.stdin = open("input.txt")

'''
1. 문제.
격자: n*n, (모든 행,열 끝과 끝이 연결 되어 있음)
원자 수: m개
원자 - 질량,방향,속력,초기 위치. 방향(상하좌우,대각선)
x,y - 행,열.(1~n)
실험
    - 1. 모든 원자는 자신의 방향,속력으로 이동.(1초)
    - 2. 2개 이상의 원자가 한칸에 있으면 
        - 질량, 속력을 모두 합한 하나의 원자로 됨.
        - 4개의 원자로 나눠짐.
        - 질량//5 , 속력//합쳐진 원자 개수, 방향(상하좌우or대각선 중하나) -> 상하좌우, (상하좌우,대각선) ->대각선.
        - 질량 0인 원소는 소멸.
k 초가 될때 남아 있는 원자의 질량 합을 구하시오.
2. 입력:
    n: 격자 크기, m:원자의 개수, k:실험 시간
    x,y: 위치, m:질량, s:속력, d:방향(0~7)
'''
n,m,k = tuple(map(int,input().split()))
grid = [[[] for _ in range(n)] for _ in range(n)]
next_grid = [[[] for _ in range(n)] for _ in range(n)]


#입력
for _ in range(m):
    x,y,m,s,d = map(int,input().split())
    grid[x-1][y-1].append((m,s,d))

#
def split(x,y):
    sum_mass, sum_v =0,0
    num_dir_types =[0,0]
    atom_cnt = len(next_grid[x][y])

    for w,v,move_dir in next_grid[x][y]:
        sum_mass+=w
        sum_v+=v
        num_dir_types[move_dir%2]+=1

    start_dir=-1
    #전부 상하좌우 방향이거나, 전부 대각선 방향이면 상하좌우 방향 갖기
    if num_dir_types[0]==0 or num_dir_types[1]==0:
        start_dir=0
    else:
        start_dir=1

    for move_dir in range(start_dir,8,2):
        if sum_mass//5>0:
            grid[x][y].append((sum_mass//5, sum_v//atom_cnt, move_dir))

def compound():
    #grid 초기화
    for i in range(n):
        for j in range(n):
            grid[i][j]=list()

    #합성을 진행한다.
    for i in range(n):
        for j in range(n):
            atom_cnt = len(next_grid[i][j])
            if atom_cnt==1:
                grid[i][j].append(next_grid[i][j][0]) # 한개의 원소가 들어있는 리스트에서 원소 하나
            elif atom_cnt>1:
                split(i,j)

def next_pos(x,y,s,d):
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]

    # 움직인 이후 값이 음수가 되는 경우, 이를 양수로 쉽게 만들기 위해서
    # n의 배수이며 더했을 때 값을 항상 양수로 만들어 주는 수인 ns를 더해주면 됨.
    nx = (x+dxs[d]*s + n*s)%n
    ny = (y+dys[d]*s + n*s)%n

    return (nx,ny)


def move_all():
    for i in range(n):
        for j in range(n):
            for m,s,d in grid[i][j]:
                nx,ny = next_pos(i,j,s,d)
                next_grid[nx][ny].append((m,s,d))


def simulate():
    #next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j]=list()

    #원소 이동
    move_all()

    #합성, 그 결과를 grid에 저장한다.
    compound()


for _ in range(k):
    simulate()

ans = sum([weight for i in range(n) for j in range(n) for weight,_,_ in grid[i][j]])
print(ans)