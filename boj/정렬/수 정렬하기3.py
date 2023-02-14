import sys
#입력되는 숫자가 많기 때문에 리스트를 생성하고 append하는 방식은 메모리 초과 남. 메모리 제한:8 MB
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
n = int(input())

#숫자가 1~10000
num_list = [0]*10001

for _ in range(n):
    num_list[int(input())]+=1

for i in range(10001):
    if num_list[i]!=0:
        for _ in range(num_list[i]):
            print(i)