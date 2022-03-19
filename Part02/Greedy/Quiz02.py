# p.92 실전문제 02 - 큰 수의 법칙

N, M, K = map(int, input().split())
# print("N M K :", N, M, K)

data = list(map(int, input().split()))
# print("data:", data)

data.sort(reverse = True)
# print("내림차순:", data)

i = 0
flag = 0
result = 0

while i < M:
  if (flag < K):
    result += data[0]
    flag += 1
  else:
    result += data[1]
    flag = 0
  i += 1

print("큰 수:", result)