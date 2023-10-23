import sys
sys.stdin = open("input.txt","r")

'''
1: 스위치 켜짐.
0: 스위치 꺼짐.
학생: 몇명 뽑아 1~스위치 개수 이하 자연수를 하나씩 나눠 줌.
     자신의 성별과 숫자에 따라 스위치 조작.
     남학생: 스위치 번호: 자기가 받은 수의 배수 -> 스위치 상태 바꿈.
     여학생: 자기가 받은 수와 같은 번호의 스위치 -> 좌우 대칭, 가장 많은 스위치 포함하는 구간 상태 바꿈.
     구간에 속한 스위치 개수 모두 홀수 됨.
입력:
스위치 개수(1~100)
스위치 상태
학생수 (1~100)
성별(1:남,2:여), 받은 숫자.
'''

n = int(input())
switch = [-1]+list(map(int,input().split())) # 스위치 상태 저장
m = int(input())

# 스위치 바꾸는 함수
def change(x):
    global switch
    switch[x] = abs(1-switch[x])

for _ in range(m):
    gender, number = map(int,input().split())

    #남자라면
    i=1
    if gender == 1:
        while i*number <= n:
            change(number*i)
            i+=1
    # 여자일 때
    elif gender ==2:
        change(number)
        while number-i > 0 and number+i <=n and switch[number-i] == switch[number+i]:
            change(number+i)
            change(number-i)
            i+=1

# 출력
for i in range(1, n+1):
    print(switch[i], end=" ")
    if i%20==0:
        print()