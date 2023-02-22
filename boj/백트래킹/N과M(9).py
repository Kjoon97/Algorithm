import sys
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
visited =[False]*n
ans =[]

def dfs():
    if len(ans)==m:
        print(*ans)
        return

    remember_me=0
    for i in range(n):
        #같은 숫자 중복x, 반복문 안에서 이전 숫자랑 다른지 검사
        if not visited[i] and remember_me !=nums[i]:
            visited[i]=True
            ans.append(nums[i])
            remember_me = nums[i]
            dfs()
            visited[i]=False
            ans.pop()

dfs()