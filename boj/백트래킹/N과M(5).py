import sys

sys.stdin = open("input.txt","r")
n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
indx =[]
def dfs(l):
    if l==m:
        for i in indx:
            print(nums[i], end=" ")
        print()
        return
    else:
        for i in range(n):
            if i not in indx:
                indx.append(i)
                dfs(l+1)
                indx.pop()

dfs(0)

'''
다른 방법:
nums.sort()
check =[0]*n
indx =[]
def dfs(l):
    if l==m:
        print(' '.join(map(str,indx)))
        return
    else:
        for i in range(n):
            if check[i]==0:
                check[i]=1
                indx.append(nums[i])
                dfs(l+1)
                indx.pop()
                check[i]=0

dfs(0)
'''