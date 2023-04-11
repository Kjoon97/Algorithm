import sys

sys.stdin = open("input.txt", "r")

'''
문제
* n일 휴가 동안
* 외주 작업 - 하루에 1개씩, 걸리는 기한: t, 수익: p
* 한번에 하나씩 가능
* 외주 수익의 최댓 값 구하라

입력:
n
걸리는 기한 t, 수익 p
'''
t_l=[]
p_l=[]
n = int(input())

for i in range(n):
    t, p = map(int, input().split())
    t_l.append(t)
    p_l.append(p)

t_l.insert(0,0)
p_l.insert(0,0)
ans = 0
def dfs(L,sum_money):
    global ans
    if L>=n+1:
        ans = max(ans,sum_money)
        return
    else:
        if L+t_l[L] <= n+1:    ### 중요!!! 해당일에서 걸리는 날이 n+1보다 작거나 같아야함. 예를 들어 7(마지막날)+1(당일 처리) = 8까지 인정.
            dfs(L+t_l[L],sum_money+p_l[L])
        dfs(L+1,sum_money)

dfs(1,0)
print(ans)