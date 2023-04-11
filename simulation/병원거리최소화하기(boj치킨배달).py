import sys
sys.stdin = open("input.txt",'r')
'''
1.문제:
* n*n크기의 도시
* 사람의 병원 거리: 가장 가까운 병원 
* m개의 병원만을 남겨두고 나머지 페업. 각 병원에 대한 각 사람들의 거리 총합이 최소가 되도로가자. 
2. 입력:
* n(크기), m개 
* 0:빈칸, 1: 사람, 2:병원
3. 출력:
* 병원 m개일 때, 각 사람 들의 병원 거리 총 최소 합 구하기.
'''
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
hospitals = []
peoples = []
choose_hospital_index =[]

#사람, 병원 위치 저장
for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            peoples.append((i,j))
        elif city[i][j]==2:
            hospitals.append((i,j))

# 각 케이스 별로 최소 거리 합 구하기.
def cal(choose_hospital_index):
    sum_=0
    #한 사람 당 모든 병원의 거리 재고 최솟 거리 구하기.
    for people in peoples:
        min_val = 2147000000
        for h_index in choose_hospital_index:
            # print(abs(hospitals[h_index][0]-people[0]) + abs(hospitals[h_index][1]-people[1]))
            min_val = min(abs(hospitals[h_index][0]-people[0]) + abs(hospitals[h_index][1]-people[1]), min_val)
        min_dis = min_val
        #모든 사람들의 병원 최소 거리 합.
        sum_ += min_dis
    return sum_

ans = 2147000000

#총 병원 개수 중 m개 병원 고르기(조합) -
def dfs(L,idx):
    global ans
    if L == m:
        #각 케이스 별 최소 거리 합 중에서도 최소 값 구하기.
        ans= min(ans,cal(choose_hospital_index))
        return
    else:
        #총개수에서 m개 고를 수 있는 경우의 인덱스 저장.
        for i in range(idx,len(hospitals)):
            choose_hospital_index.append(i)
            dfs(L+1,i+1)
            choose_hospital_index.pop()

dfs(0,0)
print(ans)