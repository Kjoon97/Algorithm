import sys
sys.stdin = open("input.txt","r")
'''
1.문제:
불: 매초씩 동서남북 방향으로 빈공간에 퍼짐.(벽 제외)
상근: 1초에 동서남북으로 이동 가능.(벽 통과x, 불이 옮겨진 칸x, 불 붙으려는 칸x)
      상근이가 있는 칸에 불이 올때, 동시에 다른 칸으로 이동 가능. 
2. 입력: 
t = 테스트 케이스 개수
w:가로, h:세로
 . :빈공간, #:벽, @:상근 시작 위치, *:불
3. 출력:
방 탈출하는데 최소 시간, 불가능할 경우->IMPOSSIBLE출력.
'''
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    while q:
        x, y = q.popleft()
        #불이 아닐 경우 숫자 저장.
        if visited[x][y] != "FIRE":
            flag = visited[x][y]
        # 불일 경우
        else:
            flag = "FIRE"

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #테두리 안의 경우.
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == -1 and (board[nx][ny] == "." or board[nx][ny] == "@"):
                    #불일 경우 다음 위치도 불.
                    if flag == "FIRE":
                        visited[nx][ny] = flag
                    #불이 아닐 경우 다음 위치는 숫자+1
                    else:
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            #테두리 밖으로 탈출하고 flag가 "FIRE"가 아니면
            else:
                if flag != "FIRE":
                    return flag + 1

    return "IMPOSSIBLE"


t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    q = deque()
    board = []
    visited = [[-1] * w for _ in range(h)]
    for i in range(h):
        board.append(list(input().strip()))
        for j in range(w):
            if board[i][j] == "@":
                visited[i][j] = 0
                start = (i, j)
            elif board[i][j] == "*":
                visited[i][j] = "FIRE"
                q.append((i, j))

    q.append(start)
    print(bfs())