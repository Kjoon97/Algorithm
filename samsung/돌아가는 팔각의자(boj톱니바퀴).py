import sys
import copy
sys.stdin = open("input.txt","r")
'''
문제:
* 4개의 팔각의자가 주어짐.
* k번 회전
* n번째 의자가 회전 - n-1, n+1번째 의자에서 마주치는 사람의 출신이 다르면 다른방향으로 한번씩 회전
* 12시 방향에 앉은 남쪽 지방 사람의 여부

입력:
* 첫 번째 팔각의자 - 사람들 지역
* 두 번째 팔각의자 - 사람들 지역
* 세 번째 팔각의자 - 사람들 지역
* 네 번째 팔각의자 - 사람들 지역
(0:북쪽, 1:남쪽)
* k: 회전 횟 수
* n: 회전시킬 팔각 의자 번호, d: 방향(1:시계방향, -1:반시계방향)

출력:
* 1*s1 + 2*s2 + 4*s3 + 8*s4(착석시 s:1, 착석x s:0) 

먼저 각 의자 별 방향 값을 저장한다. 
시작점을 기준으로 방향을 넣고 앞뒤 방향으로 차례대로 지금 방향과 다르게 넣는다. 
'''
#의자별로 회전해야할 방향 저장합니다.
rotate_dir = [0 for _ in range(4)]

#이동(회전)
def shift(n, dir):
    chair = chairs[n]
    global a
    if dir ==1:
        temp = chair.pop()
        chair.insert(0,temp)
    else:
        temp = chair.pop(0)
        chair.append(temp)


#주어진 방향에서 반대 방향 반환.
def flip(curr_dir):
    if curr_dir==1:
        return -1
    else:
        return 1


def simulate(start_num, start_dir):
    global rotate_dir

    #step1. 각 의자마다 회전할 방향 구하기
    #회전값 초기화
    rotate_dir = [0 for _ in range(4)]

    #시작 위치 회전 방향 넣기.
    rotate_dir[start_num] = start_dir

    #좌측의 의자들의 회전 방향 정하기.
    for i in range(start_num-1,-1,-1):
        if chairs[i][2]!=chairs[i+1][6]:
            rotate_dir[i] = flip(rotate_dir[i+1])
        else:
            break

    #우측의 의자들의 회전 방향 정하기
    for i in range(start_num+1,4):
        if chairs[i][6]!=chairs[i-1][2]:
            rotate_dir[i] = flip((rotate_dir[i-1]))
        else:
            break

    #step2.회전시킴
    for i in range(4):
        if rotate_dir[i]!=0:
            shift(i,rotate_dir[i])


chairs = [list(map(int, input())) for _ in range(4)]

k = int(input())
for _ in range(k):
    start_num, start_dir = map(int, input().split())
    simulate(start_num-1,start_dir)

s1 = chairs[0][0]
s2 = chairs[1][0]
s3 = chairs[2][0]
s4 = chairs[3][0]

print(1*s1 + 2*s2 + 4*s3 + 8*s4)
