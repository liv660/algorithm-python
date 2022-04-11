# p.201 실전문제 03 - 떡볶이 떡 만들기
import sys

# 1. 입력
N, M = map(int, sys.stdin.readline().rstrip().split())
dduck = list(map(int, sys.stdin.readline().rstrip().split()))
dduck.sort()

# 2. 이진 탐색
start, end, result = 0, max(dduck), 0
# S = "START\t\tEND\t\tMID(result)\t\ttotal\n"  # log_1

while start <= end:
    temp_total = 0
    mid = (start + end) // 2

    # S += (str(start) + "\t\t\t" + str(end) + "\t\t\t" + str(mid) +"\t\t\t")   # log_2

    for i in dduck:
        if i > mid:
            temp_total += (i-mid)

    # S += (str(temp_total) + "\n") # log_3

    if temp_total < M:
        end = (mid-1)
    else:
        result = mid
        start = (mid + 1)

print(result)
# print(S)  # log_4
