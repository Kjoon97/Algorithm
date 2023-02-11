import sys
sys.stdin = open("input.txt","r")
input= sys.stdin.readline
'''
배추가 무더기 개수 구하기
1. 입력:
* T: 테스트 케이스
* m: 가로, n: 세로, k: 배추 개수

'''
from collections import deque
dy=[-1,0,1,0]
dx=[0,1,0,-1]
t = int(input())

def bfs(y,x):
    q = deque()
    q.append((y,x))
    board[y][x]=0

    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey+dy[i]
            nx = ex+dx[i]

            if 0<=ny<n and 0<=nx<m and board[ny][nx]==1:
                board[ny][nx]=0
                q.append((ny,nx))

for _ in range(t):
    m,n,k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        board[y][x]=1

    cnt=0
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                cnt+=1
                bfs(i,j)

    print(cnt)

