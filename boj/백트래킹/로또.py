import sys
sys.stdin = open("input.txt", "r")

def dfs(l, s):
    if l == 6:
        print(*ans)
        return
    else:
        for i in range(s, k):
            if nums[i] not in ans:
                ans.append(nums[i])
                dfs(l + 1, i + 1)
                ans.pop()


while True:
    ans = []
    nums = list(map(int, input().split()))
    k = nums.pop(0)
    if k == 0:
        break
    dfs(0, 0)
    print()
