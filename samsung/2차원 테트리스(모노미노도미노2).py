import sys
sys.stdin = open("input.txt", "r")
'''
입력:
    블록을 입력한 횟수: k
    블록 정보 t:블록 종류, x,y:블록의 위치
출력:
    점수
    빨간 보드, 노란 보드에 있는 블록이 차지하는 칸의 개수 합 출력.
'''
tc = int(input())
b = [[0]*6 for _ in range(4)]
g = [[0]*4 for _ in range(6)]

ans =0

def remove_green(idx):
    for i in range(idx,0,-1):
        for j in range(4):
            g[i][j] = g[i-1][j]
    for j in range(4):
        g[0][j]=0

def check_green():
    global ans
    for i in range(2,6):
        cnt=0
        for j in range(4):
            if g[i][j]:
                cnt+=1
        if cnt==4:
            remove_green(i)
            ans+=1

# 입력 받은 열부터 1열까지 한 칸씩 이전 열값을 옮겨오는 작업을 한다.0번째 열은 0으로 초기화.
def remove_blue(idx):
    for j in range(idx,0,-1):
        for i in range(4):
            b[i][j] = b[i][j-1]
    for i in range(4):
        b[i][0]=0

# 반복문으로 각 열을 탐색하면서 블럭이 몇개 있는지 cnt 변수로 센다
#cnt가 4면 해당 열이 블럭을 꽉 찼으므로 remove_blue에 j 열을 넣어 실행한 후, 제거한 횟수를 세는 ans를 늘린다
def check_blue():
    global ans
    for j in range(2,6):
        cnt=0
        for i in range(4):
            if b[i][j]:
                cnt+=1
        if cnt==4:
            #열 삭제
            remove_blue(j)
            ans+=1

def move_blue(t,x):
    y=1
    if t==1 or t==2:
        # 다음칸이 보드 범위를 벗어나거나 이미 블럭이 있을때까지 y값을 증가시킨다
        while True:
            if y+1 > 5 or b[x][y+1]:
                b[x][y]=1
                if t==2:
                    b[x][y-1]=1
                break
            y+=1
    else:
        # t가 3이면 (x+1, y+1) 칸이 블럭이 있을 경우도 추가해서 y값을 증가시킨다
        while True:
            if y+1>5 or b[x][y+1] or b[x+1][y+1]:
                b[x][y], b[x+1][y] = 1,1
                break
            y+=1

    #제거할 블럭이 있는지 확인
    check_blue()

    #0,1번째 열에 블럭 있는지 확인. 있으면 맨 마지막 열을 제거하고 한칸씩 땡겨진 보드로 만든다.
    for j in range(2):
        for i in range(4):
            if b[i][j]:
                remove_blue(5)
                break

def move_green(t,y):
    x=1
    if t==1 or t==3:
        while True:
            if x+1>5 or g[x+1][y]:
                g[x][y]=1
                if t==3:
                    g[x-1][y]=1
                break
            x+=1
    else:
        while True:
            if x+1>5 or g[x+1][y] or g[x+1][y+1]:
                g[x][y], g[x][y+1] = 1,1
                break
            x+=1

    check_green()

    for i in range(2):
        for j in range(4):
            if g[i][j]:
                remove_green(5)
                break

for _ in range(tc):
    t,x,y = map(int,input().split())
    move_blue(t,x)   #파란색 보드- 동일 행으로 떨어짐.
    move_green(t,y)  #초록색 보드 - 동일 열로 떨어짐

cnt_b, cnt_g = 0,0

#파란색 보드 위 블록 세기.
for i in range(4):
    for j in range(2,6):
        if b[i][j]:
            cnt_b+=1

#초록 색 보드 위 블록 세기
for i in range(2,6):
    for j in range(4):
        if g[i][j]:
            cnt_g+=1

print(ans)
print(cnt_b+cnt_g)


'''
1. 4x6 크기의 파란색 보드와 6x4크기의 초록색 보드를 만든다

  이후로는 풀이 과정이 똑같기 때문에 파란색 보드에 대한 풀이만 설명

2. t, x, y를 입력받고 move_blue에 t와 x를 입력해서 블록을 이동시킨다.

  파란색 보드의 경우 x 좌표는 고정이기 때문에 x 값만 입력한다. (초록색 보드는 반대)

3. move_blue에서는 우선 t가 1, 2인 경우와 3인 경우를 나눠서 처리한다.

  - t가 1이나 2일 때는 다음칸이 보드 범위를 벗어나거나 이미 블럭이 있을때까지 y값을 증가시킨다

   블럭을 놓을 좌표를 찾으면 1로 바꿔주고, t가 2이면 (x, y-1) 좌표도 1로 바꿔준다

  - t가 3이면 (x+1, y+1) 칸이 블럭이 있을 경우도 추가해서 y값을 증가시킨다

   블럭을 놓을 좌표를 찾으면 (x, y)와 (x+1, y) 칸을 1로 바꿔준다

4. 제거할 블럭이 있는지 확인하는 check_blue를 실행한다

5. check_blue에서는 반복문으로 각 열을 탐색하면서 블럭이 몇개 있는지 cnt 변수로 센다

   cnt가 4면 해당 열이 블럭을 꽉 찼으므로 remove_blue에 j 열을 넣어 실행한 후, 제거한 횟수를 세는 ans를 늘린다

6. remove_blue에서는 입력 받은 열부터 1열까지 한 칸씩 이전 열값을 옮겨오는 작업을 한다.

   0번째 열은 0으로 초기화한다.

7. check_blue가 끝나면 0, 1번째 열에 블럭이 있는지 확인한다.

   블럭이 있으면 remove_blue에 5를 입력해서 맨 마지막 열을 제거하고 한칸씩 땡겨진 보드로 만든다.

8. 모든 과정이 끝나면 파란색보드, 초록색보드에 있는 블럭을 세고 정답을 출력한다.  
'''