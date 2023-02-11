import sys
sys.stdin = open("input.txt","r")
n, k = map(int, input().split())
from collections import deque
q = deque()
MAX = 10**5
q.append((n,0))
memo = {}
while q:
    loc, cnt = q.popleft()
    memo[loc]=0   #key에 데이터 저장하고 value에는 걍 임의값 0 넣음
    if loc == k:
        print(cnt)
        break
    else:
        for nl in(loc-1, loc+1, loc*2):
            if 0<=nl<=MAX and nl not in memo:   #in 연산자를 리스트로 쓰면 O(N)이 걸리므로 시간초과. 딕셔너리 이용하면 O(1)
                q.append((nl,cnt+1))