import sys
sys.stdin = open("input.txt","r")
# 1<=수의 갯수<= 10^6, 숫자는 10^6이하의 정수, 메모리 제한: 256mb

nums = []
n = int(input())
for _ in range(n):
    nums.append(int(input()))

nums.sort()      #O(nlogn)
nums.reverse()   #O(n)

for n in nums:
    print(n)