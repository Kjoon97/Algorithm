import sys
sys.stdin = open("input.txt","r")
n = int(input())
arr = list(map(int,input().split()))

left = 0
right = n-1
answerL =0
answerR =0
min_v = 2147000000

while left < right:
    sum_v = arr[left]+arr[right]

    if abs(sum_v)<min_v:
        answerL = left
        answerR = right
        min_v = abs(sum_v)

    if sum_v >0:
        right-=1
    elif sum_v <0:
        left+=1
    else:
        break

print(arr[answerL],arr[answerR])