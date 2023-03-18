import sys
sys.stdin = open("input.txt","r")

'''
n<=10^4
길이 n짜리 수열.
연속 된 수들의 부분 합 중 그 합 >=s, 가장 짧은 것. 
-> 투 포인터. 
#누적 값이 s보다 크면 개수를 따져주고 왼쪽 포인터 +1
#s보다 작으면 오른쪽 포인터+1
'''
n,s = map(int,input().split())
nums = list(map(int,input().split()))
left, right = 0,0
sum_ = nums[0]
ans =2147000000

while True:
    if sum_ <s:
        right+=1
        if right==n:
            break
        sum_+=nums[right]
    else:
        sum_-=nums[left]
        ans = min(ans, right-left+1)
        left+=1

print(ans if ans!=2147000000 else 0)
