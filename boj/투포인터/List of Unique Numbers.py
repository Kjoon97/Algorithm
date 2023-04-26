import sys
sys.stdin = open("input.txt","r")

n = int(input())
num_list = list(map(int,input().split()))

result = 0
start, end = 0, 0

seq = [False] * 100001

while start < n and end <n:
    if seq[num_list[end]] == False: #start부터 end까지 중복 숫자가 없으면
        seq[num_list[end]] = True
        result += end-start+1
        end+=1
    else:
        seq[num_list[start]]=False #end를 포함하여 만들 수 있는 수열의 개수.
        start+=1

print(result)