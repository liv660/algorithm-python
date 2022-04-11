# p.368 기출문제 28 - 고정점 찾기
import sys
import numpy as np

# 1. 입력
N = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))

# 2. 이진 탐색
def findFixedPoint(ls, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if mid == ls[mid]:
        return mid
    elif mid < ls[mid]:
        return findFixedPoint(ls, start, mid-1)
    else:
        return findFixedPoint(ls, mid+1, end)
    return -1

# 3. 고정점 찾기
temp = np.array(data)
start = np.where(temp > 0)[0][0]    # 0보다 큰 요소부터

print(findFixedPoint(data, start, N))