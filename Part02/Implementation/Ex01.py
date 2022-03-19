# p.110 예제 01 - 상하좌우

N = int(input())
data = list(input().split())
# print(N, data)

x, y = 1, 1
# print(y, x)

for i in data:
  if i == 'L':
    if(y >= 2): y -= 1
  elif i == 'R':
    if(y + 1 <= N): y += 1
  elif i == 'U':
    if(x >= 2): x -= 1
  else: # i == 'D'
    if(x + 1 <= N): x += 1

print("(x,y) =", x, y)