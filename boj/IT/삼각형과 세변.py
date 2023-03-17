import sys
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
while True:
    a,b,c = map(int, input().split())
    num = [a,b,c]
    m = max(num)
    num.remove(m)
    r = m - sum(num)
    if a+b+c == 0:
        break
    if a==b==c:
        print("Equilateral")
    elif r>=0:
        print("Invalid")
    elif a==b or a==c or b==c:
        print("Isosceles")
    else:
        print("Scalene")