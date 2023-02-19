import sys
sys.stdin = open("input.txt", 'r')
n, m = map(int, input().split())
ans=[]
def dfs(l,s):
    if l==m:
        for a in ans:
            print(a, end=" ")
        print()
        return
    else:
        for i in range(s,n):
            ans.append(i+1)
            dfs(l+1,i+1)
            ans.pop()

dfs(0,0)