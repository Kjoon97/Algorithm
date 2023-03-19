import sys
sys.stdin = open("input.txt","r")

'''
연산을 사용 하는 횟수의 최솟 값은? -> dp 사용
'''
n = int(input())
dp = {1:0} # 현재 수:연산 횟수. - 1이 1이 되기 위해서는 연산 안해도 되니깐 0

for i in range(2,n+1):
    dp[i]=dp[i-1]+1 #1을 빼는 연산 ->1회 진행.
    if i%2==0:  #2로 나누는 연산
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)

print(dp[n])
