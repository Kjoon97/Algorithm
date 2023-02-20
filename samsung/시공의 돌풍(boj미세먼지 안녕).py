import sys
sys.stdin = open("input.txt","r")

'''
1. 문제:
- n*m 격자 방안에 먼지가 쌓여있음
- 시공의 돌풍 : 1번 열, 두 칸을 차지.
- 먼지 1초마다:
    1. 먼지가 인접한 4방향 상하좌우로 확산.
    2. 인접한 방향이 방의 범위를 벗어남 or 돌풍이 있으면 확산x
    3. 확산되는 양: 원래 칸의 먼지의 5를 나눈 몫, 원래 칸의 먼지 양은 확산된 만큼 줄어듦.
    4. 모든 먼지가 확산이 끝나면 해당 칸에 더해짐
- 시공의 돌풍:
    항상 1번 열에 설치되어 있으며 크기는 두 칸을 차지.
    1. 윗칸: 반시계 방향으로 바람, 아랫칸: 시계 방향으로 바람.
    2. 바람 불면 먼지는 모두 방향대로 모두 한 칸씩 이동.
    3. 시공의 돌풍으로 들어간 먼지는 사라짐.

2. 입력:
n,m: 방크기, t:시간

3. 출력:
t초 후 먼지 총 양
'''
# 변수 선언 및 입력:
n, m, t = tuple(map(int, input().split()))
dust = [list(map(int, input().split())) for _ in range(n)]
next_dust = [[0 for _ in range(m)] for _ in range(n)]

# (x, y)에서 인접한 4방향으로 확산이 일어납니다.
def spread(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    curr_dust = dust[x][y]

    # 인접한 4방향으로 확산이 일어납니다.
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        # 격자 안이면서, 시공의 돌풍이 없는 곳으로만 확산이 가능합니다.
        if 0<=nx<n and 0<=ny<m:
            if dust[nx][ny]!=-1:
                next_dust[nx][ny] += curr_dust // 5
                dust[x][y] -= curr_dust // 5


def diffusion():
    # next_dust 값을 0으로 초기화합니다.
    for i in range(n):
        for j in range(m):
            next_dust[i][j] = 0

    # 시공의 돌풍을 제외한 위치에서만 확산이 일어납니다.
    for i in range(n):
        for j in range(m):
            if dust[i][j] != -1:
                spread(i, j)

    # next_dust값을 확산 후 남은 dust에 더해줍니다.
    for i in range(n):
        for j in range(m):
            dust[i][j] += next_dust[i][j]


def counter_clockwise_roration(start_row, start_col, end_row, end_col):
    # Step1-1. 직사각형 가장 왼쪽 위 모서리 값을 temp에 저장합니다.
    temp = dust[start_row][start_col]

    # Step1-2. 직사각형 가장 위 행을 왼쪽으로 한 칸씩 shift 합니다.
    for col in range(start_col, end_col):
        dust[start_row][col] = dust[start_row][col + 1]

    # Step1-3. 직사각형 가장 오른쪽 열을 위로 한 칸씩 shift 합니다.
    for row in range(start_row, end_row):
        dust[row][end_col] = dust[row + 1][end_col]

    # Step1-4. 직사각형 가장 아래 행을 오른쪽으로 한 칸씩 shift 합니다.
    for col in range(end_col, start_col, -1):
        dust[end_row][col] = dust[end_row][col - 1]

    # Step1-5. 직사각형 가장 왼쪽 열을 아래로 한 칸씩 shift 합니다.
    for row in range(end_row, start_row, -1):
        dust[row][start_col] = dust[row - 1][start_col]

    # Step1-6. temp를 가장 왼쪽 위 모서리를 기준으로 바로 아래 칸에 넣습니다.
    dust[start_row + 1][start_col] = temp


def clockwise_rotation(start_row, start_col, end_row, end_col):
    # Step1-1. 직사각형 가장 왼쪽 위 모서리 값을 temp에 저장합니다.
    temp = dust[start_row][start_col]

    # Step1-2. 직사각형 가장 왼쪽 열을 위로 한 칸씩 shift 합니다.
    for row in range(start_row, end_row):
        dust[row][start_col] = dust[row + 1][start_col]

    # Step1-3. 직사각형 가장 아래 행을 왼쪽으로 한 칸씩 shift 합니다.
    for col in range(start_col, end_col):
        dust[end_row][col] = dust[end_row][col + 1]

    # Step1-4. 직사각형 가장 오른쪽 열을 아래로 한 칸씩 shift 합니다.
    for row in range(end_row, start_row, -1):
        dust[row][end_col] = dust[row - 1][end_col]

    # Step1-5. 직사각형 가장 위 행을 오른쪽으로 한 칸씩 shift 합니다.
    for col in range(end_col, start_col, -1):
        dust[start_row][col] = dust[start_row][col - 1]

    # Step1-6. temp를 가장 왼쪽 위 모서리를 기준으로 바로 오른쪽 칸에 넣습니다.
    dust[start_row][start_col + 1] = temp


def cleaning():
    windblast_rows = [
        i for i in range(n)
        if dust[i][0] == -1
    ]

    counter_clockwise_roration(0, 0, windblast_rows[0], m - 1)
    clockwise_rotation(windblast_rows[1], 0, n - 1, m - 1)

    # 돌풍 보정
    dust[windblast_rows[0]][0] = dust[windblast_rows[1]][0] = -1
    dust[windblast_rows[0]][1] = dust[windblast_rows[1]][1] = 0


def simulate():
    # 확산이 일어납니다.
    diffusion()
    # 시공의 돌풍이 청소를 진행합니다.
    cleaning()


# 총 t번 시뮬레이션을 진행합니다.
for _ in range(t):
    simulate()

ans = sum([dust[i][j] for i in range(n) for j in range(m) if dust[i][j] != -1])

print(ans)
