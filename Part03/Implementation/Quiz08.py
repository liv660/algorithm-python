# p.322 기출문제 08 - 문자열 재정렬

data = list(input())
# print("data:", data)

# 1. 문자, 숫자 쪼개기
data_str = []
value = 0
for i in data:
  temp = ord(i)
  if temp < 48 or temp > 57: # 문자일 때
    data_str.append(i)
  else:
    value += int(i)
data_str.sort()

# 2. 문자, 숫자 재조합
result = ""
for i in data_str:
  result += i
result += str(value)
print(result)