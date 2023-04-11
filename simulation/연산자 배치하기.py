import sys
sys.stdin = open("input.txt",'r')

'''
*문제:
1. 주어진 정수 순서 바꿀 수 x
2. 연산자: 덧셈, 뺄셈, 곱셈
3. 연산 -> 앞에서부터 차례로 연산.
4. 가능한 최솟값과 최댓값 구하기.

*입력:
1.n -> 2~11
2.n개의 정수 공백을 두고 주어짐.
3.사용 가능한 덧셈, 뺄셈, 곱셈 개수 
'''
def dfs(i, now):
    global min_value, max_value, add, sub,mul
    if i == n:
        min_value= min(min_value,now)
        max_value = max(max_value,now)
    else:
        if add>0:
            add-=1
            dfs(i+1, now+nums[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1, now-nums[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1, now*nums[i])
            mul+=1

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul = map(int, input().split())
min_value = 2147000000
max_value= -2147000000
dfs(1,nums[0])
print(min_value,max_value)