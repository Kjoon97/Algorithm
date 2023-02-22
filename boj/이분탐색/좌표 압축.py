import sys
sys.stdin = open("input.txt","r")

n = int(input())
nums = list(map(int,input().split()))
sorted_nums = sorted(list(set(nums)))
# print(nums)
# print(sorted_nums)


def bs(arr,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None


for n in nums:
    result = bs(sorted_nums,n,0,len(sorted_nums)-1)
    print(result, end=" ")