import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
n = int(input())
a=sorted(list(map(int,input().split())))
m = int(input())
b=list(map(int,input().split()))

#이분 탐색 이용하기 -> 시간 복잡도 O(logN)
def binary_search(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None


for x in b:
    if binary_search(a,x,0,n-1)==None:
        print(0)
    else:
        print(1)

'''
set or dict를 이용하는 방법. -> 시간 복잡도 O(1)
set, dict은 in연산자로 탐색할 경우 시간 복잡도 O(1)이므로 빠르다. 
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
for x in b:
    if x not in a:
        print(0)
    else:
        print(1)
'''