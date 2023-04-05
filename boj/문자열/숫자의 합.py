import sys
sys.stdin = open("input.txt","r")

n = int(input())
nums = list(map(int,input()))
print(sum(nums))