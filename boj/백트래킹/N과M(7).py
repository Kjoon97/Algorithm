import sys
sys.stdin = open("input.txt","r")
n, m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans = []
def dfs(l,s):
    if l==m:
        for a in ans:
            print(a, end=" ")
        print()
        return
    else:
        for i in range(s,n):
            ans.append(nums[i])
            dfs(l+1,i)
            ans.pop()

dfs(0,0)