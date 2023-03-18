import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
#돌- 1개 or 3개를 가져라 수 있고, 게임은 상근이 먼저, 마지막 돌을 가져가는 사람은?
n = int(input())
dp = [-1]*1001
dp[1]=1  #1번째 상근
dp[2]=0  #2번째 상근
dp[3]=1  #3번째 상근

for i in range(4,n+1):
    #직전이나 3개 전이 상근이라면 다음은 창영.
    if dp[i-3]==1 or dp[i-1]==1:
        dp[i]=0
    else:
        dp[i]=1

print('CY' if dp[n] == 0 else 'SK')