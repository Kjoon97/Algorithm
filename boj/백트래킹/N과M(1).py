import sys

sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())

ans = [0] * m
check =[0]*(n+1)


def dfs(l):
    if l == m:
        for a in ans:
            print(a, end=" ")
        print()
        return
    else:
        for i in range(1,n+1):
            if check[i]==0:
                check[i]=1
                ans[l]=i
                dfs(l+1)
                ans[l]=0
                check[i]=0

dfs(0)
