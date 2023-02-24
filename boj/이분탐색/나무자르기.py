import sys
#sys.stdin =open("input.txt","r")
input = sys.stdin.readline
'''
1.문제:
상근 - 나무 M미터 필요.
목재 절단기 - 높이 h(0<=) 지정. 
잘린 부분을 모두 집에 가져감.
최소 필요한 만큼만 자름. 
적어도 M미터의 나무를 가져가기 위해 설정할 수 있는 높이의 최댓값을 구하라.
2. 입력:
n:나무의 수(<=10^5), M:상근이가 필요한 길이.
나무 높이 - 높이의 합은 항상 >=M
3. 출력:
절단기 높이 최댓 값 출력.
'''
n, m  = map(int,input().split())
trees = list(map(int,input().split()))
m_tree = max(trees)

def Cnt(len):
    cutted_trees=[]
    for tree in trees:
        if tree>=len:
            cutted_trees.append(tree-len)

    return sum(cutted_trees)

def binary_search(target,start,end):
    while start<=end:
        mid=(start+end)//2
        if Cnt(mid)>=target:
            res = mid
            start=mid+1
        else:
            end=mid-1
    return res

print(binary_search(m, 0,m_tree))