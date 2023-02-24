import sys
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
a_cnt, b_cnt = list(map(int,input().split()))
a = list(map(int,input().split()))
b = sorted(list(map(int,input().split())))
#a에는 속하고, b에는 속하지 않는 것
cnt=0
def binary_search(arr,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return None
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return target
ans=[]
for v in a:
    result = binary_search(b, v, 0, b_cnt - 1)
    if result==None:
        continue
    else:
        ans.append(result)
print(len(ans))
ans.sort()
for x in ans:
    print(x, end=" ")