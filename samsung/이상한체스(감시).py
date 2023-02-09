import sys
sys.stdin = open("input.txt","r")
'''
1.문제:
* 말 - 4방향 중 한가지 방향을 선택, 
* n*m 체스판
* 말들의 방향을 설정 -> 갈 수 없는 격자 크기 최소화 하기
* 규칙:
    - 본인의 말 뛰어넘을 수 있음.
    - 상대편의 말은 뛰어넘을 수 없음 -> 상대편 말이 있는 격자는 세지 않는다.
2. 입력:
* n, m (1~8)
* 1~5: 자신의 말
* 6: 상대편 말. 

3. 출력:
* 자신의 말을 이용해서 갈수 없는 체스판의 영역의 최소 합 구하기.
'''

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
min_area = 2147000000
board = [ list(map(int, input().split())) for _ in range(n)]
chess_pieces = []
for i in range(n):
    for j in range(m):
        if 1<=board[i][j]<=5:
            chess_pieces.append((i,j))

# 말들의 방향을 표시합니다.
piece_dir = [[0 for _ in range(m)] for _ in range(n)]

# 자신의 말로 갈 수 있는 영역을 표시합니다.
visited = [[False for _ in range(m)] for _ in range(n)]

# 입력으로 주어진 방향에 대해
# 말의 종류마다 북동남서 방향으로
# 이동이 가능한지 표시합니다.
can_move = [
    [],
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]


# (start_x, start_y)에서 해당 타입의 말이 특정 방향을
# 바라보고 있을 때 갈 수 있는 곳들을 전부 표시합니다.
def fill(start_x, start_y, piece_num, face_dir):
    # 북동남서 순으로 방향을 설정합니다.
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(4):
        # 해당 말이 움직일 수 있는 방향인지를 확인, 움직일 수 없다면 pass
        if not can_move[piece_num][i]:
            continue

        # 갈 수 있다면, 끝날때까지 계속 진행,방향은 face_dir만큼 시계방향으로 회전했을 때를 기준으로 움직임.
        x, y = start_x, start_y
        move_dir = (i + face_dir) % 4;
        while True:
            visited[x][y] = True
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 6:
                x, y = nx, ny
            else:
                break


# n 개의 체스 말의 방향이 정해졌을 때 이동할 수 없는 영역의 넓이를 반환합니다.
def get_area():
    # visited 배열을 초기화합니다.
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0

    for x, y in chess_pieces:
        # 해당 말이 정해진 방향에 있을 때 갈 수 있는 곳들을 전부 표시합니다.
        fill(x, y, board[x][y], piece_dir[x][y])

    area=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and board[i][j]!=6:
                area+=1

    return area


def search_min_area(cnt):
    global min_area

    # 자신의 말들의 방향이 전부 결정되었을 때, 갈 수 없는 넓이를 계산하여 갱신합니다.
    if cnt == len(chess_pieces):
        min_area = min(min_area, get_area())
        return

    # cnt 말의 방향을 설정합니다.
    piece_x, piece_y = chess_pieces[cnt]

    for i in range(4):
        piece_dir[piece_x][piece_y] = i
        search_min_area(cnt + 1)


search_min_area(0)
print(min_area)