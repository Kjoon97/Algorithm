import sys
sys.stdin = open("input.txt", "r")

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
board = [list(list(input()))for _ in range(n)]
ans = 11

# 해당 문자가 맵에 남아있는지를 판단.
def exist(target):
    return any([target in row for row in board])

# 파란색이 맵에 남아있는지 판단합니다.
def blue_exist():
    return exist('B')


# 빨간색이 맵에 남아있는지 판단합니다.
def red_exist():
    return exist('R')

# (x, y)로 진행이 가능한지 판단합니다.
# 더 진행하기 위해서는 해당 위치에 벽이나 사탕이 없어야 합니다.
def can_go(x, y):
    return board[x][y] == '.' or board[x][y] == 'O'


# (x, y)에 있는 사탕을 move_dir 방향으로 최대한 끌어 내립니다.
def move(x, y, move_dir):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while True:
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        # 그 다음 위치가 가로막혀 있다면 더 이상 끌어 내리지 못합니다.
        if not can_go(nx, ny):
            break

        # 그 다음 위치가 출구라면 현재 사탕을 맵에서 지워주고 종료합니다.
        if board[nx][ny] == 'O':
            board[x][y] = '.'
            break

        # 그 다음 위치로 나아갈 수 있으므로 사탕을 한 칸 당겨줍니다.
        board[nx][ny] = board[x][y]
        board[x][y] = '.'
        # 사탕의 위치를 한 칸 이동시켜 줍니다.
        x, y = nx, ny


# move_dir 0, 1, 2, 3는 각각 상하좌우를 의미합니다.
def tilt(move_dir):
    # 상,좌 이동의 경우 위와 좌측 부분이 먼저 탐색.
    # 해당 방향으로 떨어지면 되기 때문에 행, 열이 모두 증가하는 방향으로
    # 묶어 같은 케이스로 처리가 가능합니다.
    if move_dir == 0 or move_dir == 2:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'R' or board[i][j] == 'B':
                    move(i, j, move_dir)

    # 하, 우 이동 역시 위와 비슷하게 반대 방향으로 묶어 처리.
    else:
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if board[i][j] == 'R' or board[i][j] == 'B':
                    move(i, j, move_dir)


# cnt번 기울였을 때의 상태입니다.
def find_min(cnt):
    global ans, board

    # 파란색이 구멍으로 빠져 맵에 존재하지 않는다면 실패 - 탐색 중단.
    if not blue_exist():
        return

    # 파란색은 맵에 남아있지만 빨간색은 구멍으로 빠져 맵에 존재하지 않는다면 성공, 더이상 탐색x
    if not red_exist():
        ans = min(ans, cnt)
        return

    # 이미 10번을 움직였는데도 성공하지 못했다면 탐색을 중단합니다.
    if cnt >= 10:
        return

    # 4 방향 중 한 방향을 정하여 움직입니다.
    for move_dir in range(4):
        # Tilt를 하면 a배열 상태가 바뀌게 되므로, tilt전 모양을 저장해 놓습니다.
        temp = [b[:]for b in board]

        # move_dir 방향으로 기울여 사탕을 떨어뜨립니다.
        tilt(move_dir)
        # 계속 탐색을 진행합니다.
        find_min(cnt + 1)

        # 탐색 후 퇴각하여 Tilt 전 상태로 복원하여 그 다음 방향으로도 동일한 기회를
        # 주도록 합니다.
        board = temp

print(board)
# backtracking을 이용해 최소 이동 횟수를 구합니다.
find_min(0)

# 10번 이내로 답을 구할 수 없다면
# -1을 답으로 넣어줍니다.
if ans == 11:
    ans = -1

print(ans)