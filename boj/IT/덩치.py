import sys
sys.stdin = open("input.txt","r")

n = int(input())
people = list()
for _ in range(n):
    x,y = map(int,input().split())
    people.append((x,y))

for p in people:
    rank =1
    for j in people:
        if p[0] < j[0] and p[1] < j[1]:
            rank+=1
    print(rank, end=" ")


'''
그냥 자기보다 크고 무거운(둘 다 큰) 사람이 몇 명인지 쟤서 자기 등수만 정하면 된다. n명을 n-1번씩 전수 비교해보면 된다.
'''