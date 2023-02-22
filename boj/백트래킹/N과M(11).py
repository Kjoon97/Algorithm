import sys
sys.stdin = open("input.txt","r")

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

ans =[]

def dfs(l):
    if l==m:
        print(*ans)
        return
    remember_me=0
    for i in range(n):
        if remember_me!=nums[i]:
            remember_me=nums[i]
            ans.append(nums[i])
            dfs(l+1)
            ans.pop()

dfs(0)