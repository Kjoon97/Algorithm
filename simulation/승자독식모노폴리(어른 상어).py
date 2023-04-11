import sys
sys.stdin = open("input.txt","r")
'''
1. 문제:
    n*n 격자칸에서 게임 진행.
    m개의 플레이어, 
    1턴 당 플레이어 한 칸씩 이동, 칸 이동시 해당 칸 독점 계약.(초기 상태 위치도 독점한 상태)
    독점 계약 - k 턴 만큼 유효. 
    각 플레이어- 각 방향 별로 이동 우선 순위.
               아무도 독점하지 않은 칸. 없으면 -> 본인이 독점한 땅으로 이동.
               보고있는 방향 = 그 직전에 이동한 방향.
    모든 플레이어가 이동한 후 -> 한 칸에 여러 플레이어 있는 경우 가장 작은 번호의 플레이어만 살아남음. 
2. 입력: 
n:격자 크기, m: 플레이어 수, k:독점 계약 턴수
(격자 정보) 0: 빈칸, p: 플레이어
d: 각 플레이어 초기 방향 (1:위, 2: 아래, 3:왼쪽, 4:오른쪽)
플레이어의 방향에 대한 우선 순위, 
위를 향했을 때 이동 우선 순위
아래를 향했을 때 이동 우선 순위
왼쪽을 향했을 때 이동 우선 순위
오른 쪽을 향했을 때 이동 우선 순위

3. 출력
1번 플레이어만 남게 되기까지 걸린 턴의 수를 출력하자. 
'''
EMPTY_NUM =401
EMPTY = (401, 401)
# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))
given_map = [list(map(int, input().split())) for _ in range(n)]
next_dir = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(m + 1)]
player = [[EMPTY for _ in range(n)] for _ in range(n)]
next_player = [[EMPTY for _ in range(n)] for _ in range(n)]
contract = [[EMPTY for _ in range(n)] for _ in range(n)]

time = 0

def next_pos(x, y, curr_dir):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    num, _ = player[x][y]

    #1.먼저 독점계약을 맺지 않은 공간이 있다면 우선순위에 따라 그곳으로 이동
    for move_dir in next_dir[num][curr_dir]:
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        if 0 <= nx < n and 0 <= ny < n:
            if contract[nx][ny][0] == EMPTY_NUM:
                return nx, ny, move_dir

    #2.접한 곳이 모두 독점계약을 맺은 곳이라면 우선순위에 따라 그 중 본인이 독점계약한 땅으로 이동
    for move_dir in next_dir[num][curr_dir]:
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        if 0 <= nx < n and 0 <= ny < n:
            if contract[nx][ny][0] == num:
                return nx, ny, move_dir


def move(x, y):
    num, curr_dir = player[x][y]

    # Step1. 현재 플레이어의 다음 위치와 방향을 구합니다.
    nx, ny, move_dir = next_pos(x, y, curr_dir)

    # Step2. 플레이어를 옮겨줍니다. 새로 들어온 플레이어가 더 우선순위가 높을 경우에만 (x, y)위치에 해당 플레이어가 위치함. Empty인 위치에서는 401로 항상 update가 됨.
    if next_player[nx][ny] > (num, move_dir):
        next_player[nx][ny] = (num, move_dir)


def dec_contract(x, y):
    num, remaining_period = contract[x][y]

    # 남은 기간이 1이면 다시 Empty가 됩니다.
    if remaining_period == 1:
        contract[x][y] = EMPTY
    # 그렇지 않다면 기간이 1 줄어듭니다.
    else:
        contract[x][y] = (num, remaining_period - 1)


def add_contract(x, y):
    num, _ = player[x][y];
    contract[x][y] = (num, k)


def simulate():
    # Step1. next_player를 초기화.
    for i in range(n):
        for j in range(n):
            next_player[i][j] = EMPTY

    # Step2. 각 플레이어들을 한 칸씩 이동.
    for i in range(n):
        for j in range(n):
            if player[i][j] != EMPTY:
                move(i, j)

    # Step3. player next_player로 업데이트.
    for i in range(n):
        for j in range(n):
            player[i][j] = next_player[i][j]

    # Step4. 남은 contract기간을 1씩 감소.
    for i in range(n):
        for j in range(n):
            if contract[i][j] != EMPTY:
                dec_contract(i, j)

    # Step5. 새로운 contract를 추가.
    for i in range(n):
        for j in range(n):
            if player[i][j] != EMPTY:
                add_contract(i, j)


def end():
    #1000초 이상이면 true하고 종료.
    if time > 1000:
        return True

    #1번 플레이어말고 나머지 플레이어가 있다면 false.
    for i in range(n):
        for j in range(n):
            if player[i][j] == EMPTY:
                continue
            num, _ = player[i][j]
            if num != 1:
                return False

    return True


# 플레이어 마다 초기 방향을 입력받아 설정해줍니다.
init_dirs = list(map(int, input().split()))
for num, dir in enumerate(init_dirs, start=1):
    for i in range(n):
        for j in range(n):
            if given_map[i][j] == num:
                player[i][j] = (num, dir - 1)
                contract[i][j] = (num, k)

# 플레이어 마다 방향 우선순위를 설정합니다.
for num in range(1, m + 1):
    for curr_dir in range(4):
        dirs = list(map(int, input().split()))
        for i, dir in enumerate(dirs):
            next_dir[num][curr_dir][i] = dir - 1

# 시간이 1000이 넘지 않고
# 1번이 아닌 플레이어가 남아 있다면
# 계속 시뮬레이션을 반복합니다.
while not end():
    simulate()
    time += 1

if time > 1000:
    time = -1

print(time)
