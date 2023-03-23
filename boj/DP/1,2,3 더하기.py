import sys
sys.stdin = open("input.txt","r")
# f(n) = f(n-1)+f(n-2)+f(n-3) (n>=3)

# top-down 방식(재귀 사용)
t = int(input())
def dp1(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 4
    else:
        return dp1(x-1)+dp1(x-2)+dp1(x-3)

for _ in range(t):
    n = int(input())
    print(dp1(n))


'''
bottom-up 방식(반복문 사용):

t = int(input())

def dp2(x):
    for i in range(4,x+1):
        d[i] = d[i-1]+d[i-2]+d[i-3]


for _ in range(t):
    n = int(input())
    d = {1: 1, 2: 2, 3: 4}
    dp2(n)
    print(d[n])
    
'''