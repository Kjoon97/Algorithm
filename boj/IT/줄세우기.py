import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
p = int(input())
lines =[]
for t in range(p):
    line = list(map(int,input().split()))[1:]
    cnt=0
    #이전 줄 슨 사람이랑 비교.
    for i in range(1,20):
        for j in range(i):
            if line[j]>line[i]:
                cnt+=1

    print(t+1,cnt)