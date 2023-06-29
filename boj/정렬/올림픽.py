import sys
#sys.stdin = open("input.txt","r")

n,k = map(int,input().split())
medals = [list(map(int, input().split())) for _ in range(n)]

medals.sort(key= lambda x: (x[1],x[2],x[3]), reverse=True)

idx = [medals[i][0] for i in range(n)].index(k)  #국가 K에 해당하는 인덱스를 찾아야한다.

'''
동점국가가 존재하는지 검사해준다.
N개의 국가를 확인해서 만약 국가 K의 메달 수와 일치하는 국가가 존재한다면, 그 인덱스의 +1이 등수가 될 것이다.
일치하는게 본인일 경우는 동점자의 첫번째 인덱스 순위이거나 동점자가 없을 경우일 것이다.
'''
for i in range(n):
    if medals[idx][1:] == medals[i][1:]:
        print(i+1)
        break
