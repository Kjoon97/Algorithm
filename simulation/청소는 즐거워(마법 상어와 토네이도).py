import sys
sys.stdin = open("input.txt","r")
'''
1. 문제:
    n*n격자(n-홀수) 정가운데는 먼지x
    왼,아래,오른쪽,위 순으로 이동하며 청소.
    먼지는 비율에 맞춰 이동.
    
2. 해설
    * 나선형으로 순회하기
    * 방향은 왼,아래,오른쪽 위, 순서로 변하고 
      각 방향에 대해서는 처음 1씩 이동하다가 방향이 오른쪽,왼쪽으로 바뀌게 될때
      동일한 방향에 대해 이동거리가 1씩 늘어남. (마지막 끝나는 부분은 제외)
    
    * 방향을 왼,아래,오른,위 순으로 변하게 하시 위해서는 해당 방향 순으로 
      dx,dy 값을 설정. dir=3 다음은 0이 되어야함. 다음 dir = (현재 dir+1)%4
      미리 방향마다 5*5격자에 떨어지는 먼지 비율 담는 배열을 활용해서 먼지양에 각 비율 곱해주기.
'''
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

#시작 위치, 방향, 이동할 횟수
curr_x, curr_y = n//2, n//2
move_dir=0
move_num=1
ans=0

#비율 순서: 왼,아래,오른,위
dust_ratio = [
    [
        [0,  0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5,  0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0,  0, 2, 0, 0]
    ],
    [
        [0,  0, 0,  0, 0],
        [0,  1, 0,  1, 0],
        [2,  7, 0,  7, 2],
        [0, 10, 0, 10, 0],
        [0,  0, 5,  0, 0]
    ],
    [
        [0, 0, 2,  0, 0],
        [0, 1, 7, 10, 0],
        [0, 0, 0,  0, 5],
        [0, 1, 7, 10, 0],
        [0, 0, 2,  0, 0]
    ],
    [
        [0,  0, 5,  0, 0],
        [0, 10, 0, 10, 0],
        [2,  7, 0,  7, 2],
        [0,  1, 0,  1, 0],
        [0,  0, 0,  0, 0]
    ]
]

# 격자 안이면 먼지 더하기, 밖이면 답에 더하기
def add_dust(x,y,dust):
    global ans
    if 0<=x<n and 0<=y<n:
        grid[x][y]+=dust
    else:
        ans+=dust

#한 칸 움직이며 청소 진행
def move():
    global curr_x, curr_y

    #왼,아래,오른,위 방향
    dxs = [0,1,0,-1]
    dys = [-1,0,1,0]

    #현재 curr 위치 계산
    curr_x = curr_x+dxs[move_dir]
    curr_y = curr_y+dys[move_dir]

    added_dust=0
    for i in range(5):
        for j in range(5):
            dust = grid[curr_x][curr_y]* dust_ratio[move_dir][i][j]//100
            add_dust(curr_x + i - 2, curr_y + j - 2, dust)
            added_dust +=dust

    #a%자리에 먼지를 추가
    add_dust(curr_x+dxs[move_dir], curr_y+dys[move_dir], grid[curr_x][curr_y]-added_dust)

def end():
    if curr_x==0 and curr_y==0:
        return True
    else:
        return False

while not end():
    # move_num 만큼 이동
    for _ in range(move_num):
        move()

        #이동하는 도중 (0, 0)으로 오게 되면, 움직이는 것을 종료
        if end():
            break

    #방향을 변경
    move_dir = (move_dir+1)%4

    #현재 방향이 오른쪽, 왼쪽이 되는 경우, 움직여야 할 횟수를 1 증가
    if move_dir == 0 or move_dir==2:
        move_num+=1

print(ans)
