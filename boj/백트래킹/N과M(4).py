import sys

sys.stdin = open("input.txt","r")
n,m = map(int,input().split())
ans =[]
def dfs(s):
    if len(ans)==m:
        for a in ans:
            print(a, end=" ")
        print()
        return
    else:
        for i in range(s,n+1):
            ans.append(i)
            dfs(i)
            ans.pop()

dfs(1)