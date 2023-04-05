import sys
sys.stdin = open("input.txt","r")

'''
1. 문제:
    특수영양제는 나무를 +1해준다.
    격자의 모든 행, 열은 각 끝이 연결 되어 있음
    1년 규칙:
        1. 특수 영양제 이동
        2. 대각선으로 인접한 방향에 높이가 1이상인 것이 있는 만큼 높이 성장. 
        3. 특수 영양제 투입한 것 제외하고 높이가 2 이상인 것은 높이 2를 컷, 해당 위치에 영양제 올리기.
    반복.
    남아 있는 나무 높이 총합 구하기.

2. 입력:
    n:격자 크기, 나무 키우는 총 년수: m년
    서로 다른 나무 높이 주어짐.
    이동 규칙(d:이동 방향(1~8), 이동 칸수:p) 
'''
n, m = map(int,input().split())
height = [list(map(int,input().split())) for _ in range(n)]
nutrient = [[False for _ in range(n)] for _ in range(n)]
next_nutrient =[[False for _ in range(n)] for _ in range(n)]

# 문제에서 주어진 순서대로 → ↗ ↑ ↖ ← ↙ ↓ ↘
dxs = [0, -1, -1, -1,  0,  1, 1, 1]
dys = [1,  1,  0, -1, -1, -1, 0, 1]


# 기존 특수 영양제는 없애주고 새로운 특수 영양제는 추가해주기.
def determine_nutrient():
    for i in range(n):
        for j in range(n):
            if nutrient[i][j]:
                nutrient[i][j]=False

            elif height[i][j]>=2:
                height[i][j]-=2
                nutrient[i][j]=True

def get_dig_cnt(x,y):
    cnt=0
    for i in range(1,8,2):
        nx = x+dxs[i]
        ny = y+dys[i]
        if 0<=nx<n and 0<=ny<n and height[nx][ny]>=1:
            cnt+=1

    return cnt

def diagonal_grow():
    for i in range(n):
        for j in range(n):
            if nutrient[i][j]:
                cnt = get_dig_cnt(i,j)
                height[i][j]+=cnt


def grow():
    for i in range(n):
        for j in range(n):
            if nutrient[i][j]:
                height[i][j]+=1


#격자의 모든 행,열은 각각 끝과 끝이 연결되어 있울경우 이동 구현.
def next_pos(x,y,d,p):
    nx = (x+ dxs[d]*p +n*p)%n
    ny = (y+ dys[d]*p + n*p)%n
    return (nx,ny)

def move(d,p):
    for i in range(n):
        for j in range(n):
            next_nutrient[i][j]=False

    for i in range(n):
        for j in range(n):
            if nutrient[i][j]:
                nx,ny = next_pos(i,j,d,p)
                next_nutrient[nx][ny] = True

    for i in range(n):
        for j in range(n):
            nutrient[i][j]=next_nutrient[i][j]

def simulate(d,p):
    #1. 영양제 이동
    move(d,p)

    #2.영양제 위치에 있던 나무 성장.
    grow()

    #3.대각선 방향의 높이가 1이상인 나무만큼 더 성장
    diagonal_grow()

    #4. 새로운 특수 영양제 추가, 기존 영양제 없애기
    determine_nutrient()


for i in range(n-2,n):
    for j in range(2):
        nutrient[i][j]=True

for _ in range(m):
    d,p = map(int,input().split())
    simulate(d-1,p)

def get_score():
    return sum([height[i][j] for i in range(n) for j in range(n)])
ans = get_score()
print(ans)