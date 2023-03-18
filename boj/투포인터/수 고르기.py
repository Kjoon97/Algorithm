import sys
sys.stdin = open("input.txt","r")

'''
n개의 수열에서 두 수를 골랐을 때, 그 차이 >=m , 제일 작은 경우 구하기.
'''
n, m = map(int,input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))

#투포인터를 하기 위해 정렬.
nums.sort()

left, right = 0,1
min_val = 2147000000

while left<=right and right<n:
    diff = nums[right]-nums[left]
    if diff == m:
        print(diff)
        exit(0)
    elif diff>m:
        min_val = min(min_val,diff)
        left+=1
    else:
        right+=1

print(min_val)