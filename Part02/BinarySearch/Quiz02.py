# p.197 실전문제 02 - 부품 찾기
import sys

# 1. 입력
N = int(sys.stdin.readline().rstrip())
store_ls = list(map(int, sys.stdin.readline().rstrip().split()))
store_ls.sort()

M = sys.stdin.readline().rstrip()
buy_ls = list(map(int, sys.stdin.readline().rstrip().split()))

# 2. 이진 탐색으로 구현하기
def getItem(store_ls, target, start, end):
    # 탈출 조건
    if start > end:
        return -1

    # 중간번째 인덱스
    mid = (start + end) // 2

    # 이진 탐색
    if target == store_ls[mid]:
        return mid
    elif target < store_ls[mid]: # 중간번째 요소보다 작을 때
        return getItem(store_ls, target, start, mid-1)
    else:   # 중간번째 요소보다 클 때
        return getItem(store_ls, target, mid+1, end)
    return -1

def chageYorN(value):
    if value >= 0:
        return "yes "
    return "no "

# 3. 탐색 및 출력
S = ""
for i in buy_ls:
    S += (chageYorN(getItem(store_ls, i, 0, N)))

print(S)




