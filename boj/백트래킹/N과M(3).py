import sys
sys.stdin = open("input.txt", 'r')
n, m = map(int, input().split())
ans = []

def dfs(l):
    if l==m:
        for a in ans:
            print(a, end=" ")
        print()
        return
    else:
        for i in range(1,n+1):
            ans.append(i)
            dfs(l+1)
            ans.pop()
dfs(0)