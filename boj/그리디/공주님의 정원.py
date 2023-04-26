import sys
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
'''
* 문제:
n개의 꽃이 있음 - 모두 같은 해에 피고 같은 해에 진다.피는 날과 지는날이 정해짐. 
n개의 꽃들 중 다음 두 조건을 만족하는 꽃들을 선택하자.
1. 3월1일~11월30일까지 매일 꽃이 한가지 이상 피어있게 하자.
2. 정원에 심는 꽃들 수 최대한 적게하자.

선택한 꽃들의 최소 개수를 출력하자.

*입력:
꽃 총 개수:n개
피는 날짜, 지는 날짜(월,일)
'''

n = int(input())

arr = []

for _ in range(n):
    sm, sd, em, ed = map(int,input().split())
    arr.append((sm*100+sd,em*100+ed)) # 꽃이 피고 지는 날짜에 대해 월에 100을 곱한 뒤, 일이랑 덧셈

# 꽃이 피는 날짜, 꽃이 지는 날짜순으로 오름차순 정렬
arr.sort()

end_date = 301   # 정원의 마지막 꽃이 지는 날짜
count =0         # 심은 꽃의 개수
max_end_date = -1    # 꽃이 피는 날짜가 end_date 이전일 때, 가장 느리게 지는 꽃의 날짜

# 더 이상 확인할 꽃이 없을때까지 반복.
while arr:
    # 정원의 마지막 꽃이 지는 날짜가 12월 1일 이상이 됐거나,
    # 현재 확인할 꽃의 시작 날짜가 정원의 마지막 꽃이 지는 날짜와 이어지지 않을 경우, 탐색 종료
    if end_date>=1201 or arr[0][0] > end_date:
        break


    for _ in range(len(arr)):
        if arr[0][0] <= end_date:    # 꽃이 피는 날짜가 end_date 이전이라면,
            if max_end_date <= arr[0][1]:   # 그 중 가장 느리게 지는 꽃의 날짜를 확인
                max_end_date = arr[0][1]

            arr.pop(0)                    # 확인한 꽃은 원본 배열에서 제거
        else:
            break

    end_date = max_end_date        # 가장 꽃이 느리게 지는 날짜를 end_date로 수정
    count+=1                       # 심은 꽃의 개수 증가


# 마지막으로 확인한 꽃의 지는 날짜가 12월 1일 보다 작으면,
# 3월 1일부터 11월 30일까지 계속 피어있는게 아니므로 0 출력
if end_date < 1201:
    print(0)
else:
    print(count)