import sys
sys.stdin = open("input.txt","r")
'''
n개로 된 수열, i~j까지의 합(연속 합) 이 M이 되는 경우의 수를 구하자. 
n(10^5)
연속이고 시간 복잡도 빡세면 투포인터 쓰자.
'''
n,m = map(int,input().split())
left=0
right=0
nums = list(map(int,input().split()))
cnt=0
while right<=n:
    total = sum(nums[left:right])
    if total==m:
        cnt+=1
        right+=1
    elif total < m:
        right+=1
    else:
        left+=1

print(cnt)