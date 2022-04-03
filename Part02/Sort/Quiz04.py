# p.182 실전문제 04 - 두 배열의 원소 교체

# 1. 입력
N, K = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

# 2. A는 오름차순, B는 내림차순 정렬
list_a.sort()
list_b.sort(reverse=True)
print(list_a, list_b)
e
# 3. K번 바꿔치기 후 최댓값 출력
for i in range(K):
    if list_a[i] < list_b[i]:
        list_a[i] = list_b[i]   # b에서 가장 큰 값 -> a로
    else:
        break
print(sum(list_a))