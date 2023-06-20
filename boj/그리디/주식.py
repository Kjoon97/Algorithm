import sys
sys.stdin = open("input.txt","r")

t = int(input())
for _ in range(t):
    n = int(input())
    cycle = list(map(int,input().split()))

    ans = 0
    max_v =0

    for i in range(len(cycle)-1,-1,-1):
        if cycle[i] > max_v:
            max_v = cycle[i]
        else:
            ans+=max_v-cycle[i]

    print(ans)