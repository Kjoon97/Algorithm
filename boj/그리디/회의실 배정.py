import sys
#sys.stdin = open("input.txt")
input = sys.stdin.readline
'''
팁: 끝나는 시간, 시작하는 시간 오름차순으로 정렬하면 된다.
'''
n = int(input())
time = [list(map(int,input().split())) for _ in range(n)]
time = sorted(time,key=lambda x: (x[1], x[0]))

cnt = end =0

for s,e in time:
    if s>=end:
        cnt+=1
        end=e

print(cnt)
