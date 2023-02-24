import sys
#sys.stdin = open("input.txt","r")
input=sys.stdin.readline
n= int(input())
s_cards = sorted(list(map(int,input().split())))
m = int(input())
cards = list(map(int,input().split()))

def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

for c in cards:
    result=binary_search(s_cards,c,0,len(s_cards)-1)
    if result==None:
        print(0, end=" ")
    else:
        print(1, end=" ")

