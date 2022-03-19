# p.115 실전문제 02 - 왕실의 나이트

x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
loc = list(input())
min, max = 1, len(x_list)
# print(loc, min, max)

x, y = x_list.index((loc[0])) + 1, int(loc[1])
# print(x, y)

cnt = 0
# 수평2 + 수직1
if (x + 2 <= max):  # 오른쪽 방향으로
  if (y - 1 >= min): cnt += 1
  if (y + 1 <= max): cnt += 1

if (x - 2 >= min):  # 왼쪽 방향으로
  if (y - 1 >= min): cnt += 1
  if (y + 1 <= max): cnt += 1

# 수직2 + 수평1
if (y + 2 <= max):  # 아래 방향으로
  if (x - 1 >= min): cnt += 1
  if (x + 1 <= max): cnt += 1

if (y - 2 >= min):  # 위 방향으로
  if (x - 1 >= min): cnt += 1
  if (x + 1 <= max): cnt += 1

print("경우의 수:", cnt)