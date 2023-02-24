import sys
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
'''
1. 문제:
* 최대한 긴 과자를 나눠주려고 함
* 동일한 과자 길이로!
* M명의 조카, N개의 과자가 있음. 
* 1명에게 줄 수 있는 과자 길이의 최댓 값은?
2.입력:
* M:조카의 수(10^7), N:과자의 수(10^7)
* 과자의 길이. 
'''
m,n = map(int,input().split())
snacks = list(map(int,input().split()))
max_len = max(snacks)


def Cnt(len):
    return sum([x//len for x in snacks])


def binary_search(target,start,end):
    res=0
    while start<=end:
        mid = (start+end)//2
        if mid==0:
            mid=1
        if Cnt(mid)>=target:
            res=mid
            start=mid+1
        else:
            end=mid-1
    return res

if sum(snacks)//m==0:
    ans=0
else:
    ans = binary_search(m,0,max_len)
print(ans)