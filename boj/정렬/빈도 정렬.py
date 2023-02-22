import sys
sys.stdin = open("input.txt","r")

'''
1. 문제:
* 메세지: n개의 수열- 숫자<=c
* 이 숫자를 빈도 순으로 정렬하고자 함. 많이 등장하는 순으로.
* 등장 횟수가 같으면 먼저 나온 것 순.
2. 입력:
* n: 메세지 길이, 숫자<=c
* 메세지 수열
3. 출력:
* 빈도 정렬 한 값
'''
n, c = map(int,input().split())
message = list(map(int,input().split()))
md = {x:0 for x in message}
for m in message:
    md[m]+=1
# print(md)
md = [(k,x) for k,x in md.items()]
# print(md)

newlist =[]
#순서 고려한 리스트- 개수와 순서를 같이 한꺼번에 reverse=True로 정렬하기 위해 순서는 역순으로 저장했음.
for i,t in enumerate(md):
    newlist.append((t[0],t[1],len(md)-i))

#값, 개수, 순서(순서가 빠를 수록 큰 숫자).

#개수, 순서 별로 정렬.
newlist.sort(key=lambda x: (x[1],x[2]), reverse=True)
# print(newlist)

for n in newlist:
    v = n[0]
    count = n[1]
    for _ in range(count):
        print(v, end=" ")
