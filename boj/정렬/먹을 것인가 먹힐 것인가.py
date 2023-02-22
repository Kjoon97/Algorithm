import sys
sys.stdin = open("input.txt","r")
'''
1.문제:

2.입력:
t:테스트 케이스
n:A의 수, M:B의 수.
A의 크기들
B의 크기들.
3.출력:
A가 B보다 큰 쌍의 개수 구하시오.

주의: n,m이 20000개이므로 완전 탐색으로 이중 for문 돌리면 시간 초과 됨=> 이분 탐색으로 풀자.
'''
t = int(input())

def binary_search(target,data):
    start=0
    end=len(data)-1
    res=-1
    while start<=end:
        mid = (start + end) // 2
        if data[mid]<target:
            start=mid+1
            res=mid
        else:
            end=mid-1
    return res

for _ in range(t):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt=0
    for a in A:
        cnt+=binary_search(a,B)+1
    print(cnt)