import sys
sys.stdin = open("input.txt",'r')
input = sys.stdin.readline
'''
1.문제:
* i번줄의 결과 - i번으로 나가야함.
* 데이터가 제대로 옮겨 지지 않는 경우 - 버그.
* 가로선: 취약지점.
* n: 고객의 수, 
* 해커들이 유실선 설치 - 승용: 유실선 추가 하여 버그 고치기.
* 유실선 겹치게 추가 불가.
2. 입력
* n: 고객의 수 , m: 유실선 개수, h: 취약지점 개수
* 유실선 정보 (a: 취약 지점, b: 유실이 일어난 지점(고객))
* 고객 번호 1번~
* 취약 지점 번호 1번~
3. 출력.
* 버그를 고치기 위한 유실선 최솟 값 구하기 
* 필요한 유실선이 3보다 큰 값이거나 고치는 것이 불가능하면 -1 출력.
'''
n, m, h = map(int, input().split())
line = [[False for _ in range(n+1)] for _ in range(h+1)]
for _ in range(m):
    a,b = map(int, input().split())
    line[a][b] = True

ans = 2147000000

#i번째 줄이 어디로 향하는지 기록.
num=[0 for _ in range(n+1)]

#i번째 출발점이 i번째 종료 점으로 가는지 확인
def possible():

    #유실선끼리 이어져있는 경우 불가
    if any([line[a][b] and line[a][b-1] for a in range(1,h+1) for b in range(2,n)]):
        return False

    #직접 어느 위치로 이동하는지 계산하기 위해 초깃값 설정
    for i in range(1, n+1):
        num[i]=i

    #유실 선이 있는 경우 해당 위치에 있는 고객의 번호 교환
    for a in range(1,h+1):
        for b in range(1,n):
            if line[a][b]:
                num[b], num[b+1] = num[b+1], num[b]

    # 전부 자기 자신으로 내려오는지 확인
    if any([num[i]!=i for i in range(1, n+1)]):
        return False

    return True



def find_min(curr_idx, cnt):
    global ans

    #추가한 유실선의 수가 이미 지금까지 구한 답보다 많다면 커팅.
    if cnt >= ans:
        return

    #가능한 조합이라면 답 갱신.
    if possible():
        ans = min(ans,cnt)

    #이미 3개를 뽑았거나, 더이상 뽑을게 없다면 퇴각.
    if cnt==3 or curr_idx==len(candidates):
        return

    #curr_idx 번째 유실선은 추가하지 않았을 경우
    find_min(curr_idx+1, cnt)

    #curr_idx 번째 유실선을 추가했을 경우
    a,b = candidates[curr_idx]
    line[a][b] = True
    find_min(curr_idx+1, cnt+1)
    line[a][b]= False

#처음 유실선 제외한 나머지 공간.(후보들)
candidates = [(i,j) for i in range(1,h+1) for j in range(1,n) if not line[i][j]]

find_min(0,0)

if ans == 2147000000:
    ans=-1

print(ans)




