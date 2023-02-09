import sys

sys.stdin = open("input.txt","r")

'''
1. 일의 양 - n - 2의 배수, 
2. 업무 간의 상성 Pij
'''

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
indexs = []
works = []
def dfs(idx,cnt):
    if cnt ==n//2:
        work =0
        for i in range(len(indexs)):
            for j in range(len(indexs)):
                if i==j:
                    continue
                else:
                    work += board[indexs[i]][indexs[j]]
        works.append(work)
        # print(indexs)
    else:
        for i in range(idx,n):
            indexs.append(i)
            dfs(i+1,cnt+1)
            indexs.pop()

dfs(0,0)
# print(works)

min_val = 2147000000
wl = len(works)
for i in range(wl//2):
    sum_ = abs(works[i]-works[wl-1-i])
    min_val = min(sum_, min_val)
print(min_val)
