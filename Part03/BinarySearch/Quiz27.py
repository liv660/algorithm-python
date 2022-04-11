# p.367 기출문제 27 - 정렬된 배열에서 특정 수의 개수 구하기

import sys

# 1. 입력
N, x = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

# 2. 이진 탐색
def findX(ls, x, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if x == ls[mid]:
        return mid
    elif x < ls[mid]:
        return findX(ls, x, start, mid-1)
    else:
        return findX(ls, x, mid+1, end)
    return -1

# 3. x 찾기
mid = N // 2
front = findX(data, x, 0, mid)  # 가장 앞에 등장하는 x의 인덱스 = bisect_left(a,x)
data.sort(reverse=True)
behind = findX(data, x, 0, mid) # 가장 뒤에 등장하는 x의 인덱스 = bisect_right(a,x)

if front == -1 and behind == -1:
    print(-1)
else:
    print(N - behind - front)