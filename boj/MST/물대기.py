import sys
import heapq
#sys.stdin = open("input.txt","r")
n = int(input())
q =[]
pay_list =[]

for i in range(n):
    pay = int(input())
    heapq.heappush(q,(pay,i))
    pay_list.append(pay)


connect_list = [list(map(int,input().split())) for _ in range(n)]

visited =[False]*(n)
result=0
while q:
    pay, en = heapq.heappop(q)
    if visited[en]==False:
        visited[en]=True
        result+=pay

        for nn in range(n):
            if nn!=en:
                if pay_list[nn]>connect_list[en][nn]:
                    pay_list[nn]=connect_list[en][nn]
                    heapq.heappush(q,(pay_list[nn],nn))

print(result)