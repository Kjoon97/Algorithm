import sys

sys.stdin = open("input.txt","r")

n = int(input())


for _ in range(n):
    d = {chr(x): 0 for x in range(97, 123)}
    sentence = list(input().replace(' ',''))
    for s in sentence:
        d[s]+=1
    d = list(d.items())
    d.sort(key = lambda x: x[1], reverse=True)


    if d[0][1]!=d[1][1]:
        print(d[0][0])
    else:
        print("?")
