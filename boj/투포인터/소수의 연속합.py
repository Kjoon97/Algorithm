import sys
sys.stdin = open("input.txt","r")
#n이 <=4*10^6이므로 백트래킹시 시간 초과 -> 투포인터로 풀기.
'''
에라토스테네스의 체와 투포인터 함께 사용하기
에라토스테네스의 체 : 소수를 구하는 알고리즘으로 어떤 수를 확인, 그것의 제곱수+배수들 제외.2는 4,6,8,10... 3은 9,12,15,18.. 소수 체크하는데 시간을 줄여줌.
'''
n = int(input())

#에라토스테네스의 체
primeList=[]
array = [False,False]+[True]*(n-1)

for i in range(2,n+1):
    if array[i]:
        primeList.append(i)
    for j in range(i*i,n+1,i):
        array[j]=False

#투포인터
start,end =0,0
cnt=0

while end<=len(primeList):
    psum = sum(primeList[start:end])
    if psum == n:
        cnt+=1
        end+=1
    elif psum<n:
        end+=1
    else:
        start+=1

print(cnt)