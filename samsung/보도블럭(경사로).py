import sys
sys.stdin = open("input.txt","r")
'''
문제
* n*n크기의 인도 - 각 칸에는 높이
* 경사로 설치 (높이:1,길이:L)
- 높이 정확히 1 차이 나는 보도블럭에 설치, 낮은 칸에 설치
- 경사로 길이 L만큼 바닥에 접촉해야함.  
- 경사로를 이용해 지나갈 수 있는 열과 행의 총 개수를 구하라.

접근 법:
1. 인접한 곳의 높이 차가 2이상인 곳이 있는지 확인 -> 불가
2. 경사로를 놓아야할 곳 확인 -> 경사로 놓일 때마다 칸에 개수 +1
3. 직각 삼각형이 필요한 곳 찾기 -> 
   - 인접한 곳 높이 차:1, 왼쪽 값이 더 큰 경우.
   L만큼 여유 공간이 잇는지 확인. 
   왼쪽 공간이 i라면 i+1, i+L구간에 경사로를 놓는다.
   i+1,i+L구간에 전부 같은 숫자 놓여있는지 확인.
   
   - 인접한 곳 높이 차:1, 오른쪽 값이 더 큰 경우.
   L만큼 여유 공간이 잇는지 확인.
   왼쪽 공간이 i라면 i-L, i-1구간에 경사로를 놓아야함.
   i-L,i-1구간에 전부 같은 숫자 놓여있는지 확인.

   놓아야하는 경사로끼리 겹쳐있는지 확인- 각 칸에 2번이상 놓여있는지 확인.
'''
n, L = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
arr = [0 for _ in range(n)]

#각 칸마다 경사로가 몇번씩 놓여있는지 기록. - 경사로 겹치는걸 확인하기 위해 필요.
ramp_cnt = [0 for _ in range(n)]

#arr의 [l,r] 구간에 있는 원소가 전부 동일한지 확인.
def all_same(l,r):
    return len(set(arr[l:r+1]))==1

# 해당 arr가 지나갈 수 있는 경우인지 확인합니다.
def can_pass():
    global ramp_cnt

    #step1. 인접한 곳의 높이 차가 2이상인지 확인
    for i in range(n-1):
        if abs(arr[i]-arr[i+1])>=2:
            return False

    #각 위치마다 경사로 개수 0으로 초기화
    ramp_cnt = [0 for _ in range(n)]

    #step2-1. 경사로 확인하기.
    #직각 삼각형이 필요한 곳 찾기(왼쪽이1 높은곳)
    for i in range(n-1):
        if arr[i]==arr[i+1]+1:
            #L만큼의 여유공간이 있나
            if i+L>=n:
                return False

            #경사로가 놓일 곳의 높이가 전부 같은지 확인.
            if not all_same(i+1,i+L):
                return False

            #경사로 놓이는 곳에 개수 갱신
            for j in range(i+1,i+L+1):
                ramp_cnt[j]+=1


    #step2-2. 경사로 확인하기
    #직각 삼각형이 필요한 곳 찾기(오른쪽이 1높은 곳)
    for i in range(1,n):
        if arr[i]==arr[i-1]+1:
            #L만큼의 여유공간이 있나.
            if i-L<0:
                return False

            if not all_same(i-L,i-1):
                return False

            # 경사로 놓이는 곳에 개수 갱신
            for j in range(i-L,i):
                ramp_cnt[j]+=1

    #step3. 경사로 겹쳐있는지 확인.
    if any([cnt >=2 for cnt in ramp_cnt]):
        return False

    #모든 조건을 만족했다면 가능한 경우
    return True

ans =0

#row 번째 행이 지나갈 수 있는지 확인
for row in range(n):

    # 확인하고 싶은 수열을 입력.
    for col in range(n):
        arr[col] = grid[row][col]

    #지나갈 수 있으면 답 갱신
    if can_pass():
        ans+=1

#column번째 열이 지나갈 수 있는 곳인지 확인.
for col in range(n):

    #확인하고 싶은 수열 입력.
    for row in range(n):
        arr[row]=grid[row][col]

    #지나갈 수 있다면 답 갱신
    if can_pass():
        ans+=1

print(ans)
