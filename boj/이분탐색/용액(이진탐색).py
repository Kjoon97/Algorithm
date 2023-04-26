import sys
#sys.stdin = open("input.txt","r")
n = int(input())
arr = list(map(int,input().split()))

ans = 2147000000
ans_left=0
ans_right=0

for i in range(n-1):
    current = arr[i]

    start=i+1
    end = n-1

    while start<=end:
        mid = (start+end)//2
        tmp = current+arr[mid]

        if abs(tmp) <ans:
            ans = abs(tmp)
            ans_left=i
            ans_right= mid

            if tmp == 0:
                break
        if tmp<0:
            start= mid+1
        else:
            end = mid-1

print(arr[ans_left], arr[ans_right])