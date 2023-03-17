import sys
sys.stdin = open("input.txt","r")

n = int(input())
house_nums =1
cnt =1
while n > house_nums:
    house_nums+=6*cnt  #벌집 증가
    cnt+=1
print(cnt)