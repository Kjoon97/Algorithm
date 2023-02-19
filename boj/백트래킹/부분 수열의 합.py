import sys
sys.stdin = open("input.txt","r")

n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

def dfs(l, sum_nums):
    global ans

    if l >= n:
        return

    sum_nums += nums[l]

    if sum_nums == s:
        ans += 1

    dfs(l + 1, sum_nums)
    dfs(l + 1, sum_nums - nums[l])

dfs(0, 0)
print(ans)