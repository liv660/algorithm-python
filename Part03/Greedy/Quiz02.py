# p.312 기출문제 02 - 곱하기 혹은 더하기

S = list(map(int, list(input())))
# print(S)

result = 0
for i in S:
  if (i == 0):
    pass

  if (result == 0 or result == 1 or i == 1):
    result += i
  else:
    result *= i

print(result)