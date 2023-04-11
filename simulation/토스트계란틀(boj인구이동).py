import sys

sys.stdin = open("input.txt","r")

'''
1. 문제:
n*n개에 1*1크기의 계란 틀이 주어진다.
서로 맞대고 있는 두 계란의 양의 차이가 L<= <=R이면 선을 제거 - 계란 합치고, 동일하게 분리
계란의 이동이 더 이상 필요 없을 때까지 반복. 
계란 이동은 몇 번 일어날까

2. 입력 
n: 칸의 크기, L: 최솟 값, R: 최댓값
계란의 양

3. 출력
계란 이동의 총 횟수.
'''
from collections import deque
n,L,R = map(int, input().split())
egg = [list(map(int, input().split())) for _ in range(n)]
q=deque()
egg_group =[]
visited= [[False for _ in range(n)] for _ in range(n)]


def bfs():
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    # BFS 탐색을 수행합니다.
    while q:
        ex, ey = q.popleft()

        for i in range(4):
            nx, ny = ex + dx[i], ey + dy[i]

            # L, R 사이인 경우에만 합쳐질 수 있습니다.
            if 0<=nx<n and 0<=ny<n and L<=abs(egg[nx][ny] - egg[ex][ey])<=R and not visited[nx][ny]:
                q.append((nx, ny))
                egg_group.append((nx, ny))
                visited[nx][ny] = True

#조건에 맞게 계란의 양을 바꾼다.
def move_eggs():
    global egg_group

    #초기화
    for i in range(n):
        for j in range(n):
            visited[i][j]=False

    is_changed= False

    #아직 방문하지 못한 칸에 대해 bfs 탐색으로 합칠 계란찾기.
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                #합쳐질 계란 목록을 초기화
                egg_group=[]

                q.append((i,j))
                egg_group.append((i,j))
                visited[i][j]=True

                bfs()

                # 계란의 이동이 한번이라도 일어났는지를 확인
                if len(egg_group)>1:
                    is_changed=True

                #계란들 합침.
                sum_of_eggs = sum([egg[x][y] for x,y in egg_group])
                for x,y in egg_group:
                    egg[x][y] = sum_of_eggs//len(egg_group)

    return is_changed


# 이동이 더 이상 필요 없을 때까지 계란의 이동을 반복.
move_cnt=0
while True:
    is_changed = move_eggs()
    if not is_changed:
        break

    move_cnt+=1
print(move_cnt)