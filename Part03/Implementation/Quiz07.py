# p.321 기출문제 07 - 럭키 스트레이트

value = list(str(int(input())))
# print("value:", value)

mid = len(value) // 2
# print("mid:", mid)

left_sum, right_sum = 0, 0
for i in range(len(value)):
  if(i < mid):
    left_sum += int(value[i])
  else:
    right_sum += int(value[i])
  # print("left, right:", left_sum, right_sum)

if(left_sum == right_sum): print("LUCKY")
else: print("READY")