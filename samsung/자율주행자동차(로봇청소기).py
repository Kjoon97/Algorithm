import sys
sys.stdin = open("input.txt","r")

'''
문제:
* n*m 도로에 1*1 자동차
* 자동차 동작 규칙
  - 1.현재 방향에서 왼쪽을 간적 없으면 좌회전 후 1칸 전진
  - 2. 왼쪽이 인도 or 이미 방문했으면 다시 좌회전 후 1번 시도.
  - 3. 4방향 모두 확인했으나 전진 못하면 방향 유지한 채 한칸 후진, 1번 시도
  - 4. 뒷 공간이 인도여서 후진 못하면 작동 멈춤.
* 자동차가 멈춘 뒤 거쳐 간 도로의 총 면적을 구하라.

입력:
* 도로 n*m
* 초기 위치: x,y 바라보는 방향: d(0~3) - 북동남서
* 도로 상태 0:도로, 1:인도
'''

n, m = map(int, input().split())
x, y, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
visited[x][y]=True
while True:

    if cnt==4:
        nx = x - dx[d]
        ny = y - dy[d]
        if grid[nx][ny]!=1:
            x = nx
            y = ny
            cnt = 0
        else:
            break

    cnt+=1
    d-=1
    if d<0:
        d+=4
    nx = x+dx[d]
    ny = y+dy[d]
    #갈 수 있을 경우
    if visited[nx][ny]==False and grid[nx][ny]!=1:
        visited[nx][ny]=True
        x=nx
        y=ny
        cnt=0

ans=0
for i in range(n):
    for j in range(m):
        if visited[i][j] == True:
            ans+=1

print(ans)