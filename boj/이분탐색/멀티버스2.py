import sys
sys.stdin =open("input.txt","r")
'''
1.문제:
    M개의 우주, 각 우주에는 1~N까지의 행성이 있음    
    행성의 크기로 균등한 우주쌍 개수 구하기-순서 무시.
2.입력:
    M:우주의 개수(2~10^2), N:행성의 개수(3~10^4).
    1번 우주부터 행성 나열.
3.출력:
    균등한 우주쌍 구하기
'''
import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)
for _ in range(m):
    planets = list(map(int,input().split()))
    keys = sorted(list(set(planets)))
    ranks = {keys[i]:i for i in range(len(keys))}
    add = tuple([ranks[x] for x in planets])
    universe[add]+=1

ans = 0
for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2
print(ans)