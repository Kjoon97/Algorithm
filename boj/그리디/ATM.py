import sys
#sys.stdin = open("input.txt","r")
n = int(input())
time = list(map(int,input().split()))
time.sort()
people = [0]*n
s =0
for i,t in enumerate(time):
    s+=t
    people[i] = s
print(sum(people))