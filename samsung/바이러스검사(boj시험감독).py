import sys

sys.stdin = open("input.txt","r")

'''
요구사항:
1. n개의 식당
2. 검사팀장(1명), 검사 팀원(여러명) - 팀장과 팀원이 검사할 수 있는 수 다름
3. 가게 당 팀장 한명은 꼭 필수.
4. 가게 당 팀장, 팀원 배치됨.
5. 필요한 검사자 최소 몇명?

입력:
1. n - 식당 수 (백만)  <= 10^6
2. 각 고객 수  <=  10^6
3. 팀장이 담당할 수 있는 고객 최대 수, 팀원이 담당 할 수 있는 고객 최대 수. <=  10^6
'''

#식당 수
n = int(input())
temp = []
cnt=0
#res
restaurantsCable = list(map(int, input().split()))

#담당 능력 수.
leaderCable, teamCable = map(int, input().split())

for rc in restaurantsCable:
    if rc < leaderCable:
        temp.append(0)
        cnt+=1
    else:
        temp.append(rc-leaderCable)
        cnt+=1

restaurantsCable = temp

for rc in restaurantsCable:
    if rc==0:
        continue
    elif rc<=teamCable:
        cnt+=1
    else:
        div = rc//teamCable
        re = rc%teamCable
        cnt+=div
        if re>0:
            cnt+=1

print(cnt)