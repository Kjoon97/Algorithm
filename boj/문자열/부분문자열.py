import sys
sys.stdin = open("input.txt","r")
'''
s의 문자들로 구성된 큐를 생성한다.
t의 문자들을 왼쪽에서 오른쪽으로 순서대로 비교
큐의 맨 앞 요소가 t의 문자와 같다면 제거 후 다음 문자 진행
큐의 맨 앞 요소가 t의 문자와 같지 않다면 그냥 다음 문자 진행
큐가 비어있다면 부분 문자열이고, 큐가 비어있지 않다면 부분 문자열이 아닌 것으로 볼 수 있다. 
'''
from collections import deque

while True:
    try:
        s,t = input().split()
        q = deque(list(s))

        for c in t:
            if q and c ==q[0]:
                q.popleft()

        if q:
            print("No")
        else:
            print("Yes")
    except:
        break