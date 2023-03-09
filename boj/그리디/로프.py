import sys
sys.stdin = open("input.txt","r")
'''
문제.
1. n개의 로프가 있음.<=10^5
2. 굴기, 길이가 각각 다름.
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프 - w/k
로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량은?
모든 로프를 사용할 필요x.
'''

n= int(input())
rope = list()
value =list()

for _ in range(n):
    rope.append(int(input()))

#내림차순으로 정렬
rope.sort(reverse=True)
# print(rope)

for i in range(n):
    value.append(rope[i]*(i+1))

#규칙: 내림차순 정렬 후 1번째 값은 1번만 버틸 수 있고, 2번째 값은 1번과 2번이 버틸 수 있기 때문에
#들 수 있는 무게: rope[N]*N번째
print(max(value))