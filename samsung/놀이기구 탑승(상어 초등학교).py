import sys
sys.stdin=open("input.txt","r")

"""
1. 문제
n*n 명의 학생을 n*n 격자 놀이기구에 탑승 (1~n)
각 학생 별로 좋아하는 학생 4명씩. 
탑승 조건:
    인접한 칸 중(격자 안) 좋아하는 친구가 많은 빈 칸으로 탑승(비어 있는 칸의 수가 가장 많은 위치)
    행, 열 번호가 가장 작은 위치로 이동.
각 학생마다 점수를 합한 점수 구하기

2. 입력:
n: 격자 크기
n0, n1, n2, n3, n4 (n0: 지금 탑승하는 학생, n1,n2,n3,n4 - n0이 좋아하는 학생)

3. 풀이:
완전탐색으로 각 학생의 이동 위치 구하기.(좋아하는 학생수, 빈칸수, -행번호, -열번호) 가장 큰 순으로 이동.
복잡한 우선 순위는 tuple로 처리.
각 위치에 대해 (좋아하는 친구 수, 비어있는 칸 수, 행 번호, 열 번호)를 전부 조사하는 완전 탐색 방식.
"""

EMPTY=0

n = int(input())
#탑승할 학생
target_num = [0 for _ in range(n*n+1)]

friends = [[False for _ in range(n*n+1)] for _ in range(n*n+1)]

rides = [[0 for _ in range(n+1)] for _ in range(n+1)]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

#우선 순위에 따라 쉽게 계산하기.  (좋아하는 친구 수, 빈 칸의 수, -행 번호, -열 번호)
def get_curr_cell(num,x,y):
    friend_cnt, blank_cnt =0,0
    for i in range(4):
        nx = x+dxs[i]
        ny = y+dys[i]
        if 1<=nx<=n and 1<=ny<=n:
            if rides[nx][ny]==EMPTY:
                blank_cnt+=1
            elif friends[num][rides[nx][ny]]:
                friend_cnt+=1
    return (friend_cnt, blank_cnt, -x, -y)



def move(num):
    #step1. 가장 우선순위가 높은 칸 선택.
    best_cell = (0,0,-(n+1),-(n+1))
    for i in range(1,n+1):
        for j in range(1,n+1):
            if rides[i][j]==EMPTY:
                curr= get_curr_cell(num,i,j)

                if best_cell <curr:
                    best_cell = curr

    #stpe2. 해당 위치에 탑승
    _, _, x,y = best_cell
    rides[-x][-y] = num

for i in range(1, n*n+1):
    student_data = list(map(int,input().split()))
    target_num[i] = student_data[0]
    for f in student_data[1:]:
        #현재 번호에 친구 번호 표시.
        friends[student_data[0]][f]=True


for i in range(1, n*n+1):
    move(target_num[i])

#(x,y)에 해당하는 학생의 점수 구하기
def get_score(x,y):
    cnt=0   #친구 수
    for i in range(4):
        nx = x+dxs[i]
        ny = y+dys[i]
        if 1 <= nx <= n and 1 <= ny <= n:
            if friends[rides[x][y]][rides[nx][ny]]:
                cnt+=1
    return int(10**(cnt-1))

print(sum([get_score(i,j) for i in range(1,n+1) for j in range(1,n+1)]))
