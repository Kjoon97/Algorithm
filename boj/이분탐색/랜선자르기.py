import sys
sys.stdin = open("input.txt","r")
'''
1. 문제:
모두 제각각 다른 k개의 랜선을 길이가 모두 같은 n개의 랜선
2. 입력: 
k:가지고 있는 랜선의 개수(~10^4), n:필요한 랜선의 개수(~10^6)
3. 출력:
만들 수 있는 랜선 최대 길이 구하라.
주어진 랜선 길이 범위 안에서 정답을 도출할 수 있기 때문에 이분 탐색을 수행한다. 
'''
k, n = map(int,input().split())
nums = [int(input()) for _ in range(k)]
m = max(nums)

def binary_search(target,start,end):
    while start<=end:
        mid = (start+end)//2
        temp = [x//mid for x in nums]
        cnt = sum(temp)
        if cnt>=target:
            res=mid
            start=mid+1
        else:
            end=mid-1
    return res

result = binary_search(n,1,m)
print(result)