import sys
sys.stdin = open("input.txt","r")

'''
계단 오르기 규칙
1. 한번에 한 계단씩, 두 계단씩 오를 수 있음. 
2. 연속으로 세 계단 못 밟음.
3. 시작점은 계단에 포함x, 마지막 도착 계단 꼭 밟기.

얻을 수 있는 총 점수의 최댓 값 구하기
'''

#계단 개수(~300)
n = int(input())
stair = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    stair[i] = int(input())

#1~3번째 계단 입력
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])

#4번째~n-1번째 입력
for i in range(3, n):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[n - 1])