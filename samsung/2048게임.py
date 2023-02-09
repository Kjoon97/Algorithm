import sys

sys.stdin = open("input.txt","r")

NUM_MOVES = 5
NONE = -1

# 변수 선언 및 입력
n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]
temp = [[0 for _ in range(n)] for _ in range(n)]

move_dirs = [0 for _ in range(NUM_MOVES)]
ans = 0

#격자 최댓값 구하기.
def get_max_block_num():
    return max([grid[i][j] for i in range(n) for j in range(n)])

# 아래로 숫자 떨어뜨리기
def drop():
    #next_grid를 0으로 초기화한다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j]=0

    #아래 방향으로 떨어뜨린다.
    for j in range(n):

        # 같은 숫자끼리 단 한번만 합치기 위해 떨어뜨리기 전에 숫자 하나를 keep해줍니다.
        keep_num, next_row = None, n-1

        for i in range(n-1,-1,-1):
            if not grid[i][j]:
                continue

            # 아직 떨어진 숫자가 없다면, 갱신해줍니다.
            if keep_num == None:
                keep_num = grid[i][j]

            # 가장 최근에 관찰한 숫자가 현재 숫자와 일치한다면 하나로 합쳐주고, keep 값을 비워줍니다.
            elif keep_num == grid[i][j]:
                next_grid[next_row][j] = keep_num*2
                keep_num= None
                next_row-=1

            # 가장 최근에 관찰한 숫자와 현재 숫자가 다르다면
            # 최근에 관찰한 숫자를 실제 떨어뜨려주고, keep 값을 갱신해줍니다.
            else:
                next_grid[next_row][j] = keep_num
                keep_num= grid[i][j]
                next_row-=1


        # 전부 다 진행했는데도 keep 값이 남아있다면 실제로 한번 떨어뜨려줍니다.
        if keep_num != None:
            next_grid[next_row][j] = keep_num
            next_row-=1

    # next_grid를 grid에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]



#격자 시계 방향으로 90도 회전.
def rotate():
    #next grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j]=0

    #90도 회전
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n-j-1][i]

    #next grid -> gird
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

#아래,오,위,왼 - 0,1,2,3
def tilt(move_dir):

    #move_dir수 만큼 시계방향으로 반복 회전->해당 방향이 아래쪽으로 향하도록
    for _ in range(move_dir):
        rotate()  #90도 회전.

    #아래 방향으로 떨어뜨리기.
    drop()

    #회전했던 것 복원
    for _ in range(4-move_dir):
        rotate()



def search_max_num(cnt):
    global ans

    if cnt == NUM_MOVES:
        # 시뮬 전 상황을 저장
        for i in range(n):
            for j in range(n):
                temp[i][j] = grid[i][j]

        # 각 방향으로 기울이기 진행
        for move_dir in move_dirs:
            tilt(move_dir)

        ans = max(ans, get_max_block_num())

        # 시물 전으로 상황 복원.
        for i in range(n):
            for j in range(n):
                grid[i][j] = temp[i][j]

        return

    for i in range(4):
        move_dirs[cnt]=i  #각 분기별로 방향 저장.
        search_max_num(cnt+1)

search_max_num(0)
print(ans)